#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/12/17 11:13
@Description: 多线程 - 管道(数据传递和接收)

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/12/17 11:13
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

from multiprocessing import Process, Pipe


def f(conn):
    conn.send('今晚308？')
    print(conn.recv())
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    parent_conn.send('see you tomorrow')
    p.join()
