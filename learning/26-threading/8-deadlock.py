#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/29 11:09
@Description: 死锁；在线程间共享多个资源的时候，如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁，
    因为系统判断这部分资源都正在使用，所有这两个线程在无外力作用下将一直等待下去
    多线程之间互争cpu，互争多个锁，导致锁没法释放，最终程序一直在等待状态，使用递归锁解决

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/29 11:09
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import threading, time


class myThread(threading.Thread):
    def doA(self):
        lockA.acquire()
        print(self.name, "gotlockA", time.ctime())
        time.sleep(3)
        lockB.acquire()
        print(self.name, "gotlockB", time.ctime())
        lockB.release()
        lockA.release()

    def doB(self):
        lockB.acquire()
        print(self.name, "gotlockB", time.ctime())
        time.sleep(2)
        lockA.acquire()
        print(self.name, "gotlockA", time.ctime())
        lockA.release()
        lockB.release()

    def run(self):
        self.doA()
        self.doB()


if __name__ == "__main__":

    lockA = threading.Lock()
    lockB = threading.Lock()
    threads = []
    for i in range(5):
        threads.append(myThread())
    for t in threads:
        t.start()
    for t in threads:
        t.join()
