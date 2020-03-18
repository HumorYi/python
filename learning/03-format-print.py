#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/8/20 10:00
@Description: 格式化输出

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/8/20 10:00
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

"""
    使用占位符进行格式化输出：
        %s => string
        %d => digit
        %f => float
"""

name = input('Name: ')
age = input('Age: ')
job = input('Job: ')
salary = input('Salary: ')

if age.isdigit():
    age = int(age)

if salary.isdigit():
    salary = int(salary)
# else:
#     exit('salary must input digit')

msg = """
--------- info of %s ---------
Name: %s
Age: %d
Job: %s
Salary: %d
You will be retire in %s
--------- end of %s ---------
""" % (name, name, age, job, salary, 65-age, name)

print(msg)
