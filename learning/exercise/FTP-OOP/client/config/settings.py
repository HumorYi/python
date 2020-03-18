#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/12/9 14:23
@Description: 

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/12/9 14:23
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

BIND_HOST = '127.0.0.1'
BIND_PORT = 9992

RECV_SIZE = 1024

CHARSET = 'utf-8'


CODE = {
    'CMD': {
        'code': 1000,
        'msg': 'cmd'
    },
    'CMD_INFO': {
        'code': 1001,
        'msg': 'cmd info'
    },
    'CMD_ACK': {
        'code': 1002,
        'msg': 'cmd ack'
    },
    'POST': {
        'code': 2000,
        'msg': 'post'
    },
    'POST_INFO': {
        'code': 2001,
        'msg': 'post info'
    },
    'POST_ACK': {
        'code': 2002,
        'msg': 'ACK（可以开始上传）'
    },
    'FILE_EXIST': {
        'code': 2003,
        'msg': '文件存在'
    },
    'CONTINUED': {
        'code': 2004,
        'msg': '续传'
    },
    'NO_CONTINUED': {
        'code': 2005,
        'msg': '不续传'
    },
    'GET': {
        'code': 3000,
        'msg': 'get'
    },
    'GET_INFO': {
        'code': 3001,
        'msg': 'get info'
    },
    'GET_ACK': {
        'code': 3002,
        'msg': 'get ack'
    },
    'UNAUTHORIZED': {
        'code': 4001,
        'msg': '未授权'
    },
    'AUTHORIZED_SUCCESS': {
        'code': 4002,
        'msg': '授权成功'
    },
    'AUTHORIZED_FAIL': {
        'code': 4003,
        'msg': '授权失败'
    },
}