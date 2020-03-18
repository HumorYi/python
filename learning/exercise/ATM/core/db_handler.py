#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/6 17:02
@Description: 

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/6 17:02
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""
import json, time, os
from conf import settings


def file_execute(sql, **kwargs):
    conn_params = settings.DATABASE
    db_path = '%s/%s' % (conn_params['path'], conn_params['name'])

    sql_list = sql.split("where")

    if len(sql_list) > 1:
        column, val = sql_list[1].strip().split("=")

        if column == 'accounts':
            account_file = "%s/%s.json" % (db_path, val)

            if os.path.isfile(account_file):
                with open(account_file, 'w') as file:
                    if sql_list[0].startswith("select"):
                        return json.load(file)
                    elif sql_list[0].startswith("update"):
                        json.dump(kwargs.get("account_data"), file)
                        return True
            else:
                exit("\033[31;1m Account [%s] does not exist! \033[0m" % val)


'''
parse the db file path
:param conn_params: the db connection params set in settings
:return:
'''


def file_db_handle(conn_params):
    return '%s/%s' % (conn_params['path'], conn_params['name'])


'''
connect to db
:param conn_params: the db connection params set in settings
:return:a
'''


def db_handler():
    conn_params = settings.DATABASE
    if conn_params['engine'] == 'file_storage':
        return file_db_handle(conn_params)
    elif conn_params['engine'] == 'mysql':
        pass  # todo
    print('db_handler')
