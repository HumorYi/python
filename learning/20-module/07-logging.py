#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/9/29 9:08
@Description: 日志模块

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/9/29 9:08
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import logging

"""
默认情况下Python的logging模块将日志打印到了标准输出中，且只显示了大于等于WARNING级别的日志，
这说明默认的日志级别设置为WARNING（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET），
默认的日志格式为日志级别：Logger名称：用户输出消息。

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
"""


"""

在logging.basicConfig()函数中可通过具体参数来更改logging模块默认行为，可用参数有
    filename：用指定的文件名创建FiledHandler，这样日志会被存储在指定的文件中。
    filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”(追加)还可指定为“w”(清空重写)。
    format：指定handler使用的日志显示格式。
    datefmt：指定日期时间格式。
    level：设置rootlogger的日志级别
    stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr, sys.stdout或者文件(f=open('test.log','w'))，
            默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。

format参数中可能用到的格式化串：
    %(name)s Logger的名字
    %(levelno)s 数字形式的日志级别
    %(levelname)s 文本形式的日志级别
    %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
    %(filename)s 调用日志输出函数的模块的文件名
    %(module)s 调用日志输出函数的模块名
    %(funcName)s 调用日志输出函数的函数名
    %(lineno)d 调用日志输出函数的语句所在的代码行
    %(created)f 当前时间，用UNIX标准的表示时间的浮点数表示
    %(relativeCreated)d 输出日志信息时的，自Logger创建以来的毫秒数
    %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
    %(thread)d 线程ID。可能没有
    %(threadName)s 线程名。可能没有
    %(process)d 进程ID。可能没有
    %(message)s 用户输出的消息

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %Y-%m-%d %H:%M:%S',
    filename='test.log',
    # filemode='a'
)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')

"""


"""
添加自定义 logger
logger = logging.getLogger()
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('log.log')

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()

formatter = logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%a, %Y-%m-%d %H:%M:%S',
)

fh.setFormatter(formatter)
ch.setFormatter(formatter)

# logger对象可以添加多个fh和ch对象
logger.addHandler(fh)
logger.addHandler(ch)

logger.setLevel(logging.DEBUG)

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')
"""


"""
# filter

logger = logging.getLogger()
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 定义一个filter
filter = logging.Filter('mylogger')
fh.addFilter(filter)
ch.addFilter(filter)

# logger.addFilter(filter)
logger.addHandler(fh)
logger.addHandler(ch)

logger.setLevel(logging.DEBUG)

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')


logger1 = logging.getLogger('mylogger')
logger1.setLevel(logging.DEBUG)

logger2 = logging.getLogger('mylogger')
logger2.setLevel(logging.INFO)

logger1.addHandler(fh)
logger1.addHandler(ch)

logger2.addHandler(fh)
logger2.addHandler(ch)

logger1.debug('logger1 debug message')
logger1.info('logger1 info message')
logger1.warning('logger1 warning message')
logger1.error('logger1 error message')
logger1.critical('logger1 critical message')

logger2.debug('logger2 debug message')
logger2.info('logger2 info message')
logger2.warning('logger2 warning message')
logger2.error('logger2 error message')
logger2.critical('logger2 critical message')

"""


"""
# 应用：信用卡

import os
import time
import logging
from config import settings

def get_logger(card_num, struct_time):
    if struct_time.tm_mday < 23:
        file_name = "%s_%s_%d" %(struct_time.tm_year, struct_time.tm_mon, 22)
    else:
        file_name = "%s_%s_%d" %(struct_time.tm_year, struct_time.tm_mon + 1, 22)

    file_handler = logging.FileHandler(
        os.path.join(settings.USER_DIR_FOLDER, card_num, 'record', file_name),
        encoding='utf-8'
    )

    fmt = logging.Formatter(fmt="%(asctime)s :  %(message)s")
    file_handler.setFormatter(fmt)

    logger = logging.Logger('user_logger', level=logging.INFO)
    logger.addHandler(file_handler)

    return logger
    
"""