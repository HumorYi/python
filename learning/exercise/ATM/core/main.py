#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/6 16:06
@Description: 

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/6 16:06
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

from core import auth
from core import logger
from core import accounts
from core import transaction
from core.auth import login_required
import time

trans_logger = logger.logger('transaction')
access_logger = logger.logger('access')

user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None
}


def account_info(account_data):
    print(user_data)


'''
let user repay the bill
:return:
'''


@login_required
def repay(account_data):
    interactive_common(account_data, 'Input repay amount:', 'repay')

    return False


'''
let user do the withdraw action
:param account_data:
:return:
'''


def withdraw(account_data):
    interactive_common(account_data, 'Input withdraw amount:', 'withdraw')

    return False


def transfer(account_data):
    pass


def pay_check(account_data):
    pass


def logout(account_data):
    # account_data['is_authenticated'] = False
    return False


'''
print current balance and let user do the interactive common action
:param account_data: 
:param input_tip:
:param type: interactive type
:return:
'''
def interactive_common(account_data, input_tip, type):
    account_data_latest = accounts.load_current_balance(account_data['account_id'])

    current_balance = ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' % (account_data_latest['credit'], account_data_latest['balance'])
    print(current_balance)

    while True:
        amount = input("\033[33;1m %s: \033[0m" % input_tip).strip()

        if len(amount) > 0 and amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger, account_data_latest, type, amount)
            if new_balance:
                print('''\033[42;1m New Balance:%s \033[0m''' % (new_balance['balance']))
        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer! \033[0m' % amount)

        if amount == 'b':
            break


'''
interact with user
:return:
'''


def interactive(account_data):
    menu = u'''
    ------- OldBoy Bank ---------
    \033[32;1m
    1.  账户信息
    2.  还款(功能已实现)
    3.  取款(功能已实现)
    4.  转账
    5.  账单
    6.  退出
    \033[0m'''

    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout,
    }

    while True:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            if menu_dic[user_option](account_data) is False:
                break
        else:
            print("\033[31;1m Option does not exist! \033[0m")


def run():
    account_data = auth.account_login(user_data, access_logger)

    if user_data['is_authenticated']:
        user_data['account_data'] = account_data
        interactive(user_data)
