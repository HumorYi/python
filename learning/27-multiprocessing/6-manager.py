#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/12/17 11:45
@Description: 多线程 - 管道(数据共享)

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/12/17 11:45
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

from multiprocessing import Process, Manager


def f(d, l, n):
    d[n] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(n)


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()

        l = manager.list()
        p_list = []

        for i in range(10):
            p = Process(target=f, args=(d, l, i))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print(d)
        print(l)
