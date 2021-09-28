######################################################################
# generate the config.ini file of analysis by Configparser
#####################################################################


import configparser
import os 

def cfg_wt():
    
    GLOBAL_path = os.getcwd()

    # writeing annotation in config.ini
    def cfg_annotation(string_write):
        with open('config_hic-down.ini', 'a') as cfg:
            cfg.write("#" + " " + string_write + "\n")
        return


    with open('config_hic-down.ini', 'w') as cfg:
        cfg.write("# The version of pipline is 0.0.1\n" + "\n")

    # GLOBAL config
    cfg_annotation("the directory of working and results, juicertools_dir please use absolute path, like PATH/juicer_tools_1.22.01.jar!!!")
    cfg_annotation('#reference must be one of hg18, hg19, hg38, dMel, mm9, mm10, anasPlat1, bTaurus3, canFam3, equCab2, galGal4, Pf3D7, sacCer3, sCerS288c, susScr3, or TAIR10; alternatively, this can be the path of the chrom.sizes file that lists on each line the name and size of the chromosomes')
    config_g = configparser.ConfigParser()
    config_g.add_section('GLOBAL')
    config_g.set('GLOBAL','results_dir', GLOBAL_path + '/result_down/')
    config_g.set('GLOBAL','mcool_dir', GLOBAL_path + '/result/05-matrix/')
    config_g.set('GLOBAL','pairs.gz_dir', GLOBAL_path + '/result/04-valid/')
    config_g.set('GLOBAL','juicertools_dir', GLOBAL_path + '/hic_down/juicer_tools_1.22.01.jar')
    config_g.set('GLOBAL','reference', "hg19")
    with open('config_hic-down.ini', 'a') as cfg:
        config_g.write(cfg)

    # FindTADs config
    cfg_annotation("the paratemer of HiCExplorer hicFindTADs")
    config_findtads = configparser.ConfigParser()
    config_findtads.add_section('FindTADs')
    config_findtads.set('FindTADs','mcool_resolution', '25000')
    config_findtads.set('FindTADs','hicFindTADs_minDepth', '75000')
    config_findtads.set('FindTADs','hicFindTADs_maxDepth', '250000')
    config_findtads.set('FindTADs','hicFindTADs_step', '25000')
    config_findtads.set('FindTADs','hicFindTADs_thresholdComparisons', '0.01')
    config_findtads.set('FindTADs','hicFindTADs_delta', '0.01')
    config_findtads.set('FindTADs','hicFindTADs_correctForMultipleTesting', 'fdr')
    config_findtads.set('FindTADs','hicFindTADs_numberOfProcessors', '10')
    with open('config_hic-down.ini', 'a') as cfg:
        config_findtads.write(cfg)


    # DiffTADs config
    cfg_annotation("the paratemer of HiCExplorer hicNormalize and hicDifferentialTAD")
    config_difftads = configparser.ConfigParser()
    config_difftads.add_section('DiffTADs')
    config_difftads.set('DiffTADs','mcool_resolution', '25000')
    config_difftads.set('DiffTADs','hicNormalize_normalize', 'smallest')
    config_difftads.set('DiffTADs','hicDifferentialTAD_tadDomains_dir', GLOBAL_path + '/result_down/01-FindTADs/00-AllSamples_domains/')
    config_difftads.set('DiffTADs','hicDifferentialTAD_pValue', '0.05')
    config_difftads.set('DiffTADs','hicDifferentialTAD_mode', 'all')
    config_difftads.set('DiffTADs','hicDifferentialTAD_modeReject', 'one')
    config_difftads.set('DiffTADs','hicDifferentialTAD_threads', '10')
    with open('config_hic-down.ini', 'a') as cfg:
        config_difftads.write(cfg)


    # FindLoops config
    cfg_annotation("the paratemer of juicertools pre and hiccups")
    config_findloops = configparser.ConfigParser()
    config_findloops.add_section('FindLoops')
    config_findloops.set('FindLoops','java_max_memory', '-Xmx10g')
    config_findloops.set('FindLoops','threads', '10')
    config_findloops.set('FindLoops','hiccups_GPU_OR_CPU', '--cpu')
    config_findloops.set('FindLoops','hiccups_matrix', '512')
    config_findloops.set('FindLoops','hiccups_chromosome', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,X')
    config_findloops.set('FindLoops','hiccups_r', '5000,10000,25000')
    config_findloops.set('FindLoops','hiccups_k', 'KR')
    config_findloops.set('FindLoops','hiccups_f', '0.1,0.1,0.1')
    config_findloops.set('FindLoops','hiccups_p', '4,2,1')
    config_findloops.set('FindLoops','hiccups_i', '7,5,3')
    config_findloops.set('FindLoops','hiccups_t', '0.02,1.5,1.75,2')
    config_findloops.set('FindLoops','hiccups_sparsity', '--ignore-sparsity')
    with open('config_hic-down.ini', 'a') as cfg:
        config_findloops.write(cfg)
    

    # DiffLoops config
    cfg_annotation("the paratemer of juicertools hiccupsdiff")
    config_diffloops = configparser.ConfigParser()
    config_diffloops.add_section('DiffLoops')
    config_diffloops.set('DiffLoops','hicfile_dir', GLOBAL_path + '/result_down/03-FindLoops/hicfile/')
    config_diffloops.set('DiffLoops','mergeloop_dir', GLOBAL_path + '/result_down/03-FindLoops/00-merged_loops/')
    with open('config_hic-down.ini', 'a') as cfg:
        config_diffloops.write(cfg)

    # FindCompartment config
    cfg_annotation("the paratemer of HiCExplorer hicPCA")
    config_findcompartment = configparser.ConfigParser()
    config_findcompartment.add_section('FindCompartment')
    config_findcompartment.set('FindCompartment', 'mcool_resolution','100000')
    config_findcompartment.set('FindCompartment', 'hicPCA_format', 'bigwig')
    with open('config_hic-down.ini', 'a') as cfg:
        config_findcompartment.write(cfg)

    cfg_annotation("the paratemer of contact probability")
    config_c = configparser.ConfigParser()
    config_c.add_section('contact_probability')
    config_c.set('contact_probability', 'data_dir', GLOBAL_path + '/result/05-matrix/')
    config_c.set('contact_probability', 'cool_resolution', '5000')
    config_c.set('contact_probability', 'cool_balance', 'no')
    config_c.set('contact_probability', 'chromosome', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,X')
    with open('config_hic-down.ini', 'a') as cfg:
        config_c.write(cfg)

    




    return print('config generate successfully')


if __name__ == "__main__":
    cfg_wt()
    



