#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/8/20 15:38
@Description: 购物车 -- 实现

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/8/20 15:38
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

commodities = [
    ( 1, 'iphone6s', 5800 ),
    ( 2, 'mac book', 9000 ),
    ( 3, 'coffee', 32 ),
    ( 4, 'python book', 80 ),
    ( 5, 'bicyle', 1500 )
]

print('商品列表:\r \n')
print('商品编号\t\t商品名称\t\t商品价格')

for commodity in commodities:
    print('%d\t\t\t%s\t\t￥%d' % (commodity[0], commodity[1], commodity[2]))

print('\r\n如果您购买完毕，想退出购买系统，请输入quit\r\n')

salary = input('请输入您的工资：')

while True:
    if salary.isdigit():
        salary = int(salary)
        balance = salary
        break
    else:
        print('\r\n请输入整数，谢谢合作\r\n')
        salary = input('请输入您的工资：')

commoditySerialNumbers = []
commoditySerialNumber = ''

while True:
    commoditySerialNumber = input('请输入要购买的商品数字编号: ')

    if commoditySerialNumber == 'quit':
        print('\r\n您已购买以下商品：')

        for commoditySerialNumber in commoditySerialNumbers:
            for commodity in commodities:
                if commoditySerialNumber == commodity[0]:
                    print('%s ￥%d' % (commodity[1], commodity[2]))
                    break

        print('\r\n您的余额为：￥%d' % balance)
        print('欢迎您下次光临')
        break

    if commoditySerialNumber.isdigit(): commoditySerialNumber = int(commoditySerialNumber)
    else: print('\r\n商品数字编号输入错误，请您检查后再输入，谢谢合作\r\n')

    for commodity in commodities:
        if commoditySerialNumber == commodity[0]:

            price = commodity[2]

            if balance < commodity[2]: print('余额不足，￥%d' % (balance - price))
            else:
                commoditySerialNumbers.append(commoditySerialNumber)
                balance -= price
                print('购买成功，%s 已加入您的购物车，当前余额为: ￥%d' % (commodity[1], balance))

            break