import numpy as np
import glob
import matplotlib.pyplot as plt
# funçao para leitura de um arquivo unico
def read_one_file(arq):
    f = open(arq, 'r')
    matrix = []
    for i in f.readlines():
       ver = i.split(';')
       wn = ver[0].replace(',','.')
       wn = np.array(wn).astype('f4')
       abss = ver[1].replace(',','.')
       abss = np.array(abss).astype('f4')
       matrix.append([wn,abss])
    f.close()
    return np.array(matrix)


# funçao para leitura de varios arquivos dentro de diretorio
def read_dir_files(path,group):
    arqs = np.array(group)
    r = []
    for file in glob.glob(path + "*.csv"):
        ver = read_one_file(file)
        r.append(ver[:,1])      
    data= {}
    data['r']=np.array(r)
    data['wn'] = ver[:,0]
    data['g']=  np.ones(len(r)).astype('i8')
    data['arqs']= arqs
    return data
