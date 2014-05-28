#!/usr/bin/env python
#coding=utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
################################################################################
"""
COPYRIGHT(C) 2013-Now SVAKSHA :: https://github.com/svaksha
LICENSE: AGPLv3 License <http://www.gnu.org/licenses/agpl.html>.
All software copies must retain the Copyright, Licence and permission notice.
"""
################################################################################
__author__ = 'SVAKSHA'
__copyright__ = 'Copyright (c) 2013-Now, SVAKSHA'
__license__ = 'AGPLv3'
__version__ = "14.03.dev"


import sys, os, os.path

full_path = os.path.realpath(__file__)
dirpath, prog_file = os.path.split(full_path)
dir_datum = os.path.join(dirpath, '..')
sys.path.append(dir_datum) # Auto PATH for pathmap.py

import pathmap as pm
dir_api, dir_datum, dir_epiMM, dir_who, dir_log, dir_scripts, dir_test = pm.epimmPathMap()


