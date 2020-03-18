#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/26 9:52
@Description: 类继承

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/26 9:52
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    # 定义每个线程都要运行的函数
    def run(self):
        print('running on number : %s' % self.num)
        time.sleep(3)

if __name__ == '__main__':
    myThread1 = MyThread(1)
    myThread2 = MyThread(2)

    myThread1.start()
    myThread2.start()