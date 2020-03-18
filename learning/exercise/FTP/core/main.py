#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/11/1 17:07
@Description: 入口文件

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/11/1 17:07
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import os, socket, threading

from util.main import print_color, receive
from conf.settings import PRINT_COLOR, CHARSET, UPLOAD_PATH, LOG_TYPES
from core import auth, user

sk = socket.socket()

address = ('127.0.0.1', 8000)

sk.bind(address)

sk.listen(10)


def login(conn, data):
    """
    登录
    :param conn: socket 连接对象
    :param data: client 传输数据
    :return:
    """
    cmd, account, password = data.decode(CHARSET).split('|')

    uid = auth.login(account, password)

    if uid is None:
        uid = -1

    conn.send(str(uid).encode(CHARSET))

    return uid


def operate(conn, data):
    """
    操作行为
    :param conn: socket 连接对象
    :param data: client 传输数据
    :return:
    """
    content = data.decode(CHARSET).split('|')
    cmd = content[0]
    uid = int(content[1])

    login_user = user.getUserById(uid)

    if login_user is None:
        print_color('user no exist', PRINT_COLOR['red'])
        return False

    path = os.path.join(UPLOAD_PATH, login_user['work'])

    if cmd == 'upload':
        filename = content[2]
        file_size = int(content[3])
        return user.upload(conn, path, filename, file_size, login_user)
    elif cmd == 'download':
        filename = content[2]
        file_size = int(content[3])
        return user.download(conn, path, filename, file_size)
    elif cmd == 'view':
        return user.view(conn, path)
    elif cmd == 'exit':
        return False


def interactive():
    """
    与 client 进行交互
    :return:
    """
    while True:
        # 阻塞连接
        conn, addr = sk.accept()
        # 打印连接地址
        print_color('connect address is %s, port is %s' % (addr[0], addr[1]), PRINT_COLOR['green'])

        uid = -1

        while uid == -1:
            uid = login(conn, receive(conn))

        while True:
            data = receive(conn)

            if data.decode(CHARSET) == 'exit':
                break

            if operate(conn, data) == False:
                print_color('operate [%s] fail' % data.decode(CHARSET), PRINT_COLOR['red'])
            else:
                print_color('operate [%s] success' % data.decode(CHARSET), PRINT_COLOR['green'])


threadings = []

for i in range(10):
    threadings.append(threading.Thread(target=interactive))


def run():
    """
    启动 server 端服务
    :return:
    """
    print_color('waiting connect...', PRINT_COLOR['green'])

    for item in threadings:
        item.start()

    for item in threadings:
        item.join()
