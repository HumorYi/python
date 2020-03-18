#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/24 14:34
@Description: 服务端 群聊

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/24 14:34
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import socketserver


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        print("server start...")

        while True:
            print("waiting connect...")
            # 阻塞连接
            while True:
                try:
                    # 接收信息
                    client_data = self.request.recv(1024).decode("utf8")
                except Exception:
                    print('exception')
                    break

                print('receive data is: ', client_data)

                if not client_data:
                    break

                self.request.sendall(input(">>>: ").strip().encode("utf8"))

            self.request.close()


if __name__ == '__main__':
    socketserver.ThreadingTCPServer(('127.0.0.1', 8098), MyServer).serve_forever()
