#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/11/4 10:18
@Description:

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/11/4 10:18
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import random, math, os
from conf.settings import PRINT_COLOR, CHARSET, STORAGE

# 0 ~ 9
codes = list(range(10))
# A ~ Z
codes.extend([chr(x) for x in range(65, 91)])
# a ~ z
codes.extend([chr(x) for x in range(97, 123)])


def generate_random_character(size):
    """
    生成指定长度的随机字符（0-9a-zA-Z）
    :param size: 要生成的字符长度
    :return: str
    """
    return "".join([str(x) for x in random.sample(codes, size)])


def input_color(text, type=32):
    """
    设置输入文本字体颜色
    :param text: 文本
    :param type: 颜色类型
    :return:
    """
    return input('\033[%d;%s >>>: \033[0m' % (type, text))


def print_color(text, type=32):
    """
    设置输出到控制台的文本字体颜色
    :param text: 文本
    :param type: 颜色类型
    :return:
    """
    print('\033[%d;1m %s \033[0m' % (type, text))


def print_bgc(text, type=32):
    """
    设置输出到控制台的文本背景颜色
    :param text: 文本
    :param type: 颜色类型
    :return:
    """
    print_color(text, type)


def receive(conn):
    """
    接收 client 传输数据，并返回
    :param conn: socket 连接对象
    :return:
    """
    while True:
        # windows 强制中断程序导致数据接收失效异常
        try:
            # 接收信息
            data = conn.recv(1024)
        except Exception as e:
            print_color('传输异常 %s ' % e, PRINT_COLOR['red'])
            break

        # 信息为空时退出当前连接
        # if not data.decode(CHARSET):
        #     break

        # 打印信息
        # print_color('receive data is : [%s]' % data, PRINT_COLOR['green'])

        return data


def file_write(conn, path, file_size, config):
    """
    文件写入
    :param conn: socket 对象
    :param path: 用户家目录
    :param file_size: 文件大小
    :param config: 配置信息
    :return: bool
    """
    file = open(path, 'ab')
    last_progress = 0

    while config['file_receive_size'] != file_size:
        data = receive(conn)
        file.write(data)
        config['file_receive_size'] += len(data)
        last_progress = progress(config['file_receive_size'], file_size, last_progress)

    file.close()
    print_color('write success', PRINT_COLOR['green'])
    return True


def send_file(conn, path, file_size, config):
    """
    文件发送
    :param conn: socket 对象
    :param path: 用户家目录
    :param file_size: 文件大小
    :param config: 配置信息
    :return: bool
    """
    file = open(path, 'rb')

    last_progress = 0

    # 断点续传, 扔掉已下载的字节数
    file.seek(config['file_send_size'])

    # 从已下载的字节数开始读取并发送
    while config['file_send_size'] != file_size:
        data = file.read(1024)
        conn.sendall(data)
        config['file_send_size'] += len(data)
        last_progress = progress(config['file_send_size'], file_size, last_progress)

    file.close()
    print_color('send success', PRINT_COLOR['green'])
    return True


def send_text(conn, data):
    data_len = len(data)
    # 先传输命令处理结果总长度，防止内容过长，客户端一次性接收不了导致数据接收错误
    conn.send(str(data_len).encode(CHARSET))

    # 粘包现象 当发送数据时，会以很快的速度扫描一下后续还有没有数据也要发送，如果有则把后续数据合并再一起发送
    # 解决方法: 阻塞发送后续数据
    # receive(conn)

    # 发送信息
    start = 0
    send_size = 1024
    end = math.ceil(data_len / send_size)

    while start < end:
        conn.sendall(data[start * send_size:start + 1 * send_size].encode(CHARSET))
        start += 1

    return start == end


def receive_text(conn):
    """
    接收传输文本（可长可短）
    :param conn: socket 连接对象
    :return:
    """
    data_len = int(receive(conn).decode(CHARSET))

    receive_len = 0

    result = ''

    while receive_len != data_len:
        data = receive(conn).decode(CHARSET)
        result += data
        receive_len += len(data)

    return result


def progress(start, end, prev):
    """
    显示进度条
    :param start: 开始位置
    :param end: 结束位置
    :return: void
    """
    current = math.floor(start / end * 100)

    if prev < current:
        print_color('%d%%' % current, PRINT_COLOR['green'])

    return current


def transferByBroken(path):
    """
    断点续传，先获取已传输文件的字节长度，告诉客户端从此处开始上传，服务端接收数据继续写该文件
    :param path: 要上传的文件路径
    :return: size
    """
    if os.path.isfile(path):
        return os.stat(path).st_size

    return 0


def format_storage(bit_size):
    """
    格式化存储空间
    :param bit_size: 字节大小
    :return: 'x.xxMB'
    """
    last_item = ''

    for item in STORAGE:
        if bit_size < STORAGE[item]:
            return '%.2f%s' % (bit_size / STORAGE[last_item], last_item)
        else:
            last_item = item
