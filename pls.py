# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:44:06 2020

@author: thita
"""
from sklearn.cross_decomposition import PLSRegression
import numpy as np
import glob
import matplotlib.pyplot as plt



def loading(dados,ncomp):
    
    g = dados['g']
    r = dados['r']
    wn = dados['wn']
    pls = PLSRegression(n_components=ncomp)
    pls.fit(r,g)
    Y_pred = pls.predict(r)
    loading = pls.x_loadings_
    plt.figure()
    offset = 0;
    leng = []
    for i in range(loading.shape[1]):
        plt.plot(wn,offset+loading[:,i])
        offset = offset + np.abs(loading[:,i].min()) + np.abs(loading[:,i].max())
        leng.append('predictor loading_'+str(i+1))
    plt.legend(leng)
    
    
def scatter(dados,a,b,ncomp):
    colmap = [ (0,0,0), (1,0,0),(0,1,0),(0,0,1),(0.41,0.41,0.41),(0,1,1),
        (0.58,0,0.82),(0,0.50,0),(0.98,0.50,0.44),(1,	1,0.87),
        (0.39,0.58,0.92),(0.50,0.50,0),(1,0.89,0.76),(0.96,0.96,0.86),
        (0,1,1)]    
    g = dados['g']
    r = dados['r']
    wn = dados['wn']
    pls = PLSRegression(n_components=ncomp)
    pls.fit(r,g)
    Y_pred = pls.predict(r)
    scatter = pls.x_scores_
    for i in range(1,g.max()+1):
        sel = g == i
        plt.scatter(scatter[sel,a-1],scatter[sel,b-1],color=colmap[i])
    plt.legend(str(dados['arqs']).split('::'))
    plt.xlabel(str(a) + ' predictor score',Fontsize = 12)
    plt.ylabel(str(b) + ' predictor score',Fontsize = 12)
    plt.title('PLSR scatter plot')


def fit_plt(dados,ncomp):
    from sklearn.cross_decomposition import PLSRegression
    colmap = [ (0,0,0), (1,0,0),(0,1,0),(0,0,1),(0.41,0.41,0.41),(0,1,1),
        (0.58,0,0.82),(0,0.50,0),(0.98,0.50,0.44),(1,	1,0.87),
        (0.39,0.58,0.92),(0.50,0.50,0),(1,0.89,0.76),(0.96,0.96,0.86),
        (0,1,1)]    
    g = dados['g']
    r = dados['r']
    wn = dados['wn']
    pls = PLSRegression(n_components=ncomp)
    pls.fit(r,g)
    Y_pred = pls.predict(r)
    plt.figure() 
    plt.subplot(2,1,1)
    for i in range(1,g.max()+1):
        sel = g == i
        plt.scatter(g[sel],Y_pred[sel],color = colmap[i])
    plt.xlabel( 'Y_class',Fontsize = 12)
    plt.ylabel( 'Y_predited',Fontsize = 12)
    plt.xticks(np.arange(1,g.max() + 1), str(dados['arqs']).split('::'))
    
    plt.subplot(2,1,2)
    for i in range(1,g.max()+1):
        sel = g == i
        plt.hist(Y_pred[sel])
    plt.xlabel( 'Y_class',Fontsize = 12)
    plt.ylabel( 'histograma',Fontsize = 12)
    plt.xticks(np.arange(1,g.max() + 1), str(dados['arqs']).split('::'))
    
    
def coeff(dados,ncomp):
    
    g = dados['g']
    r = dados['r']
    wn = dados['wn']
    pls = PLSRegression(n_components=ncomp)
    pls.fit(r,g)
    Y_pred = pls.predict(r)
    plt.figure()
    zeroline = np.zeros_like(pls.coef_)
    plt.plot(wn,pls.coef_,wn,zeroline)
    plt.xlim((wn[0],wn[-1]))
    plt.xlabel( 'numero de onda ',Fontsize = 12)
    plt.ylabel( 'coeficient value',Fontsize = 12)
    plt.title('coeficientes da regressão do PLS-R')
    
    
def cross(dados,ncomp,kfold):
    from sklearn.model_selection import cross_validate
    from sklearn.cross_decomposition import PLSRegression
    g = dados['g']
    r = dados['r']
    wn = dados['wn']
    rsme =['none']
    for i in range(1,ncomp+1):
        pls = PLSRegression(n_components=i)
        rsme.append(cross_validate(pls, r,g, cv=kfold,return_train_score=True,return_estimator=True,scoring = ('neg_mean_squared_error')))
    return rsme   
    