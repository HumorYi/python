#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/12/13 14:35
@Description: 多进程 - 类式调用

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/12/13 14:35
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self):
        super(MyProcess, self).__init__()
        # self.name = name

    def run(self):
        time.sleep(1)
        print('hello', self.name, time.ctime())


if __name__ == '__main__':
    p_list = []

    for i in range(3):
        p = MyProcess()
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()

    print('end')
