#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/21 10:40
@Description: 客户端 数据传输

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/21 10:40
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import socket

sk = socket.socket()

address = ('127.0.0.1', 8000)

sk.connect(address)

while True:
    # 输入信息
    content = input('>>>:')

    # 不允许发送空信息
    while content == '':
        print('不能发空信息')
        content = input('>>>:')

    # 退出
    if content == 'exit': break

    # 发送信息
    sk.send(bytes(content, 'utf8'))

    # 接收信息
    data = str(sk.recv(1024), 'utf8')
    # 打印信息
    print('........', data)

sk.close()
