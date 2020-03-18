#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/11/5 11:41
@Description: 

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/11/5 11:41
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import json, os, math

from util.main import print_color, receive, send_text, file_write, send_file, transferByBroken, format_storage
from conf.settings import PRINT_COLOR, DATABASE, UPLOAD_PATH, CHARSET, LOG_TYPES
from core.logger import logger

trans_logger = logger(LOG_TYPES['transaction'])


def getUserById(uid):
    """
    通用 用户 id 获取用户信息
    :param uid: 用户 id
    :return: dict
    """
    path = '%s/%s' % (DATABASE['path'], DATABASE['name'])

    if os.path.isfile(path):
        accounts = json.load(open(path))

        for item in accounts:
            if uid == item['id']:
                return item

        return None
    else:
        print_color('file [%s] no exist' % path, PRINT_COLOR['red'])


def upload(conn, path, filename, file_size, user):
    """
    上传文件：接收传输的文件，再进行写
    :param conn: socket 对象
    :param path: 用户家目录
    :param filename: 文件名
    :param file_size: 文件大小
    :param user: 用户信息
    :return: bool
    """
    path = os.path.join(path, filename)

    file_receive_size = transferByBroken(path)

    conn.send(('%d|%d' % (file_receive_size, user['available_space'])).encode(CHARSET))

    # 可用存储空间不足
    if user['available_space'] < file_size - file_receive_size:
        print_color(
            'user id [%d] not enough storage space, the available space is %s' % (
                user['id'], format_storage(user['available_space'])),
            PRINT_COLOR['red'])
        return False

    config = {
        'file_receive_size': file_receive_size
    }

    file_write(conn, path, file_size, config)

    if config['file_receive_size'] == file_size:
        # todo 需要更新 accounts.json 文件
        user['available_space'] -= file_size
        user['used_space'] += file_size

        trans_logger.info('upload [%s] success' % path)

        conn.send('Success'.encode(CHARSET))
        return True
    else:
        trans_logger.error('upload [%s] fail' % path)
        conn.send('Fail'.encode(CHARSET))
        return False


def download(conn, path, filename, file_send_size):
    """
    下载文件：读取已存在的文件，再进行传输
    :param conn: socket 对象
    :param path: 用户家目录
    :param filename: 文件名
    :param file_send_size: 文件发送字节大小
    :return: bool
    """
    path = os.path.join(path, filename)

    if os.path.isfile(path):
        file_size = os.stat(path).st_size

        conn.send(str(file_size).encode(CHARSET))

        config = {
            'file_send_size': file_send_size
        }
        send_file(conn, path, file_size, config)
    else:
        conn.send('file no exist')

    if config['file_send_size'] == file_size:
        trans_logger.info('download [%s] success' % path)
        conn.send('Success'.encode(CHARSET))
        return True
    else:
        trans_logger.error('download [%s] fail' % path)
        conn.send('Fail'.encode(CHARSET))
        return False


def view(conn, path):
    """
    查看目录下所有文件
    :param conn: socket 链接对象
    :param path:
    :return: str | bool
    """
    if os.path.isdir(path):
        return send_text(conn, str(os.listdir(path))[1:-1])
    else:
        print_color('%s is not directory' % path, PRINT_COLOR['red'])
        return False
