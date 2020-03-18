#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/12/24 16:40
@Description: io-blocking: server

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/12/24 16:40
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen(3)

RECV_SIZE = 1024
CHARSET = 'utf8'

while True:
    conn, addr = sk.accept()

    while True:
        data = conn.recv(RECV_SIZE)
        print(data.decode(CHARSET))
        conn.sendall(data)