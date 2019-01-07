from collections import defaultdict
import json

try:
    import taxcalc
except ModuleNotFoundError:
    pass

from webapp.apps.core.parser import ParamData, Parser
from webapp.apps.core.utils import is_wildcard, is_reverse

class TaxcalcStyleParser(Parser):

    def unflatten(self, parsed_input):
        """
        Convert fields style dictionary to json reform style dictionary
        For example:
        start_year = 2017, cls = taxcalc.Policy
        fields = {'_CG_nodiff': [False]},
                '_FICA_ss_trt': ["*", 0.1, "*", 0.2],
                '_ID_Charity_c_cpi': True,
                '_EITC_rt_2kids': [1.0]}
        to
        revision = {'_CG_nodiff': {'2017': [False]},
                    '_FICA_ss_trt': {'2020': [0.2], '2018': [0.1]},
                    '_ID_Charity_c_cpi': {'2017': True},
                    '_EITC_rt_2kids': {'2017': [1.0]}}

        returns: json style revision
        """
        number_reverse_operators = 1

        revision = {}
        for param in parsed_input:
            revision[param] = {}
            if not isinstance(parsed_input[param], list):
                assert isinstance(
                    parsed_input[param], bool
                ) and param.endswith("_cpi")
                revision[param][str(self.start_year)] = parsed_input[param]
                continue
            i = 0
            while i < len(parsed_input[param]):
                if is_wildcard(parsed_input[param][i]):
                    # may need to do something here
                    pass
                elif is_reverse(parsed_input[param][i]):
                    # only the first character can be a reverse char
                    # and there must be a following character
                    assert len(parsed_input[param]) > 1
                    # set value for parameter in start_year - 1
                    assert isinstance(
                        parsed_input[param][i + 1], (int, float)
                    ) or isinstance(parsed_input[param][i + 1], bool)
                    revision[param][str(self.start_year - 1)] = [
                        parsed_input[param][i + 1]
                    ]

                    # realign year and parameter indices
                    for op in (0, number_reverse_operators + 1):
                        parsed_input[param].pop(0)
                    continue
                else:
                    assert isinstance(
                        parsed_input[param][i], (int, float)
                    ) or isinstance(parsed_input[param][i], bool)
                    revision[param][str(self.start_year + i)] = [
                        parsed_input[param][i]
                    ]

                i += 1

        return revision


    @staticmethod
    def get_default_param(param, defaults, param_get=None, raise_error=True):
        """
        Map webapp field name to Upstream package parameter name. This is a
        static method because:
        1. it doesn't access any Instance or Class data
        2. it is used as a standalone method to make sure parameter names exist
        3. it is not simply a function because inheriting classes may want to
            override it.

        For example: STD_0 maps to _STD_single

        returns: named tuple with taxcalc param name and metadata
        """
        if param_get is None:
            param_get = lambda d, k: d[k] if k is not None else d
        if param in defaults:  # ex. EITC_indiv --> _EITC_indiv
            return ParamData(param, param_get(defaults[param], None))
        param_pieces = param.split("_")
        end_piece = param_pieces[-1]
        no_suffix = "_".join(param_pieces[:-1])
        if end_piece == "cpi":  # ex. SS_Earnings_c_cpi --> _SS_Earnings_c_cpi
            if no_suffix in defaults:
                return ParamData(param, param_get(defaults[no_suffix], None))
            else:
                if raise_error:
                    msg = "Received unexpected parameter: {}"
                    raise ParameterLookUpException(msg.format(param))
                return None
        if no_suffix in defaults:  # ex. STD_0 --> _STD_single
            try:
                ix = int(end_piece)
            except ValueError:
                if raise_error:
                    msg = "Parsing {}: Expected integer for index but got {}"
                    raise ParameterLookUpException(msg.format(param, end_piece))
                return None
            num_columns = len(param_get(defaults[no_suffix], "col_label"))
            if ix < 0 or ix >= num_columns:
                if raise_error:
                    msg = "Parsing {}: Index {} not in range ({}, {})"
                    raise ParameterLookUpException(
                        msg.format(param, ix, 0, num_columns)
                    )
                return None
            col_label = param_get(defaults[no_suffix], "col_label")[ix]
            return ParamData(
                no_suffix + "_" + col_label, param_get(defaults[no_suffix], None)
            )
        if raise_error:
            msg = "Received unexpected parameter: {}"
            raise ParameterLookUpException(msg.format(param))
        return None

    @staticmethod
    def parse_errors_warnings(errors_warnings):
        """
        Parse error messages so that they can be mapped to webapp param ID. This
        allows the messages to be displayed under the field where the value is
        entered.

        returns: dictionary 'parsed' with keys: 'errors' and 'warnings'
            parsed['errors/warnings'] = {year: {tb_param_name: 'error message'}}
        """
        parsed = {"errors": defaultdict(dict), "warnings": defaultdict(dict)}
        for action in errors_warnings:
            msgs = errors_warnings[action]
            if len(msgs) == 0:
                continue
            for msg in msgs.split("\n"):
                if len(msg) == 0:  # new line
                    continue
                msg_spl = msg.split()
                msg_action = msg_spl[0]
                year = msg_spl[1]
                curr_id = msg_spl[2]
                msg_parse = msg_spl[2:]
                parsed[action][curr_id][year] = " ".join(
                    [msg_action] + msg_parse + ["for", year]
                )
        return parsed

    @staticmethod
    def append_errors_warnings(errors_warnings, append_func):
        """
        Appends warning/error messages to some object, append_obj, according to
        the provided function, append_func
        """
        for action in ["warnings", "errors"]:
            for param in errors_warnings[action]:
                for year in sorted(
                    list(errors_warnings[action][param].keys()),
                    key=lambda x: int(x),
                ):
                    msg = errors_warnings[action][param][year]
                    append_func(param, msg)