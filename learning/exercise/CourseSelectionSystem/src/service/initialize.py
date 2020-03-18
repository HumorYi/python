#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/12/4 15:54
@Description: 

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/12/4 15:54
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

from lib import commons
from src import models

def initialize(tip):
    print('======%s======' % tip)
    return models.Admin.register()

def main():
    choices = [
        {
            'name': '初始化管理员账户',
            'method': initialize
        }
    ]

    commons.to_choices(choices, True)