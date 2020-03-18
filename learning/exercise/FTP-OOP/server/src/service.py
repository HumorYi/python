#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/12/9 14:22
@Description: 

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/12/9 14:22
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import socketserver, json, os, re, subprocess
from config import settings


class Action:
    def __init__(self, conn):
        self.conn = conn
        self.is_login = False
        self.username = None
        self.home = None
        self.current_dir = None

    def login(self, origin):
        login_dict = json.loads(origin)
        if login_dict['username'] == 'bamboo' and login_dict['password'] == '123':
            self.is_login = True
            self.username = login_dict['username']
            self.home = os.path.join(settings.USER_HOME, self.username)
            self.current_dir = self.home

            if os.path.isdir(self.home) is False:
                os.mkdir(self.home)

            self.conn.sendall(json.dumps(settings.CODE['AUTHORIZED_SUCCESS']).encode(settings.CHARSET))
        else:
            self.conn.sendall(json.dumps(settings.CODE['AUTHORIZED_FAIL']).encode(settings.CHARSET))

    def cmd(self, origin):
        command_list = origin.split('|')[1:]
        cmd = command_list[0]

        if cmd == 'ls' or cmd == 'dir':
            if len(command_list) == 1:
                if self.current_dir:
                    command_list.append(self.current_dir)
                else:
                    command_list.append(self.home)
            else:
                if self.current_dir:
                    path_abs = os.path.join(self.current_dir, command_list[1])
                else:
                    path_abs = os.path.join(self.home, command_list[1])

                command_list[1] = path_abs

        elif cmd == 'cd':
            if len(command_list) == 1:
                command_list.append(self.home)
            else:
                if self.current_dir:
                    path_abs = os.path.join(self.current_dir, command_list[1])
                else:
                    path_abs = os.path.join(self.home, command_list[1])

                command_list[1] = path_abs
                self.current_dir = path_abs

        try:
            result_bytes = str(subprocess.check_output(' '.join(command_list), shell=True), encoding='gbk').encode(
                settings.CHARSET)
        except Exception as e:
            result_bytes = 'error cmd'.encode(settings.CHARSET)

        self.conn.sendall(("info|%d" % len(result_bytes)).encode(settings.CHARSET))
        ack = self.conn.recv(1024)
        self.conn.sendall(result_bytes)

    def post(self, origin):
        func, file_byte_size, file_name, file_md5, target_path = origin.split('|', 4)
        target_abs_md5_path = os.path.join(self.home, target_path)
        has_received = 0
        file_byte_size = int(file_byte_size)

        if os.path.exists(target_abs_md5_path):
            self.conn.sendall(json.dumps(settings.CODE['FILE_EXIST']).encode(settings.CHARSET))
            is_continue = self.conn.recv(settings.RECV_SIZE).decode(settings.CHARSET)
            is_continue = int(is_continue)

            if is_continue == settings.CODE['CONTINUED']['code']:
                has_file_size = os.stat(target_abs_md5_path).st_size
                self.conn.sendall(str(has_file_size).encode(settings.CHARSET))
                has_received += has_file_size
                file = open(target_abs_md5_path, 'ab')
            else:
                file = open(target_abs_md5_path, 'wb')
        else:
            self.conn.sendall(json.dumps(settings.CODE['POST_ACK']).encode(settings.CHARSET))
            file = open(target_abs_md5_path, 'wb')

        while file_byte_size > has_received:
            data = self.conn.recv(settings.RECV_SIZE)
            file.write(data)
            has_received += len(data)

        file.close()

    def get(self, origin):
        pass

    def exit(self, origin):
        self.conn.close()


class MultiServerHandler(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.sendall("欢迎使用FTP".encode(settings.CHARSET))

        action = Action(conn)

        while True:
            client_bytes = conn.recv(settings.RECV_SIZE)

            if not client_bytes:
                break

            client_str = client_bytes.decode(settings.CHARSET)

            if action.is_login is False:
                action.login(client_str)
                continue

            operate = client_str.split('|', 1)

            if len(operate) > 0:
                func = getattr(action, operate[0])
                func(client_str)
            else:
                conn.sendall('输入格式错误'.encode(settings.CHARSET))

        conn.close()


class MultiServer:
    def __init__(self):
        server = socketserver.ThreadingTCPServer((settings.BIND_HOST, settings.BIND_PORT), MultiServerHandler)
        server.serve_forever()


def main():
    print('waiting connect')
    MultiServer()
