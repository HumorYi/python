#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/12/4 15:55
@Description: 

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/12/4 15:55
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""
import os
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_BASEDIR = os.path.join(BASEDIR, 'db')
DB_DIR_DICT = {}

for item in os.listdir(DB_BASEDIR):
    DB_DIR_DICT[item] = os.path.join(DB_BASEDIR, item)

