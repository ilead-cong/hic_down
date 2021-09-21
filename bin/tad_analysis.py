############################################################################
# Using HiCExplorer hicFindTADs to find TAD
# Using HiCExplorer hicDifferentialTAD to find different TAD
############################################################################


from bin.subp_call import subp_c
from bin.file_name_read import filenameread
from config_wr.config_read import GlobalCfg
from config_wr.config_read import FindtadsCfg
from config_wr.config_read import DifftadsCfg


def findtads(cfg_file):
    print(f"\n####################################################################################################")
    print(f"### findtads analysis start")
    glo_cfg = GlobalCfg(cfg_file)
    findtads_cfg = FindtadsCfg(cfg_file)
    subp_c(f"mkdir -p {glo_cfg.results_dir}01-FindTADs")
    subp_c(f"mkdir -p {glo_cfg.results_dir}01-FindTADs/00-AllSamples_domains")
    findtads_dir = f"{glo_cfg.results_dir}01-FindTADs/"
    file_type = 'mcool'
    list_sample = filenameread(glo_cfg.mcool_dir, file_type)
    for sample in list_sample:
        subp_c(f"mkdir -p {findtads_dir}{sample}_tad/")
        subp_c(f"hicFindTADs -m {glo_cfg.mcool_dir}{sample}.mcool::resolutions/{findtads_cfg.mcool_resolution} --outPrefix {findtads_dir}{sample}_tad/{sample} --minDepth {findtads_cfg.hFT_minD} --maxDepth {findtads_cfg.hFT_maxD} --step {findtads_cfg.hFT_step} --thresholdComparisons {findtads_cfg.hFT_TC} --delta {findtads_cfg.hFT_delta} --correctForMultipleTesting {findtads_cfg.hFT_CFTT} -p {findtads_cfg.hFT_p}")
        subp_c(f"cp {findtads_dir}{sample}_tad/{sample}_domains.bed {glo_cfg.results_dir}01-FindTADs/00-AllSamples_domains/")
    print(f"### findtads analysis successful, please read result at {glo_cfg.results_dir}01-FindTADs/00-AllSamples_domains/")
    print(f"####################################################################################################\n")
    return 


def difftads(cfg_file):
    print(f"\n####################################################################################################")
    print(f"### difftads analysis start")
    glo_cfg = GlobalCfg(cfg_file)
    difftads_cfg = DifftadsCfg(cfg_file)
    subp_c(f"mkdir -p {glo_cfg.results_dir}02-DiffTADs")
    subp_c(f"mkdir -p {glo_cfg.results_dir}02-DiffTADs/normalize")
    subp_c(f"mkdir -p {glo_cfg.results_dir}02-DiffTADs/00-rejected")
    difftads_dir = f"{glo_cfg.results_dir}02-DiffTADs/"
    file_type = 'mcool'
    list_sample = filenameread(glo_cfg.mcool_dir, file_type)
    allsample_mcool = ""
    allsample_cool = ""
    for sample in list_sample:
        allsample_mcool += f"{glo_cfg.mcool_dir}{sample}.mcool::resolutions/{difftads_cfg.mcool_resolution}" + " "
        allsample_cool += f"{glo_cfg.results_dir}02-DiffTADs/normalize/{sample}_norm.cool" + " "
    subp_c(f"hicNormalize -m {allsample_mcool} --normalize {difftads_cfg.hN_normalize} -o {allsample_cool}")
    for i in range(0,len(list_sample)-1):
        for j in range(i+1,len(list_sample)):
            subp_c(f"mkdir -p {difftads_dir}{list_sample[i]}_VS_{list_sample[j]}/")
            inputFileNamePrefix = f"{glo_cfg.results_dir}02-DiffTADs/normalize/"
            outFileNamePrefix = f"{difftads_dir}{list_sample[i]}_VS_{list_sample[j]}/{list_sample[i]}_VS_{list_sample[j]}"
            subp_c(f"hicDifferentialTAD --targetMatrix {inputFileNamePrefix}{list_sample[i]}_norm.cool --controlMatrix {inputFileNamePrefix}{list_sample[j]}_norm.cool --tadDomains {difftads_cfg.hDT_tadDomains_dir}{list_sample[i]}_domains.bed --outFileNamePrefix {outFileNamePrefix} --pValue {difftads_cfg.hDT_pValue} --mode {difftads_cfg.hDT_mode} --modeReject {difftads_cfg.hDT_modeReject} --threads {difftads_cfg.hDT_threads}")
            subp_c(f"cp {outFileNamePrefix}_rejected.diff_tad {glo_cfg.results_dir}02-DiffTADs/00-rejected/")
    print(f"### difftads analysis successful, please read result at {glo_cfg.results_dir}02-DiffTADs/00-rejected/")
    print(f"####################################################################################################\n")
    return 

if __name__ == "__main__":
    findtads("/path/dlohic-down/config_test.ini")
    difftads("/path/dlohic-down/config_test.ini")