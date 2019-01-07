from django.conf.urls import url

from .views import (TaxbrainInputsView, TaxbrainEditInputsView,
                    TaxbrainOutputsView, TaxbrainOutputsDownloadView)


urlpatterns = [
    url(r'^$', TaxbrainInputsView.as_view(), name='taxbrain'),
    url(r'^(?P<pk>[-\d\w]+)/edit/?$', TaxbrainEditInputsView.as_view(),
        name='taxbrain_edit'),
    url(r'^(?P<pk>[-\d\w]+)/download/?$', TaxbrainOutputsDownloadView.as_view(),
        name='taxbrain_download'),
    url(r'^(?P<pk>[-\d\w]+)/', TaxbrainOutputsView.as_view(),
        name='taxbrain_outputs'),
]
