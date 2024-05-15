# importando bibliotecas 
import numpy as np
import glob
import matplotlib.pyplot as plt

## importando os submodulos
import  spc.pca as pca
import  spc.thermo as thermo
import  spc.sh as sh
import  spc.prep as prep
import spc.pls as pls
import spc.age as age


# função que fazer a procura dos melhores lambdas para classificação binaria
def bcodes(data,repeat = 500):
    import scipy.stats as stats
    gg = np.unique(data['g'])
    a = data['r'][data['g']==gg[0],:]
    b = data['r'][data['g']==gg[1],:]
    bcodes = []
    for i in range(a.shape[1]):
        print('analisando o ',data['wn'][i])
        h = 0
        for j in range(repeat):
            na = np.random.permutation(a.shape[0])[:10]
            nb = np.random.permutation(b.shape[0])[:10]
            statistic, pvalue = stats.ranksums(a[na,i],b[nb,i])
            h = h+int(pvalue<0.05)
        bcodes.append(h/j)
    return (data['wn'],100*np.array(bcodes))
