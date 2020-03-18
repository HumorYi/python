#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/9/27 13:36
@Description: 迭代器

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/9/27 13:36
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

# 迭代器不一定是生成器，生成器一定是迭代器

l = [1, 2, 3, 4]
it = iter(l)
print(next(it))

"""
for 循环内部三部曲：
    1、调用可迭代对象的 iter 方法返回一个迭代器对象
    2、不断调用迭代器对象的 next 方法
    3、处理 StopIteration 异常
for i in l: print(i)
"""

from collections.abc import Iterator, Iterable

print(isinstance(l, list))
print(isinstance(l, Iterable))
print(isinstance(l, Iterator))
print(isinstance(it, Iterator))