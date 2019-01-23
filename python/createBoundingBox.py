#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Anne-Juul Welsink and Marrit Leenstra
# Date: 22-01-2019

def createBoundingBox(x, y, width, height):
    """create bounding box around point location
    
    :x: x-coordinate
    :y: y-coordinate
    :width: width of the bounding box
    :height: height of the bounding box
    return: bounding box (xmin, ymin, xmax, ymax)
    """
    return (x-(width/2), y-(height/2), x+(width/2), y+(height/2))
