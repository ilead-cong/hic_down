##################################################################################
#
##################################################################################
import os
import sys


from bin.help_write import hw
from config_wr.config_write import cfg_wt
from bin.tad_analysis import tad
from bin.loop_analysis import loop
from bin.contact_chrom import contact
from bin.compartment import compartment

cfg_path = os.getcwd()


if len(sys.argv) == 2:
    if ("-h" in sys.argv) or ("--help" in sys.argv):
        hw()
    elif ("-c" in sys.argv) or ("--config" in sys.argv):
        cfg_wt()
    elif ("-C" in sys.argv) or ("--contact" in sys.argv):
        contact(f"{cfg_path}/config_hic-down.ini")
    elif ("-t" in sys.argv) or ("--tad" in sys.argv):
        tad(f"{cfg_path}/config_hic-down.ini")
    elif ("-l" in sys.argv) or ("--loop" in sys.argv):
        loop(f"{cfg_path}/config_hic-down.ini")
    elif ("-b" in sys.argv) or ("--compartment" in sys.argv):
        compartment(f"{cfg_path}/config_hic-down.ini")
    elif ("-a" in sys.argv) or ("--all" in sys.argv):
        tad(f"{cfg_path}/config_hic-down.ini")
        loop(f"{cfg_path}/config_hic-down.ini")
        print("all analysis is over")
    else:
        print("input erro: please read the usage dictionary")
        hw()
else:
    print("input erro: please read the usage dictionary")
    hw()





