#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Anne-Juul Welsink and Marrit Leenstra
# Date: 22-01-2019

def createBoundingBox(x, y):
    """create bounding box around point location
    
    :x: x-coordinate
    :y: y-coordinate
    return: bounding box (xmin, ymin, xmax, ymax)
    """
    return (x-500, y-500, x+500, y+500)
