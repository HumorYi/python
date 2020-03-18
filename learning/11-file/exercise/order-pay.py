#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/8/22 15:01
@Description: order.txt每一行内容分别为商品名字，价钱，个数，求出本次购物花费的总钱数

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/8/22 15:01
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

with open('order.txt', 'r', encoding='utf-8') as order:
    pay = 0

    for line in order:
        line = line.strip().split(' ')
        pay += int(line[len(line)-1])

    print('本次购物花费的总钱数: %d' % pay)