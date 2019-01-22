#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Anne-Juul Welsink and Marrit Leenstra
# Date: 22-01-2019

from owslib.wcs import WebCoverageService
import os

def getGeotiffFromWebCoverageService(url, version, bbox, identifier, frmt, directory, filename):
    """ Obtain data from WebCoverageService.
    
    :url: url from which to obtain the data
    :version: version of the data to obtain
    :bbox: bounding box
    :identifier: user-specified filename
    :format: data format to obtain
    :directory: folder in which file is to be written
    :filename: filename of file to write
    """
    wcs = WebCoverageService(url, version=version)
    
    direc = "./" + directory + "/"
    
    if not os.path.exists(direc):
        os.makedirs(direc)
  
    dirFile = direc + filename + ".tif"
    
    response = wcs.getCoverage(identifier=identifier, bbox=bbox, frmt=frmt,
                           crs='urn:ogc:def:crs:EPSG::28992', resx=0.5, resy=0.5)
    with open(dirFile, 'wb') as file:
        file.write(response.read())
        
    

    
        
        
        
        
        