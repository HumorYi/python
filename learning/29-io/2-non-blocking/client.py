#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/12/24 16:40
@Description: io-non-blocking: client

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/12/24 16:40
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

RECV_SIZE = 1024
CHARSET = 'utf8'

while True:
    inp = input('>>>:')
    sk.sendall(inp.encode(CHARSET))
    data = sk.recv(RECV_SIZE)
    print(data.decode(CHARSET))

