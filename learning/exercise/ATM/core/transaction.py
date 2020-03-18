#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/6 18:01
@Description: 

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/6 18:01
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

from conf import settings
from core import accounts
from core import logger

# transaction logger


'''
deal all the user transactions
:param account_data: user accounts data
:param tran_type: transaction type
:param amount: transaction amount
:param others: mainly for logging usage
:return:
'''


def make_transaction(log_obj, account_data, tran_type, amount, **others):
    amount = float(amount)
    if tran_type in settings.TRANSACTION_TYPE:
        transaction = settings.TRANSACTION_TYPE[tran_type]
        interest = amount * transaction['interest']
        old_balance = account_data['balance']
        action = transaction['action']

        if action == 'plus':
            new_balance = old_balance + amount + interest
        elif action == 'minus':
            new_balance = old_balance - amount - interest
            # check credit
            if new_balance < 0:
                print('''\033[31;1m Your credit [%s] is not enough for this transaction [-%s], your current balance is 
                [%s]''' % (account_data['credit'], (amount + interest), old_balance))
                return

        account_data['balance'] = new_balance
        accounts.dump_account(account_data)  # save the new balance back to file
        log_obj.info("accounts:%s   action:%s    amount:%s   interest:%s" %
                     (account_data['id'], tran_type, amount, interest))
        return account_data
    else:
        print("\033[31;1mTransaction type [%s] is not exist!\033[0m" % tran_type)
