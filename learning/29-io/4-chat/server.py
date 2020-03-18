#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/12/26 11:32
@Description: io-chat: server

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/12/26 11:32
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import select, socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen(3)

connections = [sk]

RECV_SIZE = 1024
CHARSET = 'utf8'

while True:
    readable, writable, exceptional = select.select(connections, [], [])

    for item in readable:
        if item == sk:
            conn, addr = sk.accept()
            print(conn)
            connections.append(conn)
        else:
            try:
                data = item.recv(RECV_SIZE)
                print('question>>>:%s' % data.decode(CHARSET))
                inp = input('answer>>>:')
                item.sendall(inp.encode(CHARSET))
            except Exception as e:
                connections.remove(item)
                print(e)
