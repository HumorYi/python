#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/8/20 17:44
@Description: 字典

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/8/20 17:44
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

# 跟平常看到的json一致，key-value结构，内部数据存放时无序的,
# key是hash（不可变）的，value可以是任意类型

# 定义一个dict
dict = {
    "name": "bamboo",
    "age": 18,
    "money": 100000
}

# print(dict)

# 查 S
# 注意：获取不存在的key时会报错

# 直接去key名
# print(dict["name"])
# 通过get方法去取key，不存在默认会返回None
# print(dict.get("name"))
# 通过get方法去取key，不存在默认会返回None，可以通过传递第二个参数自定义返回默认值
# print(dict.get("sex", "male"))

# in 判断key是否存在
# print("money" in dict)

# 获取所有的key 一种包装数据类型，可以转为list/tuple
# print(dict.keys())
# dict_keys = list(dict.keys())
# print(dict_keys)

# 获取所有的value 一种包装数据类型，可以转为list/tuple
# print(dict.values())
# dict_values = list(dict.values())
# print(dict_values)

# 获取所有的项 一种包装数据类型，可以转为list/tuple
# print(dict.items())
# dict_items = tuple(dict.items())
# print(dict_items)

# 查 E

# 改 赋值
# 只修改一个
# dict["money"] = "Infinity"
# 如果存在，则覆盖值，否则新增key
# dict_other = { "body": "nice", "mind": "clever" }
# dict.update(dict_other)
# 判断是否存在key
# print("money" in dict)

# 删 pop
# dict.pop("age")
# clear 清空字典
# dict.clear()
# popitem 随机删除一个key
# print(dict.popitem())

# 增
# 如果key存在，则替换value，如果key不存在，则新增key
# dict['charm'] = 'Infinity'

# 如果key存在，什么操作都不做，如果key不存在，则新增key
# dict.setdefault('knowledge', 'Infinity')

# del
# del dict

# fromkeys 对传递过来的list当做key，把value对每个key进行统一赋值，适合做key的初始化
# print(dict.fromkeys(['a', 'b', 'c'], 'common val'))


# 遍历
# for key in dict:
#     print(key, dict[key])

# for key, val in dict.items():
#     print(key, val)

# copy() 函数返回一个字典的浅复制
"""
# 直接赋值和 copy 的区别
dict1 =  {'user':'runoob','num':[1,2,3]}
 
dict2 = dict1          # 浅拷贝: 引用对象
dict3 = dict1.copy()   # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
 
# 修改 data 数据
dict1['user']='root'
dict1['num'].remove(1)
 
# 输出结果
print(dict1) # {'num': [2, 3], 'user': 'root'}
print(dict2) # {'num': [2, 3], 'user': 'root'}
print(dict3) # {'num': [2, 3], 'user': 'runoob'}
"""


print(dict)