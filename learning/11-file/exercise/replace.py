#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/8/22 15:06
@Description: 把文件中的bamboo都替换成hello world

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/8/22 15:06
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""


import os

filename = 'replace.txt'
filename_back = 'replace.txt.back'
encoding = 'utf-8'

with open(filename, 'r', encoding=encoding) as file_r, open(filename_back, 'w', encoding=encoding) as file_w:
    # 全部读入内存，在内存中统一替换
    # file_w.write(file_r.read().replace('bamboo', 'hello world'))

    # 一行一行读入内存
    for line in file_r: file_w.write(line.replace('bamboo', 'hello world'))

os.remove(filename)
os.rename(filename_back, filename)