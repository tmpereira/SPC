# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 13:46:16 2020

@author: thita
"""
# importando bibliotecas 
import numpy as np
import glob
import matplotlib.pyplot as plt

def pca(r):
     rmean = r - r.mean(0)
     rcov = np.cov(rmean.T)
     a,latent,coeff = np.linalg.svd(rcov)
     latent = latent.reshape(1,-1)
     coeff = coeff.T*np.sqrt(latent)
     scores = r @ (coeff)
     return(scores,coeff,np.sqrt(latent))
 


# funçao para o scatter plot oriundo da analise de PCA
def scores(dados,a,b):
    colmap = [ (0,0,0), (1,0,0),(0,1,0),(0,0,1),(0.41,0.41,0.41),(0,1,1),
        (0.58,0,0.82),(0,0.50,0),(0.98,0.50,0.44),(1,	1,0.87),
        (0.39,0.58,0.92),(0.50,0.50,0),(1,0.89,0.76),(0.96,0.96,0.86),
        (0,1,1)]     
    pcadata = pca(dados['r'])
    a = 3
    b = 2
    latent = np.round(pcadata[2]/pcadata[2].sum(),4)
    leng = str(dados['arqs'])
    leng = leng.split('::')
    for i in range(1,dados['g'].max()+1):
        sel = dados['g'] == i
        plt.scatter(pcadata[0][sel,a+1],pcadata[0][sel,b+1],color=colmap[i])
    plt.legend(leng)
    plt.xlabel('pc_' +str(a+1) + '  ' + str(100*latent[0,a+1]) + '%')
    plt.ylabel('pc_' +str(b+1)+ '  ' + str(100*latent[0,b+1]) + '%')
    plt.title('grafico de scatter plot')
    
# funçao para o loading plot oriundo da analise de PCA
def loading(dados,*a):
    pcadata = pca(dados['r'])
    coeff = pcadata[1]
    leng = []
    for i in a:
        plt.plot(dados['wn'],coeff[:,i])
        leng.append('loading pc' + str(i))
    plt.xlabel('numero de onda (cm^{-1})')
    plt.legend(leng)
    plt.title('grafico do loafing plot')
