# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 13:43:42 2020

@author: thita
"""

# importando bibliotecas 
import numpy as np
import glob
import matplotlib.pyplot as plt


#  funçao para fazer restrição espectral
def cut(data,a,b):
    sel = (data['wn'] > a) & (data['wn'] <b)
    data['wn'] = data['wn'][sel]
    data['r'] = data['r'][:,sel]
    return data


# funçao para savitz-golay
def golay(data,diff,order,win):
    import numpy as np
    from scipy.signal import savgol_coeffs
    from scipy.sparse import spdiags
    import numpy.matlib
    n = int((win-1)/2)
    sgcoeff = savgol_coeffs(win, order, deriv=diff)[:,None]
    sgcoeff = np.matlib.repmat(sgcoeff,1,data['r'].shape[1])
    diags = np.arange(-n,n+1)
    D = spdiags(sgcoeff,diags,data['r'].shape[1],data['r'].shape[1]).toarray()
    D[:,0:n] = 0
    D[:,data['r'].shape[1]-5:data['r'].shape[1]] = 0
    data['r'] = np.dot(data['r'],D)
    return data

      
# normalizaçao em 2 regioes  
def norm2r(data,ini1,fim1,ini2,fim2):
    import numpy as np
    sel = np.logical_and(data['wn'] > int(ini1),data['wn'] < int(fim1))
    r1 = data['r'][:,sel]
    wn1 = data['wn'][sel][:,None]
    media = np.mean(r1,axis=1)
    std = np.std(r1,axis=1)
    r1 = np.divide((r1 - media[:,None]),std[:,None])           
    sel = np.logical_and(data['wn'] > int(ini2),data['wn'] < int(fim2))
    r2 = data['r'][:,sel]
    wn2 = data['wn'][sel][:,None]
    media = np.mean(r2,axis=1)
    std = np.std(r2,axis=1)
    r2 = np.divide((r2 - media[:,None]),std[:,None])
    data['r'] = np.column_stack((r1,r2))
    data['wn'] = np.vstack((wn1,wn2))
    data['wn'] = data['wn'].reshape(-1)
    return data


# fazer normalização vetorial
def norm_vec(data):
    import numpy as np
    r = data['r']
    norma = (r*r)
    norma = np.sqrt(norma.sum(1)).reshape(-1,1)
    rnorm = np.tile(norma,(1,r.shape[1]))
    data['r'] = r/rnorm
    return data


# fazer normalização (SNV)
def snv(data):
    import numpy as np
    spc = data['r']
    media = np.mean(spc,axis=1)
    std = np.std(spc,axis=1)
    data['r'] = np.divide((spc - media[:,None]),std[:,None])
    return data                


## remover offset nas regioes entre a e b  
def offset(data,ini,fim):
    import numpy as np
    import matplotlib.pyplot as plt
    sel = np.logical_and(data['wn'] > int(ini),data['wn'] < int(fim));
    r = data['r'][:,sel];
    minino = np.min(r,axis=1);
    minino = np.reshape(minino,(-1,1));
    minino = np.tile(minino,data['r'].shape[1]);
    data['r'] = data['r']-minino;
    return data



## funçao que faz o agrupamento de dados
def group(data1,*ii):       
    data = data1.copy()
    k = 2
    for i in ii:
        data['r'] = np.vstack((data['r'],i['r']))
        data['g'] =  np.hstack((data['g'],k*i['g']))
        k = k + 1
        data['arqs'] = np.char.add(data['arqs'],'::')
        data['arqs'] = np.char.add(data['arqs'],i['arqs'])
    return data

# funçao que faz sub amostragem nos espectros 

def dsample(dados,k):
    dados['r'] = dados['r'][:,::k]
    dados['wn'] = dados['wn'][::k]
    return dados