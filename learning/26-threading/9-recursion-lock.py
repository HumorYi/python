#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/29 11:59
@Description: 递归锁：为了支持在同一线程中多次请求同一资源，python提供了“可重入锁”：threading.RLock。
    RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源可以被多次acquire。
    直到一个线程所有的acquire都被release，其他的线程才能获得资源。

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/29 11:59
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import time, threading


class Account:
    def __init__(self, _id, balance):
        self.id = _id
        self.balance = balance
        self.lock = threading.RLock()

    def withdraw(self, amount):
        with self.lock:
            self.balance -= amount

    def deposit(self, amount):
        with self.lock:
            self.balance += amount

    def drawcash(self, amount):  # lock.acquire中嵌套lock.acquire的场景

        with self.lock:
            interest = 0.05
            count = amount + amount * interest

            self.withdraw(count)


def transfer(_from, to, amount):
    # 锁不可以加在这里 因为其他的其它线程执行的其它方法在不加锁的情况下数据同样是不安全的
    _from.withdraw(amount)

    to.deposit(amount)


alex = Account('alex', 1000)
yuan = Account('yuan', 1000)

t1 = threading.Thread(target=transfer, args=(alex, yuan, 100))
t1.start()

t2 = threading.Thread(target=transfer, args=(yuan, alex, 200))
t2.start()

t1.join()
t2.join()

print('>>>', alex.balance)
print('>>>', yuan.balance)
