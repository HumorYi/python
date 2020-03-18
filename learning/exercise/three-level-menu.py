#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/8/21 11:26
@Description: 三级菜单

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/8/21 11:26
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

menus = {
    "北京": {
        "朝阳": {
            "国贸": {
                "CIOD": {},
                "HP": {},
                "渣打银行": {},
                "CCTV": {},
            },
            "望京": {
                "陌陌": {},
                "奔驰": {},
                "360": {},
            },
            "三里屯": {
                "优衣库": {},
                "apple": {},
            },
        },
        "昌平": {
            "沙河": {
                "老男孩": {},
                "阿泰包子": {},
            },
            "天通苑": {
                "链家": {},
                "我爱我家": {},
            },
            "回龙观": {},
        },
        "海淀": {
            "五渡口": {
                "谷歌": {},
                "网易": {},
                "Sohu": {},
                "Sogo": {},
                "快手": {},
            },
            "中关村": {
                "youku": {},
                "Iqiyi": {},
                "汽车之家": {},
                "新东方": {},
                "QQ": {},
            },
        },
    },
    "上海": {
        "浦东": {
            "陆家嘴": {
                "CICC": {},
                "高盛": {},
                "摩根": {},
            },
            "外滩": {},
        },
        "闵行": {},
        "静安": {},
    },
    "山东": {
        "济南": {},
        "德州": {
            "乐陵": {
                "丁务镇": {},
            },
            "平原": {},
        },
        "青岛": {},

    },
}
current_layer = menus
parent_layers = []

# 方式一：简单且易理解，性能高，适合数据量小，且对性能要求高
# 因为每次都是把当前父dict添加到parent_layers中，使用时直接拿对应的父dict即可，
# 但是如果数据量过大，内存开销很大，可能会导致内存溢出，程序被终止等
"""
while True:
    # 打印当前层信息
    for layer in current_layer:
        print(layer)

    # 获取用户输入的信息
    choice = input(">>>:").strip()

    # 避免用户没输入时一直按回车
    if len(choice) == 0: continue

    if choice == 'b':
        if parent_layers: current_layer = parent_layers.pop()
        else: print('this is the first level')
    elif choice == 'q':
        print('exit success!')
        break
    elif choice in current_layer:
        parent_layers.append(current_layer)
        current_layer = current_layer[choice]
    else: print('please enter correct option, thanks!')
"""


# 方式二：比方式一实现思路一致，处理过程稍难一点，性能相对方式一低一点，适合数据量大，对性能要求不太高
# 因为每次都是把当前父dict在menus中对应的key名字添加到parent_layers中，
# 使用时需要先遍历parent_layers，第1个key对应的是menus中的第一层dict，需要从menus中获取，
# 后面的其他key都是从menus中取到的第一个dict中取，
# 这样一来，虽然增多了计算量，但是最终在内存中只存储了当前层的父dict，内存开销减少，程序得到保护
while True:
    # 打印当前层信息
    for layer in current_layer:
        print(layer)

    # 获取用户输入的信息
    choice = input(">>>:").strip()

    # 避免用户没输入时一直按回车
    if len(choice) == 0: continue

    if choice == 'b':
        if parent_layers:
            parent_layers.pop()

            if parent_layers:
                for i, key in enumerate(parent_layers):
                    if i == 0: current_layer = menus[key]
                    else: current_layer = current_layer[key]
        if not parent_layers:
            if parent_layers != menus: current_layer = menus
            print('this is the first level')
    elif choice == 'q':
        print('exit success!')
        break
    elif choice in current_layer:
        parent_layers.append(choice)
        current_layer = current_layer[choice]
    else: print('please enter correct option, thanks!')
