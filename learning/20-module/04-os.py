#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/9/27 17:52
@Description: 操作系统模块

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/9/27 17:52
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import os
path_file = 'E:/python/learning/20-module/01-time.py'

# 获取当前文件所在的目录
# print(os.getcwd())

# 改变当前文件所在的目录
# os.chdir('E:\python\learning')

# 返回当前目录  .
# print(os.curdir)
# 返回父目录  ..
# print(os.pardir)

"""
"""
# 目录操作，必须是合理的，不能创建已存在的目录，不能删除未存在的目录

# 创建目录
# os.mkdir('bamboo')

# 删除目录
# os.rmdir('bamboo')

# 创建多个目录
# os.makedirs('bamboo/test')

# 删除多个目录
# os.removedirs('bamboo/test')

# 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表的方式打开
# print(os.listdir('E:\python\learning'))

# 删除文件
# os.remove('test.py')

# 重命名 文件 / 目录
# os.rename('test.py', 'go.py')
# os.rename('test', 'bamboo')

# 获取 文件 / 目录信息，并以列表的方式打开
# print(os.stat('./03-main.py'))

# 获取系统的 文件分隔符 => windows: \     linux: /
# print(os.sep)

# 获取系统的 换行分隔符 => windows: \r\n     linux: /n    max: /r
# print(os.linesep)

# 获取系统的 文件路径(环境变量)分隔符 => windows: ;     linux: :
# print(os.pathsep)

# 获取系统的 平台名字 => windows: nt     linux: posix
# print(os.name)

# 运行 shell 命令，直接显示
# print(os.system("dir"))

# 获取系统的环境变量
# print(os.environ)

# 获取 文件 / 目录 绝对路径
# print(os.path.abspath('./01-time.py'))

# 将 path 分割成目录和文件名二元组
# print(os.path.split(path_file))

# 获取 path 的父目录
# print(os.path.dirname(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))

# 返回 path 最后的文件名，如果 path 以 / 或 \ 结尾，那么就会返回空值
# print(os.path.basename(path_file))
# 如果path存在，返回True；如果path不存在，返回False
# print(os.path.exists(path_file))
# 如果path是绝对路径，返回True
# print(os.path.isabs(path_file))
# 如果path是一个存在的文件，返回True。否则返回False
# print(os.path.isfile(path_file))
# 如果path是一个存在的目录，则返回True。否则返回False
# print(os.path.isdir(path_file))
# 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# print(os.path.join(os.path.dirname(path_file), '03-main.py'))
# 返回path所指向的文件或者目录的最后存取时间
# print(os.path.getatime(path_file))
# 返回path所指向的文件或者目录的最后修改时间
# print(os.path.getmtime(path_file))

