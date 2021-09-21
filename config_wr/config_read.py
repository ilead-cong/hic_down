################################################################################
# read the config.ini file of analysis by Configparser
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
        self.mcool_dir = global_config.get('GLOBAL', 'mcool_dir')
        self.pairs_dir = global_config.get('GLOBAL', 'pairs.gz_dir')
        self.JT_dir = global_config.get('GLOBAL', 'juicertools_dir')
        self.reference = global_config.get('GLOBAL', 'reference')


class FindtadsCfg():
    '''
    '''
    def __init__(self, cfg_file):
        findtads_config = cfg_rd(cfg_file)
        self.mcool_resolution = findtads_config.get('FindTADs', 'mcool_resolution')
        self.hFT_minD = findtads_config.get('FindTADs', 'hicFindTADs_minDepth')
        self.hFT_maxD = findtads_config.get('FindTADs', 'hicFindTADs_maxDepth')
        self.hFT_step = findtads_config.get('FindTADs', 'hicFindTADs_step')
        self.hFT_TC = findtads_config.get('FindTADs', 'hicFindTADs_thresholdcomparisons')
        self.hFT_delta = findtads_config.get('FindTADs', 'hicFindTADs_delta')
        self.hFT_CFTT = findtads_config.get('FindTADs', 'hicFindTADs_correctForMultipleTesting')
        self.hFT_p = findtads_config.get('FindTADs', 'hicFindTADs_numberOfProcessors')


class DifftadsCfg():
    '''
    '''
    def __init__(self, cfg_file):
        difftads_config = cfg_rd(cfg_file)
        self.mcool_resolution = difftads_config.get('DiffTADs', 'mcool_resolution')
        self.hN_normalize = difftads_config.get('DiffTADs', 'hicNormalize_normalize')
        self.hDT_tadDomains_dir = difftads_config.get('DiffTADs', 'hicDifferentialTAD_tadDomains_dir')
        self.hDT_pValue = difftads_config.get('DiffTADs', 'hicDifferentialTAD_pValue')
        self.hDT_mode = difftads_config.get('DiffTADs', 'hicDifferentialTAD_mode')
        self.hDT_modeReject = difftads_config.get('DiffTADs', 'hicDifferentialTAD_modeReject')
        self.hDT_threads = difftads_config.get('DiffTADs', 'hicDifferentialTAD_threads')


class FindloopsCfg():
    '''
    '''
    def __init__(self, cfg_file):
        findloops_config = cfg_rd(cfg_file)
        self.java_maxM = findloops_config.get('FindLoops', 'java_max_memory')
        self.threads = findloops_config.get('FindLoops', 'threads')
        self.HC_CorG = findloops_config.get('FindLoops', 'hiccups_GPU_OR_CPU')
        self.HC_matrix = findloops_config.get('FindLoops', 'hiccups_matrix')
        self.HC_chrom = findloops_config.get('FindLoops', 'hiccups_chromosome')
        self.HC_r = findloops_config.get('FindLoops', 'hiccups_r')
        self.HC_k = findloops_config.get('FindLoops', 'hiccups_k')
        self.HC_f = findloops_config.get('FindLoops', 'hiccups_f')
        self.HC_p = findloops_config.get('FindLoops', 'hiccups_p')
        self.HC_i = findloops_config.get('FindLoops', 'hiccups_i')
        self.HC_t = findloops_config.get('FindLoops', 'hiccups_t')
        self.HC_sparsity = findloops_config.get('FindLoops', 'hiccups_sparsity')


class DiffloopsCfg():
    '''
    '''
    def __init__(self, cfg_file):
        diffloops_config = cfg_rd(cfg_file)
        self.hicfile_dir = diffloops_config.get('DiffLoops', 'hicfile_dir')
        self.mergeloop_dir = diffloops_config.get('DiffLoops', 'mergeloop_dir')


class FindcompartmentCfg():
    '''
    '''
    def __init__(self, cfg_file):
        findcompartment_config = cfg_rd(cfg_file)
        self.mcool_resolution = findcompartment_config.get('FindCompartment', 'mcool_resolution')
        self.hP_format = findcompartment_config .get('FindCompartment', 'hicPCA_format')



class ContactCfg():
    '''
    '''
    def __init__(self, cfg_file):
        con_config = cfg_rd(cfg_file)
        self.data_dir = con_config.get('contact_probability', 'data_dir')
        self.cool_resolution = con_config.get('contact_probability', 'cool_resolution')
        self.chrom = con_config.get('contact_probability', 'chromosome')
        self.cool_balance = con_config.get('contact_probability', 'cool_balance')
    


if __name__ == "__main__":
    cr = cfg_rd("./config_hic-down.ini")
    print(cr.sections())
    print(type(cr.get('FindTADs', 'data_dir')))
    tad_parameter = TadCfg("./config_hic-down.ini")
    print(tad_parameter.data_dir)
    con_test = ContactCfg("./config_hic-down.ini")
    #chrom = con_test.chrom
    chrom_list = con_test.chrom.split(",")
    print(chrom_list)
    if con_test.cool_balance == "yes":
        print("ok")

