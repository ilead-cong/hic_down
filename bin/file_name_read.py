###################################################################
# 读取特定路径下，特定文件类型的所有文件名，
# 并返回一个不包含文件类型扩展名的文件名的列表
###################################################################

import os

def filenameread(file_path, file_type):
    list_file = []

    for file in os.listdir(file_path):
        if file[(len(file_type)*(-1) -1): ] == ('.' + file_type):
            list_file.append(file[0: (len(file) - len(file_type) -1)])
    
    if list_file:
        print("read sample sucessfully")
        return list_file
    else:
        print("path erro: there is no the {0} type file in {1}, please check file path!".format(file_type, file_path))
        return 


if __name__ == "__main__":
    print(filenameread("/path/dlohic-down", "cool.gz"))

    
