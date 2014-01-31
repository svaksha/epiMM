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


import sys, os, os.path
import time
import csv
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from find_paths import *

timestamp = '2014-01-16' #time.strftime('%Y-%m-%d')
data_folder = os.path.abspath(os.path.join(dir_who, timestamp))

col_names_MDR_TB = ['country', 'iso2', 'iso3', 'iso_numeric', 'year', 'source_mdr_new',\
          'source_drs_coverage_new', 'source_drs_year_new', 'e_new_mdr_pcnt', \
          'e_new_mdr_pcnt_lo', 'e_new_mdr_pcnt_hi', 'e_new_mdr_num', 'e_new_mdr_num_lo',\
          'e_new_mdr_num_hi', 'source_mdr_ret', 'source_drs_coverage_ret', \
          'source_drs_year_ret', 'e_ret_mdr_pcnt', 'e_ret_mdr_pcnt_lo', \
          'e_ret_mdr_pcnt_hi', 'e_ret_mdr_num', 'e_ret_mdr_num_lo', 'e_ret_mdr_num_hi',\
          'e_mdr_num', 'e_mdr_num_lo', 'e_mdr_num_hi']
          
filename = ('MDR-TB_burden_estimates_' + timestamp +'.csv')  

filecsv = os.path.abspath(os.path.join(dir_who, timestamp, filename ))
print (filecsv)
if not os.path.exists(filecsv):
   print('file present')
# Read in TB_burden_estimates_2013
df = pd.read_csv(open(filecsv), index_col=[0]) #, 'sheet1', header=None)# )
#df1 = df[df[ columns = 6] == "2012"]
#print (df.ix[2010])
#df1 = (df.values)
#print (df[:15])
print (df.describe())
print (df.quantile(), df.var())
print (df.columns)
print (df.values)
print (df['e_new_mdr_num'].hist())
print (df['e_new_mdr_num'].plot[year])



