#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/12/24 16:40
@Description: io-multiplexing: server

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/12/24 16:40
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import socket, select

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen(3)

sk1 = socket.socket()
sk1.bind(('127.0.0.1', 8081))
sk1.listen(3)

RECV_SIZE = 1024
CHARSET = 'utf8'

while True:
    r, w, e = select.select([sk, sk1], [], [])

    for item in r:
        # conn, addr = item.accept()
        # print('conn', conn)
        # select 属于水平触发，如果不 accept 阻塞，会循环打印
        print('hello')
    print('r', r)
