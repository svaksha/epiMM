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
__author__ = 'SVAKSHA'
__copyright__ = 'Copyright (c) 2013-Now, SVAKSHA'
__license__ = 'AGPLv3'
__version__ = "14.02.dev"


import glob
import sys
import os, os.path


def epimmPathMap():
    '''
    building paths for epiMM directory
    '''
    full_path = os.path.realpath(__file__)
    dir_EpiMM, prog_file = os.path.split(full_path)
    dir_api = os.path.join(dir_epiMM,"api")
    dir_datum = os.path.abspath(os.path.join(dir_EpiMM, 'datum'))
    # fetches path to the CSV data folder
    dir_who = os.path.abspath(os.path.join((dir_EpiMM), 'EpiMM/who'))   
    # fetches path to the LOG folder that stores error/system logs.
    dir_log = os.path.join(dir_epiMM, "log")
    # fetch path to the scripts folder, which stores mundane scripts.
    dir_scripts = os.path.join(dir_epiMM, "scripts")
    dir_test = os.path.join(dir_epiMM, "test")
    print (dir_api, dir_daemon, dir_datum, dir_who, dir_EpiMM, dir_log, dir_scripts, dir_test)
    return dir_api, dir_daemon, dir_datum, dir_EpiMM, dir_who, dir_log, dir_scripts, dir_test
