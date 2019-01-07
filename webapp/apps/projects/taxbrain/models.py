from django.db import models
from django.urls import reverse
from webapp.apps.core.models import CoreInputs, CoreRun
from webapp.apps.core.utils import json_int_key_encode


class TaxbrainInputs(CoreInputs):
    """
    Set inputs fields that are specific to this project's application. Most other
    parameters will be covered in the abstract model class, CoreInputs, but
    some parameters may be specific to this project, such as the
    meta_parameters defined in this project's meta_parameters module.
    """
    start_year = models.IntegerField()
    data_source = models.CharField(max_length=10)
    use_full_sample = models.BooleanField()

    @property
    def deserialized_inputs(self):
        """
        Convert integer keys to int type after they were converted to strings
        during serialization
        """
        return json_int_key_encode(self.upstream_parameters)


class TaxbrainRun(CoreRun):
    """
    Set run or outputs fields that are specific to this project's application.
    Additionally, set the name of the table "dimension." This will be used
    for organizing the outputs. For example, if your project displays data
    on baseball pitchers, this would allow you to toggle a set of tables by
    the pitcher who is being analyzed.
    """
    dimension_name = "Year"

    inputs = models.OneToOneField(TaxbrainInputs, on_delete=models.CASCADE,
                                  related_name='outputs')

    def get_absolute_url(self):
        kwargs = {
            'pk': self.pk
        }
        return reverse('taxbrain_outputs', kwargs=kwargs)

    def get_absolute_edit_url(self):
        kwargs = {
            'pk': self.pk
        }
        return reverse('taxbrain_edit', kwargs=kwargs)

    def get_absolute_download_url(self):
        kwargs = {
            'pk': self.pk
        }
        return reverse('taxbrain_download', kwargs=kwargs)

    def zip_filename(self):
        return 'taxbrain.zip'
