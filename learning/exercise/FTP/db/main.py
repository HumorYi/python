#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/11/4 10:14
@Description: 入口文件: 模拟用户数据

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/11/4 10:14
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import os, sys, hashlib, json, random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from util.main import generate_random_character
from conf.settings import UPLOAD_PATH, DOWNLOAD_PATH, DATABASE, CHARSET, STORAGE

if __name__ == '__main__':

    accounts = []

    for i in range(1, 11):
        pwd = generate_random_character(8)
        md5_password = hashlib.md5()
        md5_password.update(pwd.encode(CHARSET))
        work = 'work%d' % i
        size = random.randint(1, 10)
        total_space = size * STORAGE['GB']

        accounts.append({
            'id': i,
            'account': generate_random_character(6),
            # todo pwd 密码明文，测试成功后要删除
            'pwd': pwd,
            'password': md5_password.hexdigest(),
            'work': work,
            'total_space': total_space,
            'available_space': total_space,
            'used_space': 0,
            'size': '%dG' % size
        })

        # 创建用户上传家目录
        upload_work_path = os.path.join(UPLOAD_PATH, work)
        download_work_path = os.path.join(DOWNLOAD_PATH, work)

        if not os.path.isdir(upload_work_path):
            os.makedirs(upload_work_path)

        if not os.path.isdir(download_work_path):
            os.makedirs(download_work_path)

    file_accounts = open('%s/%s' % (DATABASE['path'], DATABASE['name']), 'w')

    json.dump(accounts, file_accounts)

    file_accounts.close()
