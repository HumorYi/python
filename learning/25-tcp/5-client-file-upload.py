#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/21 10:40
@Description: 客户端 文件上传

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/21 10:40
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import socket
import os

sk = socket.socket()

address = ('127.0.0.1', 8000)

sk.connect(address)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    # 输入信息
    content = input('>>>:').strip()

    # 不允许发送空信息
    while content == '':
        print('不能发空信息')
        content = input('>>>:')

    # 获取命令和路径
    cmd, path = content.split('|')

    path_upload = os.path.join(BASE_DIR, path)

    filename = os.path.basename(path_upload)

    file_size = os.stat(path_upload).st_size

    file_info = 'post|%s|%s' % (filename, file_size)

    sk.sendall(file_info.encode('utf8'))

    file = open(path_upload, 'rb')

    file_send_len = 0

    while file_send_len != file_size:
        data = file.read(1024)
        sk.sendall(data)
        file_send_len += len(data)

    file.close()
    print('client upload success')
