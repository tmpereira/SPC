import numpy as np
import glob
import matplotlib.pyplot as plt

# funçao para plotar o espectro medio
def plot(data):
    plt.figure()
    for i in range(1,data['g'].max()+1):
        sel = data['g']==i
        plt.plot(data['wn'],data['r'][sel,:].mean(0))
    legenda = str(data['arqs'])
    legenda = legenda.split('::')
    plt.legend(legenda)
    plt.xlabel('numero de onda (cm^{-1})')

  
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