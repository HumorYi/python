#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/11/4 13:12
@Description: 

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/11/4 13:12
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import logging
from conf.settings import BASE_DIR, LOG_LEVEL, LOG_EXT, LOG_TYPES


def logger(log_type=LOG_TYPES['access']):
    """
    custom logger
    :param log_type: 日志类型
    :return: logger
    :use
        logger.debug('message')
        logger.info('message')
        logger.warn('message')
        logger.error('message')
        logger.critical('message')
    """

    # create logger
    logger = logging.getLogger(log_type)
    logger.setLevel(LOG_LEVEL)

    # create console handle
    ch = logging.StreamHandler()
    ch.setLevel(LOG_LEVEL)

    # create file handle
    log_file = "%s/log/%s" % (BASE_DIR, LOG_TYPES[log_type] + LOG_EXT)
    fh = logging.FileHandler(log_file)
    fh.setLevel(LOG_LEVEL)

    # create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(pathname)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)s - %(message)s')

    # add formatter to ch and fn
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add ch and fn to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger
