

from django.conf.urls import url

from .views import (TaxcalcView, TaxcalcDetailView, TaxcalcDownloadView)


urlpatterns = [
    url(r'^$', TaxcalcView.as_view(),
        name='taxcalc'),
    url(r'^(?P<pk>[-\d\w]+)/download/?$', TaxcalcDownloadView.as_view(),
        name='taxcalc_download'),
    url(r'^(?P<pk>[-\d\w]+)/', TaxcalcDetailView.as_view(),
        name='taxcalc_results'),
]
