#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/12/17 10:30
@Description: 多进程 - 队列(数据传递（复制）)

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/12/17 10:30
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

from multiprocessing import Process, Queue


def f(q, n):
    q.put([42, n, 'hello'])


if __name__ == '__main__':
    q = Queue()
    p_list = []
    for i in range(3):
        p = Process(target=f, args=(q, i))
        p_list.append(p)
        p.start()

    print(q.get())
    print(q.get())
    print(q.get())

    for i in p_list:
        i.join()
