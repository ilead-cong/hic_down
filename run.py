##################################################################################
# All functions
##################################################################################


import os
import sys

from bin.help_write import hw
from config_wr.config_write import cfg_wt
from bin.tad_analysis import findtads
from bin.tad_analysis import difftads
from bin.loop_analysis import findloops
from bin.loop_analysis import diffloops
from bin.compartment_analysis import findcompartment
from bin.quality_control import tadlength

cfg_path = os.getcwd()

if len(sys.argv) ==2:
    if ("-h" in sys.argv) or ("--help" in sys.argv):
        hw()
    elif ("-c" in sys.argv) or ("--config" in sys.argv):
       cfg_wt()
    elif ("--FindTADs" in sys.argv):
        findtads(f"{cfg_path}/config_hic-down.ini")
    elif ("--DiffTADs" in sys.argv):
        difftads(f"{cfg_path}/config_hic-down.ini")
    elif ("--FindLoops" in sys.argv):
        findloops(f"{cfg_path}/config_hic-down.ini")
    elif ("--DiffLoops" in sys.argv):
        diffloops(f"{cfg_path}/config_hic-down.ini")
    elif ("--FindCompartment" in sys.argv):
        findcompartment(f"{cfg_path}/config_hic-down.ini")    
    else:
        print('TO DO')
else:
    print("input error: please read the usage dictionary")
    hw()