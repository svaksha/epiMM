#!/usr/bin/env python
# encoding: utf-8
from __future__ import (absolute_import, division,print_function, unicode_literals)
################################################################################
"""
COPYRIGHT(C) 2013-Now SVAKSHA :: https://github.com/svaksha
LICENSE: AGPLv3 License <http://www.gnu.org/licenses/agpl.html>.
# All copies must retain this permission notice with the copyright notice.
"""
################################################################################
# Created:: Thu Nov 21 11:15:41 2013
## PROGRAM USECASE: Graphing and plotting Epidemiology data with the plotly API.
##==============================================================================
__author__ = 'SVAKSHA'
__copyright__ = 'Copyright (c) 2013-Now, SVAKSHA'
__license__ = 'AGPLv3'
__version__ = "14.02.dev"

# IMPORTS
##------------------------------------------------------------------------------
import plotly as pot
import numpy as np
import os
import sys
from IPython.display import HTML

py = pot.plotly(username='svaksha', key='kxlzomgu1g')

def __init__():
    plotly_key = pot.pot(UN, KEY)

def plotlyUser():
    username='svaksha'
    email='svaksha@gmail.com'
    response = pot.signup(username, email)
    api_key = response['api_key']
    tmp_pw = response['tmp_pw']
    print("api_key:", api_key)
    print("tmp_pw:", tmp_pw)

if __name__ == '__main__':
    # build paths to import modules via pathmap.py
    print('testing')
    import pathmap


