#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Anne-Juul Welsink and Marrit Leenstra
# Date: 22-01-2019

import matplotlib.pyplot as plt

def visualizeBuildingVolume(GDF):
    """ Plot volume of buildings
    
    :GDF: geodataframe with buildings (must have column specifying volume)
    """
    f, ax = plt.subplots(1, figsize=(10, 10))
    ax.set_title('Buildings on the WUR campus and their volume')
    GDF.plot(ax=ax,column = 'volume', scheme='fisher_jenks', k=6, 
                  cmap=plt.cm.viridis, linewidth=1, edgecolor='black', legend=True)
    ax.set_facecolor("lightgray") 
    plt.axis('equal') 
    plt.show() 

    