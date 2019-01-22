#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Anne-Juul Welsink and Marrit Leenstra
# Date: 22-01-2019

import matplotlib.pyplot as plt

def visualizeBuildingVolume(location):
    """Visualize 
    
    """
    locationMap = folium.Map([location.latitude, location.longitude], zoom_start=15)
    locationMap