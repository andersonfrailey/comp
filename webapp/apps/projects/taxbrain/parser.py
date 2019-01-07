from webapp.apps.contrib.taxcalcstyle.parser import TaxcalcStyleParser
from .displayer import TaxbrainDisplayer

from taxcalc.tbi import parse_user_inputs as _parse_user_inputs

class TaxbrainParser(TaxcalcStyleParser):
    """
    Formats the parameters into the format defined by the upstream project,
    calls the upstream project's validation functions, and formats the errors
    if they exist.
    """
    displayer_class = TaxbrainDisplayer

    def parse_parameters(self):
        params, jsonparams, errors_warnings = super().parse_parameters()

        ###################################
        # code snippet
        def parse_user_inputs(params, jsonparams, errors_warnings,
                              **valid_meta_params):
            return _parse_user_inputs(
                params,
                jsonparams,
                errors_warnings,
                **self.valid_meta_params
            )
        ####################################

        return parse_user_inputs(params, jsonparams, errors_warnings,
                                 **self.valid_meta_params)