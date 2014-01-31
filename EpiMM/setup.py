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




def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration('epydemitb', parent_package, top_path)
    config.add_subpackage('daemon')
    config.add_subpackage('qa')
    config.add_data_dir('datum')

    config.make_config_py()
    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
