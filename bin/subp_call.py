#########################################################################################
# 运行shell命令的函数
#########################################################################################

import subprocess as subp

def subp_c(cmd):
    print(cmd)
    subp.check_call(cmd, shell=True)
    return


if __name__ == "__main__":
    subp_c("mkdir -p test_dir")


