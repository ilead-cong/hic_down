####################################################################################
# Plot some quality control maps
####################################################################################


from bin.subp_call import subp_c
from config_wr.config_read import GlobalCfg


def tadlength(cfg_file):
    glo_cfg = GlobalCfg(cfg_file)
    subp_c(f"mkdir -p {glo_cfg.results_dir}00-qc/01-TAD_length")
    subp_c(f"Rscript hic_down/script/plot_TAD_length.R")
    return