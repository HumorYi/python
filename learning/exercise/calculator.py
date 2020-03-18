#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/6 11:37
@Description: 计算器

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/6 11:37
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""
import re

# 括号必须是对等的、不能有特殊字符、不能存在无效的小数点
def verify(source):
    return source.count('(') != source.count(')') or re.search('[^\s\d()+-/*.]', source) is None or re.search(
        '((?<!\d)\.(?!\d))|(\d+\.(?!\d))|((?<!\d)\.\d+)', source) is None


def format(source):
    source = source.replace(' ', '')
    source = re.sub('\+{2,}', '+', source)
    source = re.sub('-{2,}', '-', source)
    source = re.sub('\*{2,}', '*', source)
    source = re.sub('/{2,}', '/', source)
    source = re.sub('\.{2,}', '.', source)
    return source


# 注意：*/ 这种情况无法判断 是 * 还是 /
def revise(source):
    return source.replace('+-', '-').replace('-+', '-').replace('++', '+').replace('--', '+').replace('*+',
                                                                                                      '+').replace('/+',
                                                                                                                   '+')


def cal_mul_div(source):
    while True:
        search = re.search('-?\d+\.?\d*[*/]-?\d+\.?\d*', source)

        if search:
            result1 = search.group()

            x, y = re.split('[*/]', result1)

            isDiv = re.search('/', result1)

            if isDiv:
                result2 = float(x) / float(y)
            else:
                result2 = float(x) * float(y)

            source = source.replace(result1, str(result2))
        else:
            return source


def cal_add_sub(source):
    while True:
        search = re.search('-?\d+\.?\d*[+-]\d+\.?\d*', source)

        if search:
            result1 = search.group()

            x, y = re.split('[+-]', result1)

            isSub = re.search('-', result1)

            if isSub:
                result2 = float(x) - float(y)
            else:
                result2 = float(x) + float(y)

            source = source.replace(result1, str(result2))

        else:
            return source


def calculator(source):
    if verify(source) is False:
        print('请输入正确的计算表达式')
        return

    source = revise(format(source))

    while True:
        search = re.search('\([^()]+\)', source)
        if search:
            search_result = search.group()
            source = revise(source.replace(search_result, cal_add_sub(cal_mul_div(search_result))[1:-1]))
        else:
            return float(cal_add_sub(cal_mul_div(source)))


s = '1 - 2 * ( (33.2 - 2 - (-5 * 2.3 / 21 / (123.4 * 12 / 223.4 + (12.3 - 32.1)))) / (12.34 - (2 * 2)) )'
print(calculator(s) == eval(s))
