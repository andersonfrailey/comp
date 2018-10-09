from django.db import models
from django.urls import reverse
from ..core.models import CoreInputs, CoreRun


class TaxcalcInput(CoreInputs):
    pass


class TaxcalcOutput(CoreRun):
    inputs = models.OneToOneField(TaxcalcInput, on_delete=models.PROTECT,
                                  related_name='outputs')

    def get_absolute_url(self):
        kwargs = {
            'pk': self.pk
        }
        return reverse('taxcalc_results', kwargs=kwargs)

    def get_absolute_download_url(self):
        kwargs = {
            'pk': self.pk
        }
        return reverse('taxcalc_download', kwargs=kwargs)

    def zip_filename(self):
        return 'taxcalc.zip'
