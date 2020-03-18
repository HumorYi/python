#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/25 11:30
@Description: 多线程 io 密集型
    cPython 解释器 中为了防止 多进程之间的数据篡改，加了一层 GIL ( Global Intercept Lock )，
    进程之间是争用cpu，进程的切换是通过阻塞当前进程，让后续进程有机会争用cpu，
    即每一时刻只能传输一个线程给 os 再传给一个 cpu 调用，用不了多核 cpu，适合处理 io 密集型任务，不适合 计算密集型任务

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/25 11:30
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import time, threading

start = time.time()

def foo(n):
    print('foo start, the arg is : ', n)
    time.sleep(1)
    print('foo end')

def bar(n):
    print('bar start, the arg is : ', n)
    time.sleep(2)
    print('bar end')

# 串程
# foo()
# bar()

# 并程
threading_foo = threading.Thread(target=foo, args=(1,))
threading_bar = threading.Thread(target=bar, args=(2,))

# 启动多线程
threading_foo.start()
threading_bar.start()

print('...run in the main threading...')

# 阻塞多线程，等待线程执行完毕
threading_foo.join()
threading_bar.join()

end = time.time()

print('execute time is: ', end - start)