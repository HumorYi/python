#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/11/1 17:14
@Description: 

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/11/1 17:14
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import hashlib, json, time, os

from conf.settings import DATABASE, PRINT_COLOR, CHARSET, LOG_TYPES
from util.main import print_color
from core.logger import logger

access_logger = logger()


def login_required(func):
    "验证用户是否登录"

    def wrapper(*args, **kwargs):
        if args[0]:
            return func(*args, **kwargs)
        else:
            exit("no user")

    return wrapper


def auth_by_file(account, password):
    account_file = "%s/%s" % (DATABASE['path'], DATABASE['name'])

    if os.path.isfile(account_file):
        accounts = json.load(open(account_file))
        md5_password = hashlib.md5()
        md5_password.update(password.encode(CHARSET))
        password = md5_password.hexdigest()

        for item in accounts:
            if account == item['account'] and password == item['password']:
                print_color('auth success', PRINT_COLOR['green'])
                return item['id']

        print_color('auth fail', PRINT_COLOR['red'])
        return None
    else:
        print_color("%s/%s.json does not exist!" % (DATABASE['path'], DATABASE['name']), PRINT_COLOR['red'])
        return None


def auth_by_db(account, password):
    # todo
    pass


def auth(account, password):
    if DATABASE['engine'] == 'file_storage':
        return auth_by_file(account, password)
    elif DATABASE['engine'] == 'mysql':
        return auth_by_db(account, password)


def login(account, password):
    """
    登录
    :param log_obj: 日志对象
    :return:
    """

    uid = auth(account, password)

    if uid is None:
        print_color('login fail', PRINT_COLOR['red'])
    else:
        access_logger.info('user login use id is %d ' % (uid))

    return uid
