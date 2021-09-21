####################################################################################
# Using juicertools hiccups to find loops
# Using juicertools hiccupsdiff to find different loops
####################################################################################


from bin.subp_call import subp_c
from bin.file_name_read import filenameread
from config_wr.config_read import GlobalCfg
from config_wr.config_read import FindloopsCfg
from config_wr.config_read import DiffloopsCfg


def findloops(cfg_file):
    print(f"\n####################################################################################################")
    print(f"### findloops analysis start")
    glo_cfg = GlobalCfg(cfg_file)
    findloops_cfg = FindloopsCfg(cfg_file)
    subp_c(f"mkdir -p {glo_cfg.results_dir}03-FindLoops")
    subp_c(f"mkdir -p {glo_cfg.results_dir}03-FindLoops/hicfile")
    subp_c(f"mkdir -p {glo_cfg.results_dir}03-FindLoops/00-merged_loops")
    findloops_dir = f"{glo_cfg.results_dir}03-FindLoops/"
    file_type = 'pairs.gz'
    list_sample = filenameread(glo_cfg.pairs_dir, file_type)
    for sample in list_sample:
        subp_c(f"echo -e '## pairs format v1.0\n#columns: readID chr1 position1 chr2 position2 strand1 strand2' > {glo_cfg.results_dir}03-FindLoops/hicfile/{sample}-header.pairs")
        subp_c(f"zcat {glo_cfg.pairs_dir}{sample}.pairs.gz >> {glo_cfg.results_dir}03-FindLoops/hicfile/{sample}-header.pairs")
        subp_c(f"gzip {glo_cfg.results_dir}03-FindLoops/hicfile/{sample}-header.pairs")
        subp_c(f"java {findloops_cfg.java_maxM} -jar {glo_cfg.JT_dir} pre {glo_cfg.results_dir}03-FindLoops/hicfile/{sample}-header.pairs.gz {glo_cfg.results_dir}03-FindLoops/hicfile/{sample}.hic --threads {findloops_cfg.threads} {glo_cfg.reference}")
        subp_c(f"mkdir -p {findloops_dir}{sample}_loops")
        subp_c(f"java {findloops_cfg.java_maxM} -jar {glo_cfg.JT_dir} hiccups {findloops_cfg.HC_CorG} -m {findloops_cfg.HC_matrix} -c {findloops_cfg.HC_chrom} -r {findloops_cfg.HC_r} -k {findloops_cfg.HC_k} -f {findloops_cfg.HC_f} -p {findloops_cfg.HC_p} -i {findloops_cfg.HC_i} -t {findloops_cfg.HC_t} {findloops_cfg.HC_sparsity} --threads {findloops_cfg.threads} {glo_cfg.results_dir}03-FindLoops/hicfile/{sample}.hic {findloops_dir}{sample}_loops/")
        subp_c(f"cp {findloops_dir}{sample}_loops/merged_loops.bedpe {glo_cfg.results_dir}03-FindLoops/00-merged_loops/{sample}_merged_loops.bedpe")
    print(f"### findloops analysis successful, please read result at {glo_cfg.results_dir}03-FindLoops/00-merged_loops/")
    print(f"####################################################################################################\n")
    return


def diffloops(cfg_file):
    print(f"\n####################################################################################################")
    print(f"### diffloops analysis start")
    glo_cfg = GlobalCfg(cfg_file)
    findloops_cfg = FindloopsCfg(cfg_file)
    diffloop_cfg = DiffloopsCfg(cfg_file)
    subp_c(f"mkdir -p {glo_cfg.results_dir}04-DiffLoops")
    subp_c(f"mkdir -p {glo_cfg.results_dir}04-DiffLoops/00-DiffLoopList1")
    subp_c(f"mkdir -p {glo_cfg.results_dir}04-DiffLoops/00-DiffLoopList2")
    diffloop_dir = f"{glo_cfg.results_dir}04-DiffLoops/"
    file_type = 'hic'
    list_sample = filenameread(f"{diffloop_cfg.hicfile_dir}", file_type)
    for i in range(0,len(list_sample)-1):
        for j in range(i+1,len(list_sample)):
            subp_c(f"mkdir -p {diffloop_dir}{list_sample[i]}_VS_{list_sample[j]}/")
            outFileNamePrefix = f"{diffloop_dir}{list_sample[i]}_VS_{list_sample[j]}/"
            subp_c(f"java {findloops_cfg.java_maxM} -jar {glo_cfg.JT_dir} hiccupsdiff {findloops_cfg.HC_CorG} -m {findloops_cfg.HC_matrix} -c {findloops_cfg.HC_chrom} -r {findloops_cfg.HC_r} -k {findloops_cfg.HC_k} -f {findloops_cfg.HC_f} -p {findloops_cfg.HC_p} -i {findloops_cfg.HC_i} -t {findloops_cfg.HC_t} {findloops_cfg.HC_sparsity} --threads {findloops_cfg.threads} {diffloop_cfg.hicfile_dir}{list_sample[i]}.hic {diffloop_cfg.hicfile_dir}{list_sample[j]}.hic {diffloop_cfg.mergeloop_dir}{list_sample[i]}_merged_loops.bedpe {diffloop_cfg.mergeloop_dir}{list_sample[j]}_merged_loops.bedpe {outFileNamePrefix}")
            subp_c(f"cp {outFileNamePrefix}differential_loops1.bedpe {glo_cfg.results_dir}04-DiffLoops/00-DiffLoopList1/{list_sample[i]}_VS_{list_sample[j]}_differential_loops1.bedpe")
            subp_c(f"cp {outFileNamePrefix}differential_loops2.bedpe {glo_cfg.results_dir}04-DiffLoops/00-DiffLoopList2/{list_sample[i]}_VS_{list_sample[j]}_differential_loops2.bedpe")
    print(f"### diffloops analysis start successful, please read result at 00-DiffLoopList1/ and 00-DiffLoopList2")
    print(f"####################################################################################################\n")
    return


if __name__ == "__main__":
    findloops("/path/dlohic-down/config_test.ini")
    diffloops("/path/dlohic-down/config_test.ini")