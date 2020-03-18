#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/14 10:28
@Description: 异常处理

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/14 10:28
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

"""
# full of exception
try:
    int('ASJDKF')
except Exception as e:
    print(e)
"""

"""
# IndexError
try:
    li = [11, 22]
    li[1423]
except IndexError as e:
    print(e)
"""

"""
# IndexError
try:
    int('abc')
except ValueError as e:
    print(e)
"""

"""
# error sort
try:
    li = [11, 22]
    li[1423]
except IndexError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
"""

"""
# error logic
try:
    li = [11, 22]
    li[1423]
except IndexError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
else: print('success')
finally: print('anyway error or success will execute')
"""

"""
# throw custom error
"""
try:
    raise Exception('custom error')
except Exception as e:
    print(e)
