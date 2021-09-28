####################################################################################
# generate inputdata for coolbox 
####################################################################################


from bin.subp_call import subp_c
from bin.file_name_read import filenameread
from config_wr.config_read import GlobalCfg
from config_wr.config_read import FindcompartmentCfg


def coolbox(cfg_file):
    print(f"\n####################################################################################################")
    print(f"### generate inputdata for coolbox start")
    glo_cfg = GlobalCfg(cfg_file)
    findcompartment_cfg = FindcompartmentCfg(cfg_file)
    subp_c(f"mkdir -p {glo_cfg.results_dir}06-CoolBox")
    subp_c(f"mkdir -p {glo_cfg.results_dir}06-CoolBox/mcool")
    subp_c(f"mkdir -p {glo_cfg.results_dir}06-CoolBox/TAD")
    subp_c(f"mkdir -p {glo_cfg.results_dir}06-CoolBox/Loop")
    subp_c(f"mkdir -p {glo_cfg.results_dir}06-CoolBox/Compartment")
    file_type = 'mcool'
    list_sample = filenameread(glo_cfg.mcool_dir, file_type)
    for sample in list_sample:
        subp_c(f"cp {glo_cfg.mcool_dir}{sample}.mcool {glo_cfg.results_dir}06-CoolBox/mcool")
        subp_c(f"cp {glo_cfg.results_dir}01-FindTADs/00-AllSamples_domains/{sample}_domains.bed {glo_cfg.results_dir}06-CoolBox/TAD")
        subp_c(f"cp {glo_cfg.results_dir}05-FindCompartment/00-pca1/{sample}_pca1.{findcompartment_cfg.hP_format} {glo_cfg.results_dir}06-CoolBox/Compartment")
        subp_c(f"cp {glo_cfg.results_dir}03-FindLoops/00-merged_loops/{sample}_merged_loops.bedpe {glo_cfg.results_dir}06-CoolBox/Loop")
        # loop file need adjust format
        with open(f'{glo_cfg.results_dir}06-CoolBox/Loop/{sample}_merged_loops.bedpe', 'r') as f:
            lines = f.readlines()
            lines = lines[2:]
        with open(f'{glo_cfg.results_dir}06-CoolBox/Loop/{sample}_loops.bedpe', 'a') as f:
            for line in lines:
                newline = line.split()
                newline = newline[0] + '\t' + newline[1] + '\t' + newline[2] + '\t' + newline[3] + '\t' + newline[4] + '\t' + newline[5] + '\t' + newline[6] + '\t' + newline[20] + '\n'
                f.write(newline)
        subp_c(f"rm {glo_cfg.results_dir}06-CoolBox/Loop/{sample}_merged_loops.bedpe")
    print(f"### generate inputdata for coolbox successful, please read result at {glo_cfg.results_dir}06-CoolBox/")
    print(f"####################################################################################################\n")
    return
            
