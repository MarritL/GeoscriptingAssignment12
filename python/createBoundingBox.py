#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Anne-Juul Welsink and Marrit Leenstra
# Date: 22-01-2019

def createBoundingBox():
    """create bounding box around point location
    
    :GDF: GeoDataFrame with features 
    return: bbox: bounding box (xmin, ymin, xmax, ymax)
    """
    GDF_polygon = GDF.unary_union.envelope
    bbox = GDF_polygon.bounds
    return bbox
