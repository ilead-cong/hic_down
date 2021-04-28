######################################################################
#generate the config.ini file of analysis by Configparser
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


    cfg_annotation("the directory of working and results, juicertools_dir please use absolute path, like PATH/juicer_tools_1.22.01.jar!!!")
    config_g = configparser.ConfigParser()
    config_g.add_section('GLOBAL')
    config_g.set('GLOBAL','results_dir', GLOBAL_path + '/result_down/')
    config_g.set('GLOBAL','juicertools_dir', '/your_path/juicertools.jar')
    config_g.set('GLOBAL','reference', "hg19")
    with open('config_hic-down.ini', 'a') as cfg:
        config_g.write(cfg)

    cfg_annotation("the paratemer of tad analysis, cool file name like simple.cool")
    config_t = configparser.ConfigParser()
    config_t.add_section('tad_analysis')
    config_t.set('tad_analysis','data_dir', GLOBAL_path + '/result/05-matrix/')
    config_t.set('tad_analysis','hicConvertFormat_resolution', '5000')
    config_t.set('tad_analysis','hicFindTADs_minDepth', '15000')
    config_t.set('tad_analysis','hicFindTADs_maxDepth', '40000')
    config_t.set('tad_analysis','hicFindTADs_step', '5000')
    config_t.set('tad_analysis','hicFindTADs_thresholdComparisons', '0.05')
    config_t.set('tad_analysis','hicFindTADs_delta', '0.01')
    config_t.set('tad_analysis','hicFindTADs_correctForMultipleTesting', 'fdr')
    config_t.set('tad_analysis','hicFindTADs_p', '16')
    with open('config_hic-down.ini', 'a') as cfg:
        config_t.write(cfg)

    cfg_annotation("the paratemer of loop analysis, pair type name like simple.pairs.gz")
    config_l = configparser.ConfigParser()
    config_l.add_section('loop_analysis')
    config_l.set('loop_analysis','data_dir', GLOBAL_path + '/result/04-valid/')
    config_l.set('loop_analysis','java_max_memory', '-Xmx10g')
    config_l.set('loop_analysis','hiccups_G_OR_C', '--cpu')
    config_l.set('loop_analysis','hiccups_matrix', '512')
    config_l.set('loop_analysis','hiccups_chromosome', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,X')
    config_l.set('loop_analysis','hiccups_r', '5000,10000,25000')
    config_l.set('loop_analysis','hiccups_k', 'KR')
    config_l.set('loop_analysis','hiccups_f', '0.1,0.1,0.1')
    config_l.set('loop_analysis','hiccups_p', '4,2,1')
    config_l.set('loop_analysis','hiccups_i', '7,5,3')
    config_l.set('loop_analysis','hiccups_t', '0.02,1.5,1.75,2')
    config_l.set('loop_analysis','hiccups_sparsity', '--ignore-sparsity')
    with open('config_hic-down.ini', 'a') as cfg:
        config_l.write(cfg)
    
    cfg_annotation("the paratemer of contact probability")
    config_c = configparser.ConfigParser()
    config_c.add_section('contact_probability')
    config_c.set('contact_probability', 'data_dir', GLOBAL_path + '/result/05-matrix/')
    config_c.set('contact_probability', 'cool_resolution', '5000')
    config_c.set('contact_probability', 'cool_balance', 'no')
    config_c.set('contact_probability', 'chromosome', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,X')
    with open('config_hic-down.ini', 'a') as cfg:
        config_c.write(cfg)

    
    cfg_annotation("the paratemer of AB compartment")
    config_a = configparser.ConfigParser()
    config_a.add_section('AB_compartment')
    config_a.set('AB_compartment', 'data_dir', GLOBAL_path + '/result/05-matrix/')
    config_a.set('AB_compartment', 'cool_resolution', '5000')
    config_a.set('AB_compartment', 'outputMatrix', 'no')
    with open('config_hic-down.ini', 'a') as cfg:
        config_a.write(cfg)



    return print('config generate successfully')


if __name__ == "__main__":
    cfg_wt()
    



