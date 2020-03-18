#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/9/18 12:34
@Description: 函数

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/9/18 12:34
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

"""
# 无命名传参 S

# 指定参数个数，不能多传也不能少传，否则会报错
def func(a):
    print(a)

func(1)

# 设置参数默认值，推荐放在参数最后面定义
def defaultArg(name, age, money = 'Infinity'):
    print('Name: %s ' % name)
    print('Age: %d ' % age)
    print('Money: %s ' % money)

defaultArg('bamboo', 18)

# 不定参数个数，由外部决定传入参数的个数，函数内部以元组的方式存储传递的参数
def add(*args):
    # print(args)
    sum = 0
    for i in args: sum += i
    print(sum)

add(1, 2, 3)

# 无命名传参 E
"""

"""
# 命名传参 S

# 函数内部以字典的方式存储传递的参数
def print_info(**kwargs): print(kwargs)

print_info(name='bamboo', age=18, money='Infinity')

# 命名传参 E
"""

"""
# 无命名传参 + 命名传参
# 注意: 当一起使用这两种方式传参时，所有的无命名参数必须得在命名参数的左边
def print_info(*args, **kwargs): print(args, kwargs)

print_info(1, 2, 3, name='bamboo', age=18)
"""

"""
# 1、使用 return 关键字把函数的执行结果返回，外部可用一个变量接收
# 2、函数如果没有使用 return 进行返回，默认是返回 None
# 3、如果 return 多个对象，那么 python 内部会把多个对象封装成一个元组对象返回
"""
"""
def func_None(a): a+=1
print(func_None(1))

def func_return(a): return a
print(func_return(1))
"""

"""
# 作用域 built-in（系统作用域） -> global（全局作用域） -> enclosing（嵌套函数父级局部作用域） -> local（局部作用域）
# 变量的使用优先级：上边作用域从右到左
# 默认情况下，下级作用域对上级作用域的变量只有只读功能，如果想要进行写操作，得在函数作用域内顶部进行变量层级声明
count = 0
def scope_count():
    # 本地变量 count 在引用之前赋值
    # count = count + 3

    # 声明该变量为全局变量，则可以进行写操作
    # global  count
    # count = 5

    age = 1

    def local_scope_age():
        # 同上
        # age = age + 2

        # 声明该变量为全局变量，则可以进行写操作
        global count
        count += 2

        # 声明该变量不是 local(局部) 层级变量，而是上层作用域变量
        nonlocal age
        age = age + 5

    local_scope_age()

print(scope_count())
"""

"""
# 高阶函数：把函数的执行步骤进行拆分，通过把子函数作为一个参数传递给主函数进行调用
def f(n): return n*n
def func_sum(a, b, f): return f(a) + f(b)

print(func_sum(1, 2, f))
"""

"""
# api filter
list = [10000, 1000, 100, 10, 1]
def filter_func(val): return val > 1

# filter object is a iterator
result = filter(filter_func, list)
for item in result: print(item)
"""

"""
# api map
list = [10000, 1000, 100, 10, 1]
def map_func(val): return val * 10

# map object is a iterator
result = map(map_func, list)
for item in result: print(item)
"""

"""
# 使用 reduce api 得 导库
from functools import reduce

def add(x, y): return x + y
print(reduce(add, range(1, 10)))
print(reduce(lambda x, y: x * y, range(1, 5)))
"""

# 判断一个元素是否有迭代器
print(all('123430'))

# 执行表达式
print(eval('1 + 3*2'))
