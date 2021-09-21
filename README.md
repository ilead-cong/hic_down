hic_down
===========================================
Purpose
------------------------------------------------------------------------------
some tools for hic downstream analysis:  
(1)loop analysis  
(2)tad analysis  
(3)compartment analysis

Requirements
-------------------------------------------------------------------
The envoriment which you need is python=3.7, configparser, hicexplorer，numpy and cooler. You can get it from conda by the command of  
python: conda install python=3.7  
configparser: conda install -c anaconda configparser  
hicexplorer: conda install hicexplorer -c bioconda -c conda-forge  
numpy:  conda install -c anaconda numpy  
cooler: conda install -c bioconda cooler  
What 's more, you need   
juicertools: which can get from [https://github.com/aidenlab/juicer/wiki/Download,](https://github.com/aidenlab/juicer/wiki/Download,)
 if you want to analysis loop from pairsfile.  
 
Quick Start
----------------------------------------------------------------------------------------

```Shell,default
# First you should get the package from git
$ git clone https://github.com/ilead-cong/hic-down.git

# It is best for you to put the this package and result-dlohic in the same directory
# This will make it easier to edit configuration files
$ls
result-dlohic hic_down

# You can get help documentation by run "-h" or "--help"
$python hic_down/run.py -h
the version of hic_down is : 0.0.1. The envoriment which you need is python=3.7, configparser, hicexplorer，numpy and cooler. 
You can get it from conda by the command ofpython: conda install python=3.7, 
configparser: conda install -c anaconda configparser, 
hicexplorer: conda install hicexplorer -c bioconda -c conda-forge,
numpy:  conda install -c anaconda numpy,  
cooler: conda install -c bioconda cooler.
What 's more, you need juicertools which can get from
https://github.com/aidenlab/juicer/wiki/Download, if you want to analysis loop from pairsfile.
    -h or --help 
            get this dictionary
    -c or --config
            generate config.ini(what 's more, you are best to generate the config.ini in the directory of dlohic result, 
            then you can get a rignt config.ini for running with the commonly used default parameters)
    --FindTADs
            Using HiCExplorer hicFindTADs to find TAD
    --DiffTADs
            Using HiCExplorer hicDifferentialTAD to find different TAD
    --FindLoops
            Using juicertools hiccups to find loops
    --DiffLoops
            Using juicertools hiccupsdiff to find different loops
    --FindCompartment
            Using HiCExplorer hicPCA to find compartment

# Second you need to genarate a config file
$python hic_down/run.py --config

# Third you need to modify and check the parameters
$vim config config_hic-down.ini

# Finally you can use "python hic_down/run.py --option" to start analysis
$python hic_down/run.py --FindTADs 


```

