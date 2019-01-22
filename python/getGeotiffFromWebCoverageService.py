#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Anne-Juul Welsink and Marrit Leenstra
# Date: 22-01-2019

from owslib.wcs import WebCoverageService

def getGeotiffFromWebCoverageService(url, version):
    """ Obtain data from WebCoverageService.
    
    :url: url from which to obtain the data
    :version: version of the data to obtain
    return: data from WebCoverageService
    """

    return WebCoverageService(url, version=version)
    