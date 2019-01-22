#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Anne-Juul Welsink and Marrit Leenstra
# Date: 21-01-2019

from pyproj import Proj, transform

def reproject(location, oldProjCode, newProjCode):
    """Reproject location point
    
    :location: location tuple (latitude, longitude)
    :oldProjCode: current epsg projection code for specified the location
    :newProjCode: new epsg projection code for specified the location
    return: lat, lng: tuple of latitude and longitude
    """
    inProj = Proj(init= 'epsg:'+ oldProjCode) 
    outProj = Proj(init= 'epsg:' + newProjCode) 
    x,y = transform(inProj, outProj, location.longitude, location.latitude)
    return (x,y)