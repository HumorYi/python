#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/30 17:38
@Description: 队列 (内部维护了一把锁，比列表安全)
    Python queue模块有三种队列及构造函数:
        1、Python queue模块的FIFO队列先进先出。  class queue.Queue(maxsize)
        2、LIFO类似于堆，即先进后出。             class queue.LifoQueue(maxsize)
        3、还有一种是优先级队列级别越低越先出来。   class queue.PriorityQueue(maxsize)

    此包中的常用方法(q = Queue.Queue()):
        q.qsize() 返回队列的大小
        q.empty() 如果队列为空，返回True,反之False
        q.full() 如果队列满了，返回True,反之False
        q.full 与 maxsize 大小对应
        q.get([block[, timeout]]) 获取队列，timeout等待时间
        q.get_nowait() 相当q.get(False)
        非阻塞 q.put(item) 写入队列，timeout等待时间
        q.put_nowait(item) 相当q.put(item, False)
        q.task_done() 在完成一项工作之后，q.task_done() 函数向任务已经完成的队列发送一个信号
        q.join() 实际上意味着等到队列为空，再执行别的操作

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/30 17:38
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

# import queue

# Queue类即是一个队列的同步实现。队列长度可为无限或者有限。可通过Queue的构造函数的可选参数maxsize来设定队列长度。
# 如果maxsize小于1就表示队列长度无限。
# q = queue.Queue(3)

"""
将一个值放入队列中
q.put(10)
调用队列对象的put()方法在队尾插入一个项目。put()有两个参数，第一个item为必需的，为插入项目的值；第二个block为可选参数，默认为
1。如果队列当前为空且block为1，put()方法就使调用线程暂停,直到空出一个数据单元。如果block为0，put方法将引发Full异常。
"""
# q.put('bamboo', 0)
# q.put('tom')
# q.put('baby')

"""
将一个值从队列中取出
q.get()
调用队列对象的get()方法从队头删除并返回一个项目。可选参数为block，默认为True。如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。如果队列为空且block为False，队列将引发Empty异常。
"""
# print(q.get())
# print(q.get())
# print(q.get())


"""
# 例子：吃包子
import threading, queue
from time import sleep
from random import randint


class Production(threading.Thread):
    def run(self):
        while True:
            r = randint(0, 100)
            q.put(r)
            print("生产出来%s号包子" % r)
            sleep(1)


class Proces(threading.Thread):
    def run(self):
        while True:
            re = q.get()
            print("吃掉%s号包子" % re)


if __name__ == "__main__":
    q = queue.Queue(10)
    threads = [Production(), Production(), Production(), Proces()]
    for t in threads:
        t.start()
"""

"""
# 例子：吃包子（复杂版）
import time, random, queue, threading

q = queue.Queue()


def Producer(name):
    count = 0
    while count < 20:
        time.sleep(random.randrange(3))
        q.put(count)
        print('Producer %s has produced %s baozi..' % (name, count))
        count += 1


def Consumer(name):
    count = 0
    while count < 20:
        time.sleep(random.randrange(4))
        if not q.empty():
            data = q.get()
            print(data)
            print('\033[32;1mConsumer %s has eat %s baozi...\033[0m' % (name, data))
        else:
            print("-----no baozi anymore----")
        count += 1


p1 = threading.Thread(target=Producer, args=('A',))
c1 = threading.Thread(target=Consumer, args=('B',))
p1.start()
c1.start()
"""
