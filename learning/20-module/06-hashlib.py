#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/9/28 11:14
@Description: hashlib 算法模块

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/9/28 11:14
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import hashlib

# m = hashlib.md5()
# # string => unicode => utf8 => binary => hex
# m.update('hello world'.encode('utf8'))
# print(m.hexdigest())
#
# m.update(' bamboo'.encode('utf8'))
# print(m.hexdigest())
#
# m2 = hashlib.md5()
#
# m2.update('hello world bamboo'.encode('utf8'))
# print(m2.hexdigest())
#
# print(m.hexdigest() == m2.hexdigest())

s = hashlib.sha256()
s.update('hello world'.encode('utf8'))
print(s.hexdigest())
