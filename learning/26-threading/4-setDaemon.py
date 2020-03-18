#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/25 17:16
@Description: 将线程声明为守护线程，必须在start() 方法调用之前设置， 如果不设置为守护线程程序会被无限挂起。
    这个方法基本和join是相反的。当我们 在程序运行中，执行一个主线程，如果主线程又创建一个子线程，
    主线程和子线程 就分兵两路，分别运行，那么当主线程完成想退出时，会检验子线程是否完成。
    如 果子线程未完成，则主线程会等待子线程完成后再退出。
    但是有时候我们需要的是 只要主线程完成了，不管子线程是否完成，都要和主线程一起退出，这时就可以 用setDaemon方法啦

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/25 17:16
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

    t1.setDaemon(True)
    # t2.setDaemon(True)
    for t in threads:
        # t.setDaemon(True)
        t.start()
    print("\nall over %s" % ctime())
