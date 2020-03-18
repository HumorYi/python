#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/12/17 11:54
@Description: 多进程 - 进程池

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/12/17 11:54
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

from multiprocessing import Pool
import time


def Foo(i):
    time.sleep(2)
    return i + 100


def Bar(arg):
    print('-->exec done:', arg)

if __name__ == '__main__':
    pool = Pool(5)

    for i in range(10):
        pool.apply_async(func=Foo, args=(i,), callback=Bar)
        # pool.apply(func=Foo, args=(i,))

    print('end')
    pool.close()
    pool.join()
