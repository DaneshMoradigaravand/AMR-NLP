#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 17:42:58 2022

@author: moradigd
"""
class Plot:
    def __init__(self):
        self=None
    
    def plot_2Dimension(self,X,y):
        """
        returns PCA 
        :param keyword: matrix
        :return: PCA fitter
        """
        import random
        from pandas import DataFrame
        from matplotlib import pyplot
        df = DataFrame(dict(x=X[:,0], y=X[:,1], label=y))
        colors = dict([(i,"#{:06x}".format(random.randint(0, 0xFFFFFF))) for i in set(y)])
        fig, ax = pyplot.subplots()
        grouped = df.groupby('label')
        for key, group in grouped:
            group.plot(ax=ax, kind='scatter', x='x', y='y', label=key, color=colors[key])
        pyplot.show()
        
    def plot_grouped_barplot(self, input_table):
        """
        returns grouped barplot
        :param keyword: iinput matrix
        :return: Plot
        """
        import numpy as np
        import random
        import matplotlib.pyplot as plt
        # set width of bar
        barWidth = 1/input_table.shape[0]-0.01
 
        hld=np.arange(input_table.shape[0])
        colors = dict([(i,"#{:06x}".format(random.randint(0, 0xFFFFFF))) for i in range(input_table.shape[0])])
        for i in range(input_table.shape[0]):
            plt.bar(hld, input_table.iloc[:,i].values, color=colors[i], width=barWidth, edgecolor=colors[i], label=input_table.columns.values[i])
            hld = [x + barWidth for x in hld]

        plt.xlabel('group', fontweight='bold')
        plt.xticks([i-barWidth*(input_table.shape[0]/2) for i in hld], input_table.index.values)
        plt.legend()
        plt.show()