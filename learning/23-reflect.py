#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/17 17:55
@Description: 反射

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/17 17:55
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return '%s-%s ' % (self.name, self.age)

foo = Foo('bamboo', 18)

print(getattr(foo, 'name'))
print(hasattr(foo, 'age'))
setattr(foo, 'gender', 'male')
print(getattr(foo, 'gender'))
delattr(foo, 'gender')
