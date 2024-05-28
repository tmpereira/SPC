import numpy as np
import glob
import matplotlib.pyplot as plt

colmap = [ (0,0,0), (1,0,0),(0,1,0),(0,0,1),(0.41,0.41,0.41),(0,1,1),
        (0.58,0,0.82),(0,0.50,0),(0.98,0.50,0.44),(1,	1,0.87),
        (0.39,0.58,0.92),(0.50,0.50,0),(1,0.89,0.76),(0.96,0.96,0.86),
        (0,1,1)] 

# funçao para plotar o espectro medio
def mplot(data):
    for i in range(1,data['g'].max()+1):
        sel = data['g']==i
        plt.plot(data['wn'],data['r'][sel,:].mean(0))
    legenda = str(data['arqs'])
    legenda = legenda.split('::')
    plt.legend(legenda)
    plt.xlabel('numero de onda (cm^{-1})')

  
# funçao para plotar todos os espectros

def aplot(data):
    for i in range(1,data['g'].max()+1):
        sel = data['g']==i
        d = data['r'][sel,:]
        for j in range(d.shape[0]):
            plt.plot(data['wn'],d[j,:],color=colmap[i])
    legenda = str(data['arqs'])
    legenda = legenda.split('::')
    plt.legend(legenda)
    plt.xlabel('numero de onda (cm^{-1})')
    return d


# funçao que faz o calculo de medias 
def area (dados,a,b):
    ver = cut(dados.copy(),a,b)
    r = ver['r']
    area = np.trapz(r)
    gruops =[]
    for i in range(1,1+ver['g'].max()):
        sel = ver['g'] == i
        gruops.append(area[sel])
    plt.boxplot(gruops)
    leng = str(ver['arqs']).split('::')
    plt.xticks(np.arange(1,i+1),leng)
    plt.title('boxplot da area entre '+ str(a) + ' até ' +str(b) + 'cm-1')
    gdict = {}
    j = 0
    for i in gruops:
        gdict[leng[j]] = i
        j = j + 1       
    return gdict


# funçoes auciliares do modulo 

def cut(data,a,b):
    sel = (data['wn'] > a) & (data['wn'] <b)
    data['wn'] = data['wn'][sel]
    data['r'] = data['r'][:,sel]
    return data
