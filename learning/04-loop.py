#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/8/20 11:08
@Description: 循环

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/8/20 11:08
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

# for i in range(1, 100, 2):
#     print(i)

for i in range(200):
    if i == 100:
        print('right')
        # if break, the end else will not execute
        break
    else:
        print(i)
else:
    print('end')