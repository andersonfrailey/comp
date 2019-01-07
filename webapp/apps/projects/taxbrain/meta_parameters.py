from webapp.apps.contrib.taxcalcstyle.meta_parameters import meta_parameters


def meta_parameter_factory(mp):
    # optionally edit parameters attribute on mp
    return mp


taxbrain_meta_parameters = meta_parameter_factory(meta_parameters)