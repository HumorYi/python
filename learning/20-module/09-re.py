#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/9/29 13:15
@Description: re 正则模块

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/9/29 13:15
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import re

# 匹配到的所有结果都存储在一个列表中返回
# print(re.findall('[1-9a-zA-Z]', '12tyAS') == re.findall('[1-9, a-z, A-Z]', '12tyAS'))

# 匹配到的结果存储在一个迭代器中返回，只匹配一次
# resultFindIter = re.finditer('[1-9a-zA-Z]', '12tyAS')
# print(next(resultFindIter).group())

# 匹配到的结果存储在一个对象中返回
# 注意：使用 search 查找内容时，得到的结果要先判断是否有值，有值才能掉 group 得到具体的值，没值调用 group 会报错
searchResult = re.search('bamboo', 'bamboo is so nice')
# if searchResult: print(searchResult.group())

# 注意: \ 匹配，在 python 中，\ 具有特殊意义，得通过转义符(\)才能匹配, \\ => \
#       在 re 模块中也是如此，由于 re 模块是在 python 中执行的，先经过 python 转义后再交由 re 模块转义
# r 修饰符的意思是：告诉 python 这是一个原生字符串，不需要转义
# print(re.findall('\\\\c', 'adsab\c') == re.findall(r'\\c', 'adsab\c'))

# (?P<name>) 给组别起名字，使其可读
# groupName = re.search('(?P<id>\d{3})/(?P<name>\w{3})', 'wewewqe132/abc')
# print(groupName.group())
# print(groupName.group('id'))
# print(groupName.group('name'))


# () 表示对匹配的规则进行分组，即把括号里面的所有内容看做是一组进行匹配
# 注意：findall 会优先匹配分组内容，而不是匹配所有规则匹配的内容
# print(re.findall('www.(\w+).com', 'www.baidu.com')) # ['baidu']
# (?:) 取消分组匹配的优先级，即匹配所有规则内容
# print(re.findall('www.(?:\w+).com', 'www.baidu.com')) # ['www.baidu.com']

# 只在字符串开始匹配，匹配到的结果存储在一个对象中返回
# 注意：使用 search 查找内容时，得到的结果要先判断是否有值，有值才能掉 group 得到具体的值，没值调用 group 会报错
matchResult = re.match('\d', '1abc123')


# if matchResult: print(matchResult.group())

# split 字符串分割匹配规则
# print(re.split('[k, s]', 'absdkabgas'))

# sub 根据匹配的规则进行字符串替换，默认替换规则匹配到的所有字符
# print(re.sub('a..b', '12', 'adsbaslasdb'))
# 第四个参数是控制替换次数
# print(re.sub('a..b', '12', 'adsbaslasdb', 1))
# subn 返回替换后的最终内容和替换次数
# print(re.subn('a..b', '12', 'adsbaslasdb'))

# compile 对正则进行编译，适合使用相同的正则进行多次操作，提升性能
# reg = re.compile('\d{3}')
# print(reg.findall('1243asdf'))
# print(reg.findall('as1234asf'))
