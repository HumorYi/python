#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/6 16:23
@Description: 

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/6 16:23
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""
import os
from core import db_handler
from core import logger
import json
import time


def login_required(func):
    "验证用户是否登录"

    def wrapper(*args, **kwargs):
        if args[0].get('is_authenticated'):
            return func(*args, **kwargs)
        else:
            exit("User is not authenticated.")

    return wrapper


def account_auth_handle(account, password, account_data):
    """
    认证通用接口
    :param accounts: credit accounts number
    :param password: credit card password
    :param account_data: actual account data
    :return: if passed the authentication , return the accounts object, otherwise ,return None
    """
    if account_data['password'] == password:
        exp_time_stamp = time.mktime(time.strptime(account_data['expire_date'], "%Y-%m-%d"))
        if time.time() > exp_time_stamp:
            print("\033[31;1m Account [%s] has expired,please contact the back to get a new card! \033[0m" % account)
        else:  # passed the authentication
            return account_data
    else:
        print("\033[31;1m Account ID or password is incorrect!\033[0m")


def account_auth_db(account, password):
    '''
    accounts auth by db
    :param accounts: credit accounts number
    :param password: credit card password
    '''
    db_api = db_handler.db_handler()
    account_data = db_api("select * from accounts where accounts=%s" % account)
    account_auth_handle(account, password, account_data)


def account_auth_file(account, password):
    '''
    accounts auth by file
    :param accounts: credit accounts number
    :param password: credit card password
    '''
    db_path = db_handler.db_handler()
    account_file = "%s/%s.json" % (db_path, account)

    if os.path.isfile(account_file):
        with open(account_file, 'r') as file:
            account_auth_handle(account, password, json.load(file))
    else:
        print("\033[31;1m Account [%s] does not exist! \033[0m" % account)




def account_login(user_data, log_obj):
    '''
    accounts login func
    :user_data: user info data , only saves in memory
    :return:
    '''
    retry_count = 0

    while user_data['is_authenticated'] is False and retry_count < 3:

        account = input("\033[32;1maccount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()

        auth = account_auth_file(account, password)

        if auth:  # not None means passed the authentication
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            return auth

        retry_count += 1
    else:
        log_obj.error("accounts [%s] too many login attempts" % account)
        exit()
