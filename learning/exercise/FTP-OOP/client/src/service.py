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

import socket, json, os, re

from config import settings
from lib import commons


def login(conn):
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()

        conn.sendall(json.dumps({'username': username, 'password': password}).encode(settings.CHARSET))

        result = json.loads(conn.recv(settings.RECV_SIZE).decode(settings.CHARSET))

        if result['code'] == settings.CODE['AUTHORIZED_SUCCESS']['code']:
            print(result['msg'])
            break
        else:
            print('用户名或密码错误...')


def cmd(conn, inp):
    conn.sendall(inp.encode(settings.CHARSET))

    basic_info_str = conn.recv(settings.RECV_SIZE).decode(settings.CHARSET)

    conn.sendall("ack".encode(settings.CHARSET))

    print(basic_info_str)

    result_length = int(basic_info_str.split('|')[1])
    has_received = 0
    content_bytes = bytes()

    while result_length > has_received:
        fetch_bytes = conn.recv(settings.RECV_SIZE)
        has_received += len(fetch_bytes)
        content_bytes += fetch_bytes

    print(content_bytes.decode(settings.CHARSET))


def get(conn, inp): pass

def post(conn, inp):
    # post|F:\BaiduNetdiskDownload\day30-python 全栈开发-基础篇\30-02 python 全栈开发-基础篇-day30 FTP作业示例代码（一）.avi
    # inp  ===> post|D:/1.txt|2.txt
    commad_list = inp.split("|")
    local_path = commad_list[1]
    target_path = ''

    if len(commad_list) == 3:
        target_path = commad_list[2]
    else:
        local_path = local_path.replace('\\', '/')
        target_path = local_path.split('/')[-1]

    # 获取本地文件大小
    file_byte_size = os.stat(local_path).st_size
    # 获取本地文件名
    file_name = os.path.basename(local_path)
    # 获取本地文件md5值
    file_md5 = commons.fetch_file_md5(local_path)

    post_info = "post|%s|%s|%s|%s" % (file_byte_size, file_name, file_md5, target_path)

    conn.sendall(post_info.encode(settings.CHARSET))

    result_recv = json.loads(conn.recv(settings.RECV_SIZE).decode(settings.CHARSET))

    has_sent = 0

    if result_recv['code'] == settings.CODE['FILE_EXIST']['code']:
        inp_continue = input('文件已经存在，是否续传？Y/N').strip()

        if inp_continue.upper() == "Y":
            conn.sendall(str(settings.CODE['CONTINUED']['code']).encode(settings.CHARSET))
            has_sent = conn.recv(settings.RECV_SIZE).decode(settings.CHARSET)
            has_sent = int(has_sent)
        else:
            conn.sendall(settings.CODE['NO_CONTINUED']['code'].encode(settings.CHARSET))

    file_obj = open(local_path, 'rb')
    file_obj.seek(has_sent)

    while file_byte_size > has_sent:
        data = file_obj.read(settings.RECV_SIZE)

        conn.sendall(data)

        has_sent += len(data)

        commons.bar(has_sent, file_byte_size)

    file_obj.close()
    print('上传成功')


def help_info():
    print("""
        cmd|命令
        post|文件路径
        get|下载文件路径
        exit|退出
    """)


def execute(conn):
    choice_dict = {
        'cmd': cmd,
        'get': get,
        'post': post,
    }

    help_info()

    while True:
        # cmd|ls
        # post|本地路径 服务器上路径
        # get|服务器路径 本地路径
        inp = input('please input:').strip()

        if inp == 'help':
            help_info()
            continue

        choice = inp.split('|')[0]

        if choice == 'exit':
            return

        if choice in choice_dict:
            func = choice_dict[choice]
            func(conn, inp)


def main():
    conn = socket.socket()
    conn.connect((settings.BIND_HOST, settings.BIND_PORT))
    welcome_bytes = conn.recv(settings.RECV_SIZE).decode(settings.CHARSET)
    print(welcome_bytes)

    login(conn)

    execute(conn)

    conn.close()
