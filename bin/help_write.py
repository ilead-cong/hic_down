########################################################################################
# The dictionary of this analysis
########################################################################################

def version():
    return "0.0.1"

def hw():
    print("\tthe version of hic_down is : {0}. \
The envoriment which you need is python=3.7, configparser, hicexplorer，numpy and cooler. \
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
    --FindTADs \n\t\
    Using HiCExplorer hicFindTADs to find TAD\n\
    --DiffTADs \n\
    Using HiCExplorer hicDifferentialTAD to find different TAD\n\
    --FindLoops \n\t\
    Using juicertools hiccups to find loops\n\
    --DiffLoops \n\t\
    Using juicertools hiccupsdiff to find different loops\n\
    --FindCompartment \n\t\
    Using HiCExplorer hicPCA to find compartment\n\
    --CoolBox \n\t\
    generate inputdata for coolbox".format(version()))
    return 

if __name__ == "__main__":
    hw()
    print("test is successful")
