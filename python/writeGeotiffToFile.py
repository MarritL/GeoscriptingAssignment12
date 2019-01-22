#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Anne-Juul Welsink and Marrit Leenstra
# Date: 22-01-2019

import rasterio
import os

def writeGeotiffToFile(raster, directory, filename, kwargs):
    """write geotiff to file
    
    :raster: raster to write to geotiff
    :directory: saving directory
    :filename: name of geotiff file
    :kwargs: metadata for geotif
    """
    # create directory if needed
    direc = "./" + directory + "/"
    dirFile = direc + filename + ".tif"
    if not os.path.exists(direc):
        os.makedirs(direc)
    
    # write to specified file
    with rasterio.open(dirFile, 'w', **kwargs) as file:
        file.write(raster.astype(rasterio.float32))