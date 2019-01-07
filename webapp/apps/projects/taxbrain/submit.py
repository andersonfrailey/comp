from webapp.apps.core.submit import Submit, Save
from .forms import TaxbrainInputsForm
from .parser import TaxbrainParser
from .models import TaxbrainRun
from .constants import TAXBRAIN_VERSION, APP_NAME
from .meta_parameters import taxbrain_meta_parameters


class TaxbrainSubmit(Submit):
    """
    High level logic for formatting the inputs, validating them, handling
    errors if they exist, and submitting to the backend workers.
    """
    parser_class = TaxbrainParser
    form_class = TaxbrainInputsForm
    upstream_version = TAXBRAIN_VERSION
    meta_parameters = taxbrain_meta_parameters
    app_name = APP_NAME

    def extend_data(self, data):
        data = super().extend_data(data)
        return data

class TaxbrainSave(Save):
    """
    Creates a Run Model instance for this model run.
    """
    project_name = "TaxBrain"
    runmodel = TaxbrainRun
