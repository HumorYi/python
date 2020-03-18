#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/9/27 10:03
@Description: 生成器

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/9/27 10:03
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

"""
# 生成器：列表
generator = (x for x in range(5))
# print(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

# for i in generator: print(i)
"""

"""
# 生成器：yield
def foo():
    print('start 1')
    yield 1

    print('start 2')
    yield 2

# gen = foo()
# next(gen)
# next(gen)

for i in foo(): print(i)
"""

"""
def fibonacci(max):
    n, before, after = 0, 0, 1

    while(n < max):
        yield before
        before, after = after, before + after
        n += 1

for i in fibonacci(8): print(i)
"""

def bar():
    print('start 1')
    count = yield 1

    print(count)

    print('start 2')
    yield 2

gen = bar()
# next(gen)
gen.send(None) # 第一次 send 前如果没有 next，只能传 None
gen.send('transfer count')
