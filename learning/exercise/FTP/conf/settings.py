#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/11/1 17:08
@Description: 配置

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/11/1 17:08
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import os, logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = {
    'engine': 'file_storage',  # support mysql,postgresql in the future
    'name': 'accounts.json',
    'path': "%s/db" % BASE_DIR
}

LOG_LEVEL = logging.INFO
LOG_EXT = '.log'
LOG_TYPES = {
    'transaction': 'transaction',
    'access': 'access',
}

CHARSET = 'utf8'

RECEIVE_DATA_SIZE = 1024

UPLOAD_PATH = "%s/upload" % BASE_DIR
DOWNLOAD_PATH = "%s/download" % BASE_DIR

PRINT_COLOR = {
    'red': 31,
    'green': 32,
    'yellow': 33,
    'blue': 34,
    'pink': 35,
    'cyan': 36,
    'gray': 37,
}

PRINT_BGC = {
    'red': 41,
    'green': 42,
    'yellow': 44,
    'blue': 44,
    'pink': 45,
    'cyan': 46,
    'gray': 47,
}

STORAGE = {
    'B': 1,
    'KB': 1 * 1024,
    'MB': 1 * 1024 * 1024,
    'GB': 1 * 1024 * 1024 * 1024,
    'TB': 1 * 1024 * 1024 * 1024 * 1024,
    'PB': 1 * 1024 * 1024 * 1024 * 1024 * 1024,
    'EB': 1 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
    'ZB': 1 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
    'YB': 1 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
    'NB': 1 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
    'DB': 1 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
}
