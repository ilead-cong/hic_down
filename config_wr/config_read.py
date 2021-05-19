################################################################################
#
################################################################################

import configparser

def cfg_rd(cfg_file):
    config_read = configparser.ConfigParser()
    config_read.read(cfg_file)
    return config_read

class GlobalCfg():
    '''
    '''
    def __init__(self, cfg_file):
        global_config = cfg_rd(cfg_file)
        self.results_dir = global_config.get('GLOBAL', 'results_dir')
        self.JT_dir = global_config.get('GLOBAL', 'juicertools_dir')
        self.reference = global_config.get('GLOBAL', 'reference')


class TadCfg():
    '''
    '''
    def __init__(self, cfg_file):
        tad_config = cfg_rd(cfg_file)
        self.data_dir = tad_config.get('tad_analysis', 'data_dir')
        self.hCF_resolution = tad_config.get('tad_analysis', 'hicconvertformat_resolution')
        self.hFT_minD = tad_config.get('tad_analysis', 'hicfindtads_mindepth')
        self.hFT_maxD = tad_config.get('tad_analysis', 'hicfindtads_maxdepth')
        self.hFT_step = tad_config.get('tad_analysis', 'hicfindtads_step')
        self.hFT_TC = tad_config.get('tad_analysis', 'hicfindtads_thresholdcomparisons')
        self.hFT_delta = tad_config.get('tad_analysis', 'hicfindtads_delta')
        self.hFT_CFTT = tad_config.get('tad_analysis', 'hicfindtads_correctformultipletesting')
        self.hFT_p = tad_config.get('tad_analysis', 'hicfindtads_p')

class LoopCfg():
    '''
    '''
    def __init__(self, cfg_file):
        loop_config = cfg_rd(cfg_file)
        self.data_dir = loop_config.get('loop_analysis', 'data_dir')
        self.java_maxM = loop_config.get('loop_analysis', 'java_max_memory')
        self.HC_CorG = loop_config.get('loop_analysis', 'hiccups_g_or_c')
        self.HC_chrom = loop_config.get('loop_analysis', 'hiccups_chromosome')
        self.HC_matrix = loop_config.get('loop_analysis', 'hiccups_matrix')
        self.HC_r = loop_config.get('loop_analysis', 'hiccups_r')
        self.HC_k = loop_config.get('loop_analysis', 'hiccups_k')
        self.HC_f = loop_config.get('loop_analysis', 'hiccups_f')
        self.HC_p = loop_config.get('loop_analysis', 'hiccups_p')
        self.HC_i = loop_config.get('loop_analysis', 'hiccups_i')
        self.HC_t = loop_config.get('loop_analysis', 'hiccups_t')
        self.HC_sparsity = loop_config.get('loop_analysis', 'hiccups_sparsity')

class ContactCfg():
    '''
    '''
    def __init__(self, cfg_file):
        con_config = cfg_rd(cfg_file)
        self.data_dir = con_config.get('contact_probability', 'data_dir')
        self.cool_resolution = con_config.get('contact_probability', 'cool_resolution')
        self.chrom = con_config.get('contact_probability', 'chromosome')
        self.cool_balance = con_config.get('contact_probability', 'cool_balance')
    
class CompartCfg():
    '''
    '''
    def __init__(self, cfg_file):
        com_config = cfg_rd(cfg_file)
        self.data_dir = com_config.get('AB_compartment', 'data_dir')
        self.cool_resolution = com_config.get('AB_compartment', 'cool_resolution')
        self.Omatrix = com_config.get('AB_compartment', 'outputMatrix')



if __name__ == "__main__":
    cr = cfg_rd("./config_hic-down.ini")
    print(cr.sections())
    print(type(cr.get('tad_analysis', 'data_dir')))
    tad_parameter = TadCfg("./config_hic-down.ini")
    print(tad_parameter.data_dir)
    con_test = ContactCfg("./config_hic-down.ini")
    #chrom = con_test.chrom
    chrom_list = con_test.chrom.split(",")
    print(chrom_list)
    if con_test.cool_balance == "yes":
        print("ok")

