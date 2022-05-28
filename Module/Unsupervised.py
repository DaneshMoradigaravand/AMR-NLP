#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 17:41:49 2022

@author: moradigd
"""
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics.pairwise import cosine_similarity

class Unsupervised:
    def __init__(self):
        self=None

    def PCA(self,X,n_components_val=2):
        """
        returns PCA 
        :param keyword: matrix
        :return: PCA fitter
        """
        
        self.pca = PCA(n_components=n_components_val)
        return(self)
    
    def fit_PCA(self, X):
        """
        returns fitted PCA 
        :param keyword: matrix
        :return: fitted redcued dimension
        """
        self.pca.fit(X)
        return(self.pca.transform(X))
    
    def TSNE(self,X, n_components_val=2):
        """
        returns fitted tSNE
        :param keyword: matrix
        :return: tSNE fitter
        """
        
        return(TSNE(n_components=n_components_val))

    def fit_TSNE(self,TSNE,X):
        """
        returns fitted tSNE
        :param keyword: matrix
        :return: fitted redcued dimension
        """
        return(TSNE.fit_transform(X))

    def cosine_similarity(self,a,b):
        """
        returns fitted tSNE
        :param keyword: input vectors
        :return: cosine similarity
        """
        
        aa = a.reshape(1,len(a))
        ba = b.reshape(1,len(b))
        return(cosine_similarity(aa, ba)[0][0])

