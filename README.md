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
    --CoolBox  
            generate inputdata for coolbox

# Second you need to genarate a config file
$python hic_down/run.py --config

# Third you need to modify and check the parameters
$vim config config_hic-down.ini

# Finally you can use "python hic_down/run.py --option" to start analysis
$python hic_down/run.py --FindTADs 

```
Visualization
----------------------------------------------------------------------------------------
You can use [CoolBox](https://github.com/GangCaoLab/CoolBox) to visualize data in 06-CoolBox/ like this：
```
import os
import coolbox
from coolbox.api import *
coolbox.__version__

os.chdir("/public/home/hzheng/my_software/result_down")
print(f"Current working directory: {os.path.abspath(os.curdir)}")

with TrackHeight(2):
    frame = Cool(f"06-CoolBox/mcool/M5_sample1.mcool", style='window', color_bar='vertical',depth_ratio=0.5,resolution=25000) + Title("mcool") + TrackHeight(5) + \
        TADCoverage(f"06-CoolBox/TAD/M5_sample1_domains.bed", border_only=True, alpha=1) + \
        Arcs(f"06-CoolBox/Loop/M5_sample1_loops.bedpe", line_width=2) + Inverted() +TrackHeight(2) + \
        InsuScore(f"06-CoolBox/mcool/M5_sample1.mcool", window_size=30)+ TrackHeight(2) + Title("Insulation score") + \
        ABCompartment(f"06-CoolBox/Compartment/M5_sample1_pca1.bigwig" ,num_bins = 5000,color= 'lightcoral',threshold = 0,threshold_color= 'lightskyblue',orientation='inverted') + Title("compartment")
        
frame = XAxis() + frame + XAxis()
frame.properties['width'] = 20
frame.plot("chr1:165000000-170000000") 
```
![coolbox visualization](https://github.com/zhenghu159/hic_down/blob/main/img/coolbox.png)
