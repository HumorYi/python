#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/8/21 9:10
@Description: 

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/8/21 9:10
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

str = "Let's go"

# print(str)

# repeat
# print('hello' * 20)

# 查 with the same list
# print('hello world'[:])

# in 判断字符是否在string中
# print('el' in 'hello')

# % 格式化字符串
# print('%s is a good programmer' % 'bamboo')

# + / join 字符串拼接
# a = '123'
# b = '456'
# c = '789'
# d = a + b + c
# print(d)
#
# e = ''.join([a, b, c])
# print(e)

# string内置方法
str2 = 'hello kitty'

# 获取字符出现的次数
# print(str2.count('l'))

# 首字母转为大写
# print(str2.capitalize())

# 判断字符串是否已某串字符结尾
# print(str2.endswith('y'))

# 判断字符串是否已某串字符开头
# print(str2.startswith('he'))

# 设置字符串中\t占据的空格大小
# print('he\tllo world'.expandtabs(tabsize=20))

# 占位符 format vs format_map 只是传参方式不同
# print('hello kitty {name} is {age}'.format(name='bamboo', age=18))
# print('hello kitty {name} is {age}'.format_map({'name':'bamboo','age':18}))


# 判断字符串是否只有数字或字母，空格啥的都不行
# print('12'.isalnum())

# 判断字符串是否为十进制数
# print('0010'.isdecimal())

# 判断字符串是否为正整数
# print('-1269999'.isdigit())
# print('1269999'.isnumeric())

# 是否合法标识符
# print('a'.isidentifier())

# 是否为全小写字符
# print('abc1'.islower())
# 是否为全大写字符
# print('ABC1'.isupper())

# 判断字符串是否为空格
# print(' '.isspace())

# 是否为标题 => 每个单词首字母已大写的形式表示
# print('My Title'.istitle())

# 大写字符转为小写字符
# print('My Title'.lower())
# 小写字符转为大写字符
# print('My Title'.upper())
# 大写字符转为小写字符,小写字符转为大写字符
# print('My Title'.swapcase())


# 居中显示字符，第一个参数为字符总数，第二个参数为剩余位置填充字符
# print(str2.center(50, '#'))
# 居左显示字符，第一个参数为字符总数，第二个参数为剩余位置填充字符
# print(str2.ljust(50, '#'))
# 居右显示字符，第一个参数为字符总数，第二个参数为剩余位置填充字符
# print(str2.rjust(50, '#'))

# 去掉开头和结尾的 空格、换行符、制表符、回车符
# 左右两边都去掉
# print('\tMy Title\n'.strip())
# 只去掉左边
# print('\tMy Title\n'.lstrip())
# 只去掉右边
# print('\tMy Title\n'.rstrip())

# 替换字符串中匹配到的所有查找字符，第一个参数是要替换的字符，第二个参数是替换内容，第三个参数是替换字符集中匹配查找内容的次数
# print('My Title Title'.replace('Title', 'house', 1))

# 查找字符的下标，找不到返回-1
# print(str2.find('t'))
# 查找字符最后出现的索引位置，找不到返回-1
# print('My title title'.rfind('a'))
# 查找字符的下标，找不到会报错
# print(str2.index('g'))

# 把字符串按指定字符切割，转为list, 第一个参数：以哪个字符作为切割标志，第二个参数：切割次数
# 从左边开始切
# print('My title title'.split('i',1))
# 从右边开始切
# print('My title title'.rsplit('i',1))

# 把字符转为标题，其实就是首字母大写
# print('My title title'.title())


#摘一些重要的字符串方法
# print(st.count('l'))
# print(st.center(50,'#'))   #  居中
# print(st.startswith('he')) #  判断是否以某个内容开头
# print(st.find('t'))
# print(st.format(name='alex',age=37))  # 格式化输出的另一种方式   待定：?:{}
# print('My Title'.lower())
# print('My Title'.upper())
# print('\tMy Title\n'.strip())
# print('My title title'.replace('itle','lesson',1))
# print('My title title'.split('i',1))