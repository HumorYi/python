#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/11/4 17:29
@Description: 

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/11/4 17:29
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import os, sys, socket

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

from conf.settings import PRINT_COLOR, CHARSET
from util.main import print_color, receive, receive_text, file_write, send_file, transferByBroken, format_storage, \
    input_color

sk = socket.socket()

address = ('127.0.0.1', 8000)

sk.connect(address)


def init(conn):
    """
    初始化
    :param conn: socket 连接对象
    :return:
    """
    print_color('please login', PRINT_COLOR['pink'])

    uid = login(conn)

    while True:
        operate = input_color('please input operate').strip().split('|')
        cmd = operate[0]

        if cmd in OPERATE_TYPES:
            if cmd == 'view':
                view(conn, uid)
            else:
                path = operate[1]
                filename = operate[2]

                if cmd == 'upload':
                    upload(conn, uid, path, filename)
                elif cmd == 'download':
                    download(conn, uid, path, filename)
        elif cmd == 'exit':
            conn.send(cmd.encode(CHARSET))
            print_color('exit success', PRINT_COLOR['red'])
            exit()
        else:
            print_color('operate [%s] no exist', PRINT_COLOR['red'])


def login(conn):
    """
    登录
    :param conn: socket 连接对象
    :return:
    """
    retry_count = 0
    uid = -1

    while uid == -1 and retry_count < 3:
        account = input_color('please input account').strip()
        password = input_color('please input password').strip()

        conn.send(('login|%s|%s' % (account, password)).encode(CHARSET))

        # 先接收信息的总长度
        uid = int(conn.recv(1024).decode(CHARSET))

        if uid == -1:
            retry_count += 1
            print_color('account or password error, please try again!', PRINT_COLOR['red'])
        else:
            print_color('user login use id is [%s] ' % uid, PRINT_COLOR['green'])
            return uid
    else:
        print_color("account [%s] too many login attempts!" % account, PRINT_COLOR['red'])
        exit()


def upload(conn, uid, path, filename):
    """
    上传文件：接收传输的文件，再进行写
    :param conn: socket 对象
    :param uid: 用户 id
    :param path: 用户家目录
    :param filename: 文件名
    :return:
    """
    path = os.path.join(path, filename)

    if os.path.isfile(path):

        file_size = os.stat(path).st_size

        upload_path = 'upload|%d|%s|%d' % (uid, filename, file_size)

        conn.send(upload_path.encode(CHARSET))

        file_send_size, available_space = receive(conn).decode(CHARSET).split('|')

        file_send_size = int(file_send_size)
        available_space = int(available_space)

        if available_space < file_size - file_send_size:
            print_color('you have not enough storage space, the available space is %s' % format_storage(
                available_space))
            return False

        config = {
            'file_send_size': file_send_size
        }

        send_file(conn, path, file_size, config)

        result = receive(conn).decode(CHARSET)

        if result == 'Success':
            print_color(result, PRINT_COLOR['green'])
        else:
            print_color(result, PRINT_COLOR['red'])
    else:
        print_color('%s/%s file no exist' % (path, filename))


def download(conn, uid, path, filename):
    """
    下载文件：读取已存在的文件，再进行传输
    :param conn: socket 对象
    :param uid: 用户 id
    :param path: 用户家目录
    :param filename: 文件名
    :return:
    """
    path = os.path.join(path, filename)

    # 断点续传
    file_receive_size = transferByBroken(path)

    conn.send(('download|%d|%s|%d' % (uid, filename, file_receive_size)).encode(CHARSET))

    file_size = int(conn.recv(1024).decode(CHARSET))

    if file_receive_size != file_size:
        config = {
            'file_receive_size': file_receive_size
        }
        file_write(conn, path, file_size, config)

        result = receive(conn).decode(CHARSET)

        if result == 'Success':
            print_color(result, PRINT_COLOR['green'])
        else:
            print_color(result, PRINT_COLOR['red'])


def view(conn, uid):
    """
    查看目录下所有文件
    :param conn: socket 对象
    :param uid: 用户 id
    :return:
    """
    conn.send(('view|%d' % (uid)).encode(CHARSET))

    result = receive_text(conn).split(',')

    for item in result:
        item.strip()
        print_color(item[1:-1], PRINT_COLOR['blue'])


OPERATE_TYPES = [
    'upload',
    'download',
    'view',
]

init(sk)

# 不允许发送空信息
# while account == '':
#     print('不能发空信息')
#     content = input('>>>:')
#
# # 获取命令和路径
# cmd, path = content.split('|')
#
# path_upload = os.path.join(BASE_DIR, path)
#
# filename = os.path.basename(path_upload)
#
# file_size = os.stat(path_upload).st_size
#
# file_info = 'post|%s|%s' % (filename, file_size)
#
# sk.sendall(file_info.encode(CHARSET))
#
# file = open(path_upload, 'rb')
#
# file_send_size = 0
#
# while file_send_size != file_size:
#     data = file.read(1024)
#     sk.sendall(data)
#     file_send_size += len(data)
#
# file.close()
# print('client upload success')
