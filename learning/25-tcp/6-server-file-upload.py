#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/21 10:34
@Description: 服务端 文件上传

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/21 10:34
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import socket
import os

sk = socket.socket()

address = ('127.0.0.1', 8000)

sk.bind(address)

sk.listen(3)

print('waiting connect...')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    # 阻塞连接
    conn, addr = sk.accept()
    # 打印连接地址
    print(addr)

    while True:
        # windows 强制中断程序导致数据接收失效异常
        try:
            # 接收信息
            data = conn.recv(1024).decode('utf8')
        except Exception:
            break

        # 打印信息
        print('receive data is :\n', data)

        # 信息为空时退出当前连接
        if not data: break

        cmd, filename, file_size = data.split('|')

        path_upload = os.path.join(BASE_DIR, 'file-upload', filename)

        file_size = int(file_size)

        file = open(path_upload, 'ab')

        file_receive_len = 0

        while file_receive_len != file_size:
            # windows 强制中断程序导致数据接收失效异常
            try:
                # 接收信息
                data_file = conn.recv(1024)
            except Exception:
                break

            file.write(data_file)
            file_receive_len += len(data_file)

        file.close()

        print('server upload success')



