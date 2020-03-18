#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/6 17:56
@Description: 

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/6 17:56
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import json
from core import db_handler

'''
return accounts balance and other basic info
:param account_id:
:return:
'''


def load_current_balance(account_id):
    db_path = db_handler.db_handler()
    account_file = "%s/%s.json" % (db_path, account_id)

    with open(account_file) as f:
        return json.load(f)

    """
    db_api = db_handler.db_handler()
    data = db_api("select * from accounts where accounts=%s" % account_id)

    return data
    """


'''
after updated transaction or accounts data , dump it back to file db
:param account_data:
:return:
'''


def dump_account(account_data):
    db_path = db_handler.db_handler()
    account_file = "%s/%s.json" % (db_path, account_data['id'])
    with open(account_file, 'w') as f:
        return json.dump(account_data, f)

    # db_api = db_handler.db_handler()
    # data = db_api("update accounts where accounts=%s" % account_data['id'], account_data=account_data)
    # return True
