#--------------------------------
# import modules
#--------------------------------
from anuga.validation_utilities.fabricate import *
from anuga.validation_utilities import run_validation_script
from anuga.validation_utilities import typeset_report

# Setup the python scripts which produce the output for this
# validation test
def build():
    run_validation_script('numerical_carrier_greenspan.py')
    run_validation_script('plot_results_cross_section.py')
    run_validation_script('plot_results_origin_wrt_time.py')
    typeset_report()    


def clean():
    autoclean()

main()
