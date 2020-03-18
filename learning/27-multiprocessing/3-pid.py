#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/12/13 14:41
@Description: 多进程 - pid

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/12/13 14:41
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

from multiprocessing import Process
import os, time


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    info('\033[31;1mfunction f\033[0m')
    print('hello', name)

# window系统下，需要注意的是要想启动一个子进程，必须加上那句if __name__ == "main"，进程相关的要写在这句下面
if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m')
    time.sleep(1)
    p = Process(target=info, args=('bob',))
    p.start()
    p.join()
