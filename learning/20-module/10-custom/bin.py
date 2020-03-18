#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/5 16:48
@Description: 运行文件模块

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/5 16:48
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

"""
# 引入模块全部内容，加载在模块名字中

import calculator, time

print(calculator.x)
print(calculator.add(2, 3))
"""

"""
# 按需引入模块内容，加载在当前文件中
from calculator import add, sub
print(add(3, 4))
print(sub(3, 4))
"""

"""
# 直接引入模块所有内容，加载在当前文件中
from calculator import *
print(x)
print(add(1, 2))
"""

"""
# 按需引入模块内容，给引入的内容取别名，避免名字冲突，加载在当前文件中
from calculator import add as my_add
print(my_add(1, 2))
"""



"""
improt web # 执行了 web package 下的 __init__.py 文件 
"""

"""
# 导入同级 package 的 module
"""
from web import logger
logger.logger()

"""
# 导入同级 package 的 内部 package 中的 module
"""
from web.tools import code
code.code()

"""
# 导入同级 package 的 module 的 member
"""
from web.tools.code import code
code()