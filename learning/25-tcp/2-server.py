#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/21 10:34
@Description: 服务端 数据传输 socket 四字节：一发一收

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/21 10:34
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import socket

sk = socket.socket()

address = ('127.0.0.1', 8000)

sk.bind(address)

sk.listen(3)

print('waiting connect...')

while True:
    # 阻塞连接
    conn, addr = sk.accept()
    # 打印连接地址
    print(addr)

    while True:
        # windows 强制中断程序导致数据接收失效异常
        try:
            # 接收信息
            data = str(conn.recv(1024), 'utf8')
        except Exception:
            break

        # 打印信息
        print('........', data)

        # 信息为空时退出当前连接
        if data == '': break

        # 输入信息
        content = input('>>>:')

        # 不允许发送空信息
        while content == '':
            print('不能发空信息')
            content = input('>>>:')

        # 发送信息
        conn.send(bytes(content, 'utf8'))
