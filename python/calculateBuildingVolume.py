#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Anne-Juul Welsink and Marrit Leenstra
# Date: 22-01-2019

import rasterstats as rs
import geopandas as gpd

def calculateBuildingVolume(buildings, tifFile, inputdirectory):
    """ Calculate the volume of buildings in area of interest
    
    :buildings: polygon file of buildings
    :tifFile: raster with height data
    return: volume
    """
    
    filepath = "./" + inputdirectory + "/" + tifFile
    
    buildingHeight = rs.zonal_stats(buildings, filepath, prefix = 'BH_', geojson_out=True)
    buildingsHeightGDF = gpd.GeoDataFrame.from_features(buildingHeight)
    
    volume = buildingsHeightGDF['BH_mean'] * buildings.area
    
    return volume
    