########################################################################################
#The dictionary of this analysis
########################################################################################

def version():
    return "0.0.1"

def hw():
    print("\tthe version of hic_down is : {0}. \
The envoriment which you need is python=3.7, configparser, and hicexplorer. \
You can get it from conda by the command of\
python: conda install python=3.7, \
configparser: conda install -c anaconda configparser, \
hicexplorer: conda install hicexplorer -c bioconda -c conda-forge, \
numpy:  conda install -c anaconda numpy, \
cooler: conda install -c bioconda cooler. \
What 's more, you need juicertools which can get from https://github.com/aidenlab/juicer/wiki/Download, \
if you want to analysis loop from pairsfile.\n\
    -h or --help \n\t\
    get this dictionary\n\
    -c or --config \n\t\
    generate config.ini(what 's more, you are best to generate the config.ini in the directory of dlohic result, then you can get a rignt config.ini for running with the commonly used default parameters)\n\
    -t or --tad \n\t\
    analysis the tad from coolfile\n\
    -C or --contact \n\
    contact probability change with genomic distance\n\
    -l or --loop \n\t\
    analysis the loop from pairsfile which is sorted\n\
    -a or --all \n\t\
    both analysis the tad and loop".format(version()))
    return 

if __name__ == "__main__":
    hw()
    print("test is successful")
