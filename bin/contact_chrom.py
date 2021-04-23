###################################################################
#
##################################################################
import math
import numpy as np
import cooler

from bin.subp_call import subp_c
from bin.file_name_read import filenameread
from config_wr.config_read import GlobalCfg
from config_wr.config_read import ContactCfg



def contact(cfg_file):
    glo_cfg = GlobalCfg(cfg_file)
    subp_c(f"mkdir -p {glo_cfg.results_dir}contact_result")
    con_dir = f"{glo_cfg.results_dir}contact_result/"

    con_cfg = ContactCfg(cfg_file)

    file_type = "cool"
    list_sample = filenameread(con_cfg.data_dir, file_type)
    if con_cfg.cool_balance == "yes":
        print("you had balanced the coolfile ")
    elif con_cfg.cool_balance == "no":
        print("start balance coolfile")
        for sample in list_sample:
            subp_c(f"cooler balance {con_cfg.data_dir}{sample}.cool")
        print("all balance over")
    else:
        print("please check the parameter of cool_balance")
      
    list_chrom = con_cfg.chrom.split(",")

    
    for chrom in list_chrom:
        for sample in list_sample:
            print(f"extract the matrix of chr{chrom} in {sample}")
            cooler_s = cooler.Cooler(f"{con_cfg.data_dir}{sample}.cool")
            matrix_s = np.array(cooler_s.matrix(balance = True).fetch(f"chr{chrom}"))
            diagonal_s = matrix_s.shape[0]
            matrix_s[np.isnan(matrix_s)]=0

            print(f"calculate genomic distance and the diagonal mean of contact probability of chr{chrom} in {sample}")
            list_mean = []
            list_site = []
            res = eval(con_cfg.cool_resolution)
            for num in range(0, diagonal_s):
                list_site.append(res)
                list_mean.append(np.mean(np.diagonal(matrix_s, offset=num)))
                res += 5000
            
            print(f"Generate the result file of chr{chrom} in {sample} at {glo_cfg.results_dir}contact_result/")
            f_contact = open(f"{glo_cfg.results_dir}contact_result/{sample}_chr{chrom}_contact.txt", "w")
            f_contact.write(f"contact probability change with genomic distance of chr{chrom} in {sample}" + "\n")
            f_contact.write("genomic distance" + "\t" + "contact probability" + "\n")
            for combination in range(0, len(list_site)):
                f_contact.write(str(list_site[combination]) + "\t" + str(list_mean[combination]) + "\n")
            f_contact.close()


    print("contact analysis is over")



if __name__ == "__main__":
    contact("./config_hic-down.ini")
            

            

                
            




    
