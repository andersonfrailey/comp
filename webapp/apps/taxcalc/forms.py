from django.forms import Form, fields, widgets



dim_order = ['year', 'MARS', 'itedtype', 'EIC']

def gen_form_from_paramspec(paramspec):
    typemap = {
        'int': fields.IntegerField,
        'float': fields.FloatField,
        'bool': fields.NullBooleanField
    }
    widgetmap = {
        'int': widgets.NumberInput,
        'float': widgets.NumberInput,
        'bool': widgets.CheckboxInput
    }

    classattrs = {}
    for param, data in paramspec.items():
        for val in data['value']:
            s = param
            for d in dim_order:
                r = val.get(d, None)
                if r is not None:
                    s += f"_{r}"
            attrs = {
                'class': 'form-control',
                'placeholder': val['value']
            }
            classattrs[s] = typemap[data['type']](
                widget=widgetmap[data['type']](attrs=attrs)
            )
    form = type('CustomForm', (Form, ), classattrs)
    return form

def paramspec():
    import os
    import json
    CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
    with open(CURRENT_PATH + '/policy_current_law2.json', 'r') as f:
        paramspec = json.loads(f.read())
    return paramspec


TaxcalcForm = gen_form_from_paramspec(paramspec())