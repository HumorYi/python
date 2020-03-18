#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/25 15:33
@Description: 多线程 计算密集型

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/25 15:33
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import time, threading

start = time.time()

isUseThreading = True
# isUseThreading = False
test_count_1 = 10000000
test_count_2 = 20000000


def add(n):
    sum = 0
    for i in range(n): sum += i
    print(sum)


if isUseThreading:
    threading_1 = threading.Thread(target=add, args=(test_count_1,))
    threading_2 = threading.Thread(target=add, args=(test_count_2,))

    threading_1.start()
    threading_2.start()

    threading_1.join()
    threading_2.join()
else:
    add(test_count_1)
    add(test_count_2)

end = time.time()

print('execute time is : ', end - start)
