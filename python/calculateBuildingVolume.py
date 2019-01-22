#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Anne-Juul Welsink and Marrit Leenstra
# Date: 22-01-2019

import rasterstats as rs
import geopandas as gpd

def calculateBuildingVolume(buildings, tifFile):
    """ Calculate the volume of buildings in area of interest
    
    :buildings: polygon file of buildings
    :tifFile: raster with height data
    return: volume
    """
    
    buildingHeight = rs.zonal_stats(buildings, tifFile, stats = "mean" geojson_out=True)
    buildingHeightGDF = gpd.GeoDataFrame.from_features(buildingHeight)
    
    volume = buildingHeightGDF * buildings.area
    
    return volume
    