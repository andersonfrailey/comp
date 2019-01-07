from webapp.apps.core.forms import InputsForm
from .displayer import TaxbrainDisplayer
from .meta_parameters import taxbrain_meta_parameters
from .models import TaxbrainInputs

print(taxbrain_meta_parameters)

class TaxbrainInputsForm(InputsForm):
    displayer_class = TaxbrainDisplayer
    model = TaxbrainInputs
    meta_parameters = taxbrain_meta_parameters
