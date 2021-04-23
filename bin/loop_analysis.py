####################################################################################
#使用hiccups寻找loop
#pairs文件格式转换和hic文件分析loop
####################################################################################
from bin.subp_call import subp_c
from bin.file_name_read import filenameread
from config_wr.config_read import GlobalCfg
from config_wr.config_read import LoopCfg



def loop(cfg_file):
    glo_cfg = GlobalCfg(cfg_file)
    subp_c(f"mkdir -p {glo_cfg.results_dir}loop_result")
    loop_dir = f"{glo_cfg.results_dir}loop_result/"

    loop_cfg = LoopCfg(cfg_file)
    file_type = 'pairs.gz'
    list_sample = filenameread(loop_cfg.data_dir, file_type)
    for sample in list_sample:
        print(f"{sample} analysis start")
        subp_c(f"echo -e '## pairs format v1.0\\n#columns: readID chr1 position1 chr2 position2 strand1 strand2' > {loop_dir}{sample}-header.pairs")
        subp_c(f"zcat {loop_cfg.data_dir}{sample}.pairs.gz >> {loop_dir}{sample}-header.pairs")
        subp_c(f"gzip {loop_dir}{sample}-header.pairs")
        subp_c(f"java {loop_cfg.java_maxM} -jar {glo_cfg.JT_dir} pre {loop_dir}{sample}-header.pairs.gz {loop_dir}{sample}.hic {glo_cfg.reference}")
        print(f"{sample} convert format successful")
        subp_c(f"java -jar {glo_cfg.JT_dir} hiccups {loop_cfg.HC_CorG} --restrict -m {loop_cfg.HC_matrix} -c {loop_cfg.HC_chrom} -r {loop_cfg.HC_r} -k {loop_cfg.HC_k} -f {loop_cfg.HC_f} -p {loop_cfg.HC_p} -i {loop_cfg.HC_i} -t {loop_cfg.HC_t} {loop_cfg.HC_sparsity} {loop_dir}{sample}.hic {loop_dir}{sample}_hiccups_loops")
        print(f"{sample} loop analysis successful")
    
    print(f"all sample analysis successful, please read result at {loop_dir}")
    return 
    
