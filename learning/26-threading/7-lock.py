#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/26 16:10
@Description: 同步锁，解决 数据公用 正确性

    GIL VS Lock
        GIL: cPython 解释器 保证同一时刻只有一个 线程 被 os 传递 给 cpu 执行，内核互斥，解释器控制
        Lock: 保证了用户程序中的 资源共享，只有当竞争线程执行完同步锁内部逻辑数据处理才释放锁，下个竞争线程重复处理，
            形成了 锁内 逻辑数据 是串行的，锁外 代码是并行的，既利用了多线程的优点，也保证了 共享数据的 正确性，程序自主控制

        GIL 和 Lock 两者各自模式相同，功能不同，相辅相成
------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/26 16:10
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import time
import threading

num = 100  # 设定一个共享变量

lock = threading.Lock()


def addNum():
    global num  # 在每个线程中都获取这个全局变量
    # num-=1

    # 在同步锁前后写进行多线程处理的逻辑，利用 cpu 提升性能
    print('many threading execute code 1')

    # 获取同步锁
    lock.acquire()

    # 串行 公共数据，锁死内部处理逻辑，保证当前线程数据处理完毕后 再执行竞争到的线程 同步锁内部逻辑，
    # 保证数据的正确性，而不是每个线程都拿原始数据进行操作，导致数据错误
    temp = num
    print('\n--get num: %d\n' % num)
    time.sleep(0.001)
    num = temp - 1  # 对此公共变量进行-1操作

    # 释放同步锁
    lock.release()

    # 在同步锁前后写进行多线程处理的逻辑，利用 cpu 提升性能
    print('many threading execute code 2')


thread_list = []

for i in range(100):
    thread_list.append(threading.Thread(target=addNum))

for t in thread_list:
    t.start()
    # t.join() # join会把整个线程给停住，造成了串行，失去了多线程的意义，只需要把计算(涉及到操作公共数据)的时候串行执行

print('\nfinal num:', num)
