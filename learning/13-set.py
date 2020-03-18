#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/9/15 10:06
@Description: set 集合是无序且不重复的，内部的元素必须是可 hash 的，创建好的集合是不可 hash 的，没有索引，去重，保证数据唯一性
    set 是可变集合
    frozenset 是不可变集合

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/9/15 10:06
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""
"""
s = set('bamboo')
print(s)
s1 = set(['bamboo', 'ruby', 'bamboo'])
print(s1, type(s1))

# to list
s2 = list(s1)
print(s2)
"""

"""
# 元素必须是可 hash 的
li = [ [1, 2], 3, 'alex' ]
s3 = set(li)
print(s3)
"""

# unhashable type: 'list
# d = { s2: 3 }


"""
# 没有索引，只能通过 循环 的方式去遍历集合，取得对应的数据
for item in set(['baba', 'kaka']):
    print(item)
"""

"""
# 传递给集合的参数会被拆解成单个元素添加进集合中，
# 普通数据类型、列表都一样，字段只会把key添加进去，因为 set 认为字段的 key 是不可 hash 的
c = set('bamboo')
d = set(['bamboo', 123])
e = set({'name': 'bamboo', 'age': 18})
print(c)
print(d)
print(e)
"""

"""
# api: add 添加数据，把参数当成一个完整的数据整个添加进集合中，不存在参数数据是重复的就只添加一个元素
f = set('next')
f.add('gg')
print(f)
"""

"""
# api: update 更新数据，也可进行添加数据，会把参数数据拆开成一个一个单独的数据分别添加到集合中
g = set({'name': 'ruby'})
g.update({'name': 'angle'})
g.update([123, 'baby'])
print(g)
"""

"""
# api: pop 随机删除数据
h = set('ruby')
h.pop()
print(h)
"""

"""
# api: clear 清空整个集合数据，变成一个空集合
i = set('bamboo')
i.clear()
print(i)
"""

"""
# set 集合之间的关系
j = set([1, 2, 3, 4, 5])
k = set([4, 5, 6, 7, 8])

# api: intersection 取两个集合的交集
print(j.intersection(k))
# 操作符表现形式
print(j & k)

# api: union 取两个集合的并集
print(j.union(k))
# 操作符表现形式
print(j | k)

# api: difference 取两个集合的单向差集，取 前一个集合中除了与后一个集合交集的 所有数据
print(j.difference(k))
# 操作符表现形式
print(j - k)

# api: symmetric_difference 取两个集合的对称差集（方向交集），除了交集之外的所有数据
print(j.symmetric_difference(k))
# 操作符表现形式
print(j ^ k)

# api: issuperset 判断前一个集合是否为后一个集合的超集（父集）
print(j.issuperset(k))
# 操作符表现形式
print(j > k)

# api: issubset 判断前一个集合是否为后一个集合的子集
print(j.issubset(k))
# 操作符表现形式
print(j < k)
"""

"""
# set == 生成的集合数据是 按照 集合里面元素来比较的，相当于普通数据类型(字符串、数字)比较
print(set('bamboo') == set('bamboo'))
print(set('bamboo') == set('bamboooo'))
"""

"""
# set < 判断前一个集合是否为后一个集合的子集合，如果两个集合元素完全一致，则认为是不包含的，跟数学中不一样
print(set('bamboo') < set('bamboo'))
print(set('bamboo') < set('bambooShow'))
"""

"""
# set or 或操作符，如果左边的数据 进行 Boolean 转化之后返回的是 False，则取左边，否则取右边
print(set('left') or False)
"""

"""
# set and 并操作符，无论左边的数据是什么类型，只取右边的数据
print(set('left') and False)
print(set('left') and set('right'))
"""