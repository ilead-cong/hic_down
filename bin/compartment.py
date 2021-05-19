##############################################################################################
#
##############################################################################################

from bin.subp_call import subp_c
from bin.file_name_read import filenameread
from config_wr.config_read import GlobalCfg
from config_wr.config_read import CompartCfg

def compartment(cfg_file):
    glo_cfg = GlobalCfg(cfg_file)
    subp_c(f"mkdir -p {glo_cfg.results_dir}compartment_result")
    com_dir = f"{glo_cfg.results_dir}compartment_result/"

    com_cfg = CompartCfg(cfg_file)
    file_type = 'cool'
    list_sample = filenameread(com_cfg.data_dir, file_type)
    
    for sample in list_sample:
        print(f"{sample} analysis start")
        subp_c(f"hicConvertFormat -m {com_cfg.data_dir}{sample}.cool -o {com_dir}{sample}.h5 --inputFormat cool --outputFormat h5 -r {com_cfg.cool_resolution}")
        print(f"{sample} convert format successful")
        subp_c(f"hicPCA --matrix {com_dir}{sample}.h5 -o {com_dir}{sample}_pca1.bedgraph {com_dir}{sample}_pca2.bedgraph")
        print(f"{sample} generate pca successful")

        if com_cfg.Omatrix == "no":
            subp_c(f"hicCompartmentalization –obsexp_matrices {com_dir}{sample}.h5 –pca {com_dir}{sample}_pca1.bedgraph -o {com_dir}{sample}_global_signal.png")
        elif com_cfg.Omatrix == "yes":
            subp_c(f"hicCompartmentalization –obsexp_matrices {com_dir}{sample}.h5  --outputMatrix {com_dir}{sample}.npz –pca {com_dir}{sample}_pca1.bedgraph -o {com_dir}{sample}_global_signal.png")
        else:
            print("please check the parameter of outputMatrix in AB_compartment")
        
        print(f"{sample} AB compartment analysis successful")

    print(f"all sample analysis successful, please read result at {com_dir}")

    return

if __name__ == "__main__":
    compartment("./config_hic-down.ini")
        