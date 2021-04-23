############################################################################
#
############################################################################

from bin.subp_call import subp_c
from bin.file_name_read import filenameread
from config_wr.config_read import GlobalCfg
from config_wr.config_read import TadCfg



def tad(cfg_file):
    glo_cfg = GlobalCfg(cfg_file)
    subp_c(f"mkdir -p {glo_cfg.results_dir}tad_result")
    tad_dir = f"{glo_cfg.results_dir}tad_result/"

    tad_cfg = TadCfg(cfg_file)
    file_type = 'cool'
    list_sample = filenameread(tad_cfg.data_dir, file_type)
    for sample in list_sample:
        print(f"{sample} analysis start")
        subp_c(f"hicConvertFormat -m {tad_cfg.data_dir}{sample}.cool -o {tad_dir}{sample}.h5 --inputFormat cool --outputFormat h5 -r {tad_cfg.hCF_resolution}")
        print(f"{sample} convert format successful")
        subp_c(f"mkdir -p {tad_dir}{sample}_tad/")
        subp_c(f"hicFindTADs -m {tad_dir}{sample}.h5 --outPrefix {tad_dir}{sample}_tad/{sample}-min{tad_cfg.hFT_minD}_max{tad_cfg.hFT_maxD}_step{tad_cfg.hFT_step}_thres{tad_cfg.hFT_TC}_delta{tad_cfg.hFT_delta}_{tad_cfg.hFT_CFTT} --minDepth {tad_cfg.hFT_minD} --maxDepth {tad_cfg.hFT_maxD} --step {tad_cfg.hFT_step} --thresholdComparisons {tad_cfg.hFT_TC} --delta {tad_cfg.hFT_delta} --correctForMultipleTesting {tad_cfg.hFT_CFTT} -p {tad_cfg.hFT_p}")
        print(f"{sample} tad analysis successful")
    
    print(f"all sample analysis successful, please read result at {tad_dir}")
    return 
    

if __name__ == "__main__":
    tad("/path/dlohic-down/config_test.ini")



