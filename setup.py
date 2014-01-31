from __future__ import (absolute_import, division,print_function, unicode_literals)
################################################################################
"""
COPYRIGHT: 2013-Now, SVAKSHA :: https://github.com/svaksha
LICENSE: AGPLv3 License <http://www.gnu.org/licenses/agpl.html>.
All copies must retain this permission notice with the copyright notice.
"""
################################################################################

__author__ = 'SVAKSHA'
__copyright__ = 'Copyright (c) 2013-Now, SVAKSHA'
__license__ = 'AGPLv3'
from distutils.core import setup
#from setuptools import setup, find_packages
import os, sys
import shutil
import warnings
import epiMM

def read():
    with open('README.mediawiki') as f:
        return f.readfile()

PKGNAME='epiMM',
VERSION=epiMM.__version__,
AUTHOR="SVAKSHA",
AUTHOR_EMAIL="svaksha@gmail.com",
LICENSE='AGPLv3',
URL='https://github.com/svaksha/epiMM',
DESCRIPTION=('Mathematical models for Epidemiology'),
LONG_DESCRIPTION=open('README.rst').read()
PACKAGES=['epiMM',
          'epiMM.datum',
          'epiMM.EpiMM',
          'epiMM.test', 
          ],   
PACKAGE_DATA={'epiMM':['LICENSE.mediawiki',
                           'README.mediawiki'],
              'epiMM.datum': ['who/2013-06-24/*.csv',
                                  'who/2013-09-11/*.csv',
                                  'who/2014-01-16/*.csv',
                                  ],
              'epiMM.EpiMM': ['/*.py']
              },
CLASSIFIERS=['Development Status :: 14.01 - Alpha',
             'Intended Audience :: Developers',
             'License :: OSI Approved :: AGPLv3 License',
             'Programming Language :: Python :: 3.3',
             'Topic :: Scientific :: BioStatistics',
             ],


setup(name=PKGNAME,
      version=VERSION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license=LICENSE,
      url=URL,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      classifiers = CLASSIFIERS,
      packages=PACKAGES,
      package_data=PACKAGE_DATA,
      include_package_data = True,
      install_requires = ['Cython==0.19.2', 'matplotlib==1.3.1', 'nose==1.3.0', 
                          'numpy==1.7.1', 'numba==0.11.0', 'pandas==0.12.0', 
                          'blaze=0.4.0', 'patsy==0.2.1', 'pyparsing==2.0.1', 
                          'python-dateutil==2.1', 'pytz==2013b', 
                          'scidb-py==0.2', 'scipy==0.13.0', 'tornado==3.1',
                          ],
      )

