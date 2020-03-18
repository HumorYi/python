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

import os, pickle

from config import settings
from lib import commons


class Nid:
    def __init__(self, role):
        """
        该对象用于标识唯一ID
        :param role: 角色名称
        """
        if role not in settings.DB_DIR_DICT:
            raise Exception('用户角色定义错误，选项为：%s' % ','.join(settings.DB_DIR_DICT))

        self.role = role
        self.uuid = commons.create_uuid()
        self.db_path = settings.DB_DIR_DICT[role]

    def __str__(self):
        return self.uuid

    def get_obj_by_uuid(self):
        """
        获取当前id对应的对象
        :return:
        """
        for name in os.listdir(self.db_path):
            if name == self.uuid:
                obj = pickle.load(open(os.path.join(self.db_path, self.uuid), 'rb'))
                return obj
