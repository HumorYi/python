#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/9/26 10:04
@Description: 装饰器

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/9/26 10:04
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""
import time

"""
def foo():
    print('foo')
    time.sleep(2)

def bar():
    print('bar')
    time.sleep(3)

# 改变调用方式，违反封闭开放原则
def showTime(fn):
    start = time.time()
    fn()
    end = time.time()
    print(end - start)
    
showTime(foo)
showTime(bar)
"""

"""
# 通过闭包返回一个内置函数，内置函数里对传递进来的函数进行装饰，再执行传递的函数，这就是装饰器的原理
# 该装饰器不能传参

def show_time(fn):
    def inner(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)
        end = time.time()
        print('spend %s second' % (end - start))

    return inner

# 先让装饰器函数加工传递的函数，再把加工好的函数重新赋值给传递进来的函数变量，不优雅
# foo=showTime(foo)
# bar=showTime(bar)

@show_time
def foo(name):
    print(name)
    time.sleep(1)

@show_time
def bar(name):
    print(name)
    time.sleep(1)


foo('foo')
bar('bar')

"""

def logger(flag):

    def show_time(fn):

        def inner(*args, **kwargs):

            start = time.time()
            fn(*args, **kwargs)
            end = time.time()

            if (flag): print('spend %s second' % (end - start))

        return inner

    return show_time


@logger(True)
def add(*args, **kwargs):
    sums = 0

    for i in args: sums += i

    print(sums)

    print(kwargs)
    time.sleep(1)

add(1, 2, 32, 231, 5, 123, name="bamboo", age="18")


















