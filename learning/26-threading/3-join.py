#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/25 17:15
@Description: 在子线程完成运行之前，这个子线程的父线程将一直被阻塞。

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/25 17:15
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import threading
from time import ctime, sleep


def music(func):
    for i in range(2):
        print("Begin listening to %s %s. %s" % (threading.currentThread(), func, ctime()))
        sleep(4)
        print("end listening %s %s" % (threading.currentThread(), ctime()))


def move(func):
    for i in range(2):
        print("Begin watching at the %s %s! %s" % (threading.currentThread(), func, ctime()))
        sleep(5)
        print("end watching %s %s" % (threading.currentThread(), ctime()))


threads = []
t1 = threading.Thread(target=music, args=('七里香',))
threads.append(t1)
t2 = threading.Thread(target=move, args=('阿甘正传',))
threads.append(t2)

if __name__ == '__main__':

    for t in threads:
        t.start()
        # t.join() # 阻塞主进程，子进程都执行完再执行主进程
    # t1.join() # t1 执行完不阻塞主进程
    # t2.join() # t2 执行完不阻塞主进程
    print("all over %s" % ctime())