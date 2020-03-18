#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/12/26 14:19
@Description: 

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/12/26 14:19
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import socket

client = socket.socket()

client.connect(('localhost', 9000))

RECV_SIZE = 1024
CHARSET = 'utf8'

while True:
    cmd = input('>>> ').strip()

    if len(cmd) == 0: continue

    client.send(cmd.encode(CHARSET))

    data = client.recv(RECV_SIZE)

    print(data.decode())

client.close()
