from webapp.apps.core.displayer import Displayer
from webapp.apps.contrib.taxcalcstyle.param import TaxcalcStyleParam

from taxcalc.tbi import get_defaults

class TaxbrainDisplayer(Displayer):
    param_class = TaxcalcStyleParam

    def package_defaults(self):
        """
        Get the package defaults from the upstream project. Currently, this is
        done by importing the project and calling a function or series of
        functions to load the project's inputs data. In the future, this will
        be done over the distributed REST API.
        """
        ####################################
        # code snippet
        def package_defaults(**meta_parameters):
            return get_defaults(**meta_parameters)
        ####################################
        print(self.meta_parameters)
        return package_defaults(**self.meta_parameters)