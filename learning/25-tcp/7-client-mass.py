#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/24 14:33
@Description: 客户端 群聊

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/24 14:33
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import socket

ip_port = ('127.0.0.1', 8098)
sk = socket.socket()
sk.connect(ip_port)
print("client start...")

while True:
    inp = input('>>>: ').strip()

    if inp == 'exit':
        break

    sk.sendall(inp.encode("utf8"))

    server_response = sk.recv(1024)
    print(server_response.decode("utf8"))

sk.close()
