#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/8/22 9:53
@Description: 文件读操作

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/8/22 9:53
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

# open 打开文件，第一个参数：文件路径，第二个参数：模式（r读），第三个参数：读取编码
file = open('read.txt', 'r', encoding='utf-8')

# 读取文件，无参数：读取文件所有内容；有参数：要读取的字符数量
# print(file.read(5))
# print(file.read(5))

# 读取文件中的一行内容
# print(file.readline())
# print(file.readline())


# 读取文件的所有行内容（每行中的换行符\n会添加到每行内容后面），存储到list中并返回
# print(file.readlines())

# 获取文件每一行的内容 两种方式只能同时存在一个有效，因为读取文件是比较耗资源的操作
# 方式1 readlines() 使用于多次读取，内存大
# for line in file.readlines(): print(line.strip())
# 方式2 迭代器，适用于单词读取，line是用一行取一行，用完就扔掉，不会存在内存中
# for line in file: print(line.strip())

# 获取当前光标位置,注意：读取中文时，utf-8对中文编码是占3个字节
# print(file.tell()) # 0
# print(file.read(4))
# print(file.tell()) # 6

# 修改光标位置
# print(file.read(2))
# file.seek(0)
# print(file.read(4))

# 关闭文件
file.close()