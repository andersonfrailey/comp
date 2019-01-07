import os

from webapp.apps.core.tests.test_views import CoreAbstractViewsTest
from webapp.apps.core.tests.compute import MockCompute
from webapp.apps.projects.taxbrain.models import TaxbrainRun

def read_outputs():
    curr = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(curr, 'outputs.json'), 'r') as f:
        outputs = f.read()
    return outputs

class TaxbrainMockCompute(MockCompute):
    outputs = read_outputs()

class TestTaxbrain(CoreAbstractViewsTest):
    """
    Inherits test cases and functionality from CoreAbstractViewsTest
    """
    app_name = 'taxbrain'
    mockcompute = TaxbrainMockCompute
    RunModel = TaxbrainRun

    def inputs_ok(self):
        inputs = super().inputs_ok()
        upstream_inputs = {}
        return dict(inputs, **upstream_inputs)

    def outputs_ok(self):
        return read_outputs()
