#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/9/27 14:41
@Description: 时间模块

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/9/27 14:41
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import time

# 获取 1970.1.1 00:00:00 ~ 当前时间的秒数 => 1569566624.9401472
# 计算天数：time.time() / 60 / 60 / 24 / 365
# print(time.time())

# 暂停时间（秒）
# time.sleep(3)

# 计算 CPU 执行时间 process_time perf_counter
# print(time.process_time())
# print(time.perf_counter())

# 获取 UTC 结构化时间
# time.struct_time(tm_year=2019, tm_mon=9, tm_mday=27, tm_hour=6, tm_min=50, tm_sec=1, tm_wday=4, tm_yday=270, tm_isdst=0)
# print(time.gmtime())

# 获取本地结构化时间
# print(time.localtime())

# 格式结构化时间
# print(help(time.strftime))
"""
print("本地时间: 格式化", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("本地时间: 时区", time.strftime("%z", time.localtime()))
print("本地时间: 星期几：简称", time.strftime("%a", time.localtime()))
print("本地时间: 星期几：全称", time.strftime("%A", time.localtime()))
print("本地时间: 月份：简称", time.strftime("%b", time.localtime()))
print("本地时间: 月份：全称", time.strftime("%B", time.localtime()))
print("本地时间: 语言环境的适当日期和时间表示", time.strftime("%c", time.localtime()))
print("本地时间: 时钟 12 小时制", time.strftime("%I", time.localtime()))
print("本地时间: 上午还是下午", time.strftime("%p", time.localtime()))
"""

# 格式化时间转结构化时间
# print(time.strptime("2019-09-27 15:17:08", "%Y-%m-%d %H:%M:%S"))

# 语言环境的适当日期和时间表示
# print(time.ctime(1234567890))
# print(time.ctime())

# 结构化时间转时间戳
# print(time.mktime(time.localtime()))
