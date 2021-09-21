####################################################################################
# HiCExplorer hicPCA to find compartment
####################################################################################


from bin.subp_call import subp_c
from bin.file_name_read import filenameread
from config_wr.config_read import GlobalCfg
from config_wr.config_read import FindcompartmentCfg


def findcompartment(cfg_file):
    print(f"\n####################################################################################################")
    print(f"### findcompartment analysis start")
    glo_cfg = GlobalCfg(cfg_file)
    findcompartment_cfg = FindcompartmentCfg(cfg_file)
    subp_c(f"mkdir -p {glo_cfg.results_dir}05-FindCompartment")
    subp_c(f"mkdir -p {glo_cfg.results_dir}05-FindCompartment/00-pca1")
    findcompartment_dir = f"{glo_cfg.results_dir}05-FindCompartment/"
    file_type = 'mcool'
    list_sample = filenameread(glo_cfg.mcool_dir, file_type)
    for sample in list_sample:
        subp_c(f"mkdir -p {glo_cfg.results_dir}05-FindCompartment/{sample}_pca")
        outPrefix = f"{glo_cfg.results_dir}05-FindCompartment/{sample}_pca/"
        subp_c(f"hicPCA -f {findcompartment_cfg.hP_format} -m {glo_cfg.mcool_dir}{sample}.mcool::resolutions/{findcompartment_cfg.mcool_resolution} -o {outPrefix}{sample}_pca1.{findcompartment_cfg.hP_format} {outPrefix}{sample}_pca2.{findcompartment_cfg.hP_format}")
        subp_c(f"cp {outPrefix}{sample}_pca1.{findcompartment_cfg.hP_format} {glo_cfg.results_dir}05-FindCompartment/00-pca1")
    print(f"### findcompartment analysis successful, please read result at {glo_cfg.results_dir}05-FindCompartment/00-pca1/")
    print(f"####################################################################################################\n")
    return


if __name__ == "__main__":
    findcompartment("/path/dlohic-down/config_test.ini")