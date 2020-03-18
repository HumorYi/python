#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/30 11:49
@Description: 信号量用来控制线程并发数的，BoundedSemaphore或Semaphore管理一个内置的计数器，
    每当调用acquire()时-1，调用release()时+1。

    计数器不能小于0，当计数器为 0时，acquire()将阻塞线程至同步锁定状态，直到其他线程调用release()。(类似于停车位的概念)

    BoundedSemaphore与Semaphore的唯一区别在于前者将在调用release()时检查计数器的值是否超过了计数器的初始值，
    如果超过了将抛出一个异常。

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/30 11:49
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import threading, time


class myThread(threading.Thread):
    def run(self):
        if semaphore.acquire():
            print(self.name)
            time.sleep(3)
            semaphore.release()


if __name__ == "__main__":
    semaphore = threading.BoundedSemaphore(5)
    thrs = []
    for i in range(100):
        thrs.append(myThread())
    for t in thrs:
        t.start()
