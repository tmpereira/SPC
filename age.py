import numpy as np
import glob
import matplotlib.pyplot as plt

# funçao para leitura de um arquivo unico
def read_one_file(arq):
    ver = np.loadtxt(arq)
    wn = ver[:,0]
    abss = ver[:,1]
    return np.vstack((wn,abss)).T[::-1,:]

def read_dir_files(path,group):
    arqs = np.array(group)
    r = []
    for file in glob.glob(path + "*.dpt"):
        ver = read_one_file(file)
        r.append(ver[:,1])      
    data= {}
    data['r']=np.array(r)
    data['wn'] = ver[:,0]
    data['g']=  np.ones(len(r)).astype('i8')
    data['arqs']= arqs
    return data