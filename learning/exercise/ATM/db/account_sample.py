#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/6 16:12
@Description: 

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/6 16:12
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import json

account_dic = {
    'id': 1234,
    'name': 'bamboo',
    'password': 'abc',
    'credit': 15000,
    'balance': 15000,
    'enroll_date': '2019-10-06',
    'expire_date': '2021-10-01',
    'pay_day': 22,
    'status': 0 # 0 = normal, 1 = locked, 2 = disabled
}

file_user = open('./accounts/1234.json', 'w')

json.dump(account_dic, file_user)

file_user.close()