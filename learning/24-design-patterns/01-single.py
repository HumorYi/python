#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/18 11:24
@Description: 单例模式

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/18 11:24
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

class Foo:
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance:
            return cls.__instance

        cls.__instance = cls()
        return cls.__instance

foo1 = Foo.get_instance()
foo2 = Foo.get_instance()
foo3 = Foo.get_instance()
print(foo1 == foo2 and foo1 == foo3 and foo2 == foo3)
