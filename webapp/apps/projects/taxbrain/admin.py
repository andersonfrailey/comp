# Register your models here.
from django.contrib import admin

# Register your models here.

from .models import TaxbrainInputs, TaxbrainRun

admin.site.register(TaxbrainInputs)
admin.site.register(TaxbrainRun)