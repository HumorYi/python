#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/21 10:40
@Description: 客户端 cmd 命令

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
    sk.send(content.encode('utf8'))

    # 先接收信息的总长度
    data_len = int(sk.recv(1024).decode('utf8'))
    # 告诉 server 端已接收信息长度,可以发送信息了
    sk.send('ok'.encode('utf8'))

    # 再循环接收信息，不断拼接收到的信息，最终组合成一个完整的信息
    data = bytes()
    while len(data) != data_len:
        data += sk.recv(1024)
    # 打印信息
    print('receive data is :\n', data.decode('gbk'))

sk.close()
