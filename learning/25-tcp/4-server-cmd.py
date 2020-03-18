#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/21 10:34
@Description: 服务端 cmd 命令

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/21 10:34
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import socket, subprocess

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
            data = conn.recv(1024)
        except Exception:
            break

        # 打印信息
        print('receive data is :\n', data.decode('utf8'))

        # 信息为空时退出当前连接
        if not data: break

        # 命令处理
        cmd_result = subprocess.Popen(data.decode('utf8'), shell=True, stdout=subprocess.PIPE).stdout.read()

        # 先传输命令处理结果总长度，防止内容过长，客户端一次性接收不了导致数据接收错误
        conn.send(str(len(cmd_result)).encode('utf8'))

        # 粘包现象 当发送数据时，会以很快的速度扫描一下后续还有没有数据也要发送，如果有则把后续数据合并再一起发送
        # 解决方法: 阻塞发送后续数据
        conn.recv(1024)

        # 发送信息
        conn.sendall(cmd_result)
