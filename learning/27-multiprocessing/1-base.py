#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/12/13 14:34
@Description: 多进程 - 基础用法

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/12/13 14:34
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

from multiprocessing import Process
import time

def f(name):
    time.sleep(1)
    print('hello', name, time.ctime())

if __name__ == '__main__':
    p_list=[]

    for i in range(3):
        p = Process(target=f, args=('alvin',))
        p_list.append(p)
        p.start()

    for p in p_list:
        p.join()

    print('end')