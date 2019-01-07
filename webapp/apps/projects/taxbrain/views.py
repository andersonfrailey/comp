from webapp.apps.core.compute import Compute
from webapp.apps.core.views import (InputsView, EditInputsView, OutputsView,
                                    OutputsDownloadView)
from webapp.apps.core.models import Tag, TagOption

from .models import TaxbrainRun
from .displayer import TaxbrainDisplayer
from .submit import TaxbrainSubmit, TaxbrainSave
from .forms import TaxbrainInputsForm
from .meta_parameters import taxbrain_meta_parameters
from .constants import (TAXBRAIN_VERSION, APP_NAME, APP_DESCRIPTION)


compute = Compute()


class TaxbrainInputsMixin:
    form_class = TaxbrainInputsForm
    displayer_class = TaxbrainDisplayer
    submit_class = TaxbrainSubmit
    save_class = TaxbrainSave
    project_name = "TaxBrain"
    app_name = APP_NAME
    app_description = APP_DESCRIPTION
    meta_parameters = taxbrain_meta_parameters
    meta_options = []
    has_errors = False
    upstream_version = TAXBRAIN_VERSION


class TaxbrainInputsView(TaxbrainInputsMixin, InputsView):
    """
    A Django view for serving the default input page, validating the inputs,
    and submitting them to the backend worker nodes.
    """


class TaxbrainEditInputsView(TaxbrainInputsMixin, EditInputsView):
    """
    A Django view for serving serving edited parameters.
    """
    model = TaxbrainRun


class TaxbrainOutputsView(OutputsView):
    """
    A Django view that polls the backend workers to check whether the result
    is ready yet. Once the result is ready, it is stored in the database and
    served from this view.
    """
    model = TaxbrainRun
    result_header = "TaxBrain Results"
    tags = []
    aggr_tags = []

    tags = [
        Tag(key="table_type",
            hidden=False,
            values=[
                TagOption(
                    value="dist",
                    title="Distribution Table",
                    tooltip="Distribution tooltip",
                    children=[
                        Tag(key="law",
                            hidden=True,
                            values=[
                                TagOption(
                                    value="current",
                                    title="Current Law",
                                    active=True,
                                    tooltip="base tooltip"),
                                TagOption(
                                    value="reform",
                                    title="Reform",
                                    tooltip="reform tooltip")])]),
                TagOption(
                    value="diff",
                    title="Difference Table",
                    tooltip="difference tooltip",
                    active=True,
                    children=[
                        Tag(key="tax_type",
                            hidden=False,
                            values=[
                                TagOption(
                                    value="payroll",
                                    title="Payroll Tax",
                                    tooltip="income tooltip"),
                                TagOption(
                                    value="ind_income",
                                    title="Income Tax",
                                    tooltip="income tooltip"),
                                TagOption(
                                    value="combined",
                                    title="Combined",
                                    active=True,
                                    tooltip="")
                            ])])]),
        Tag(key="grouping",
            hidden=False,
            values=[
                TagOption(
                    value="bins",
                    title="Income Bins",
                    active=True,
                    tooltip="income bins tooltip"),
                TagOption(
                    value="deciles",
                    title="Income Deciles",
                    tooltip="income deciles tooltip")
            ])]
    aggr_tags = [
        Tag(key="law",
            hidden=False,
            values=[
                TagOption(
                    value="current",
                    title="Current Law"),
                TagOption(
                    value="reform",
                    title="Reform"),
                TagOption(
                    value="change",
                    title="Change",
                    active=True)
    ])]


class TaxbrainOutputsDownloadView(OutputsDownloadView):
    """
    A Django view for downloading the result of the project run.
    """
    model = TaxbrainRun
