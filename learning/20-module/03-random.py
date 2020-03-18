#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/9/27 15:49
@Description: 随机数模块

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/9/27 15:49
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import random

# 0 ~ 1 的随机数
# print(random.random())
# # 指定范围 start ~ end
# print(random.randint(1, 8))
#
# # 从传递的参数中随机选取一个
# print(random.choice('hello'))
# print(random.choice([1, 2, 3, 4]))
# print(random.choice(('bamboo', 'nice')))
#
# # 随机打乱
# number_list = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
# print ("Original list : ",  number_list)
# random.shuffle(number_list)
# print ("List after first shuffle  : ",  number_list)
#
# # 指定选择个数
# print(random.sample(['123', 4, [1, 2], 'bamboo', 'name'], 2))
#
# # 从 range 中随机取一个
# print(random.randrange(1, 3))

# 0 ~ 9
codes = list(range(10))
# A ~ Z
codes.extend([chr(x) for x in range(65, 91)])
# a ~ z
codes.extend([chr(x) for x in range(97, 123)])

def verify_code_simple(size=4):
    code = ''

    for i in range(size):
        code += str(random.choice([random.randrange(10), chr(random.randint(65, 91))]))

    return code

def verify_code_shuffle(size=4):
    random.shuffle(codes)
    return "".join([str(x) for x in codes[0:size]])

# 推荐
def verify_code(size=4): return "".join([str(x) for x in random.sample(codes, size)])

print(verify_code_simple())
print(verify_code_shuffle())
print(verify_code())
