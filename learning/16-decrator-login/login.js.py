#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/9/26 13:25
@Description: 通过装饰器实现登录，具体需求：
    3 个页面，home、finance、book，
    用户输入对应页面名，后台检查用户登录状态，
    如果未登录，用户输入用户名和密码进行登录，登录成功，修改用户登录状态


------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/9/26 13:25
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""
import json

login_status = False
pages = ("home", "finance", "book")
auth_types = ("weixin", "jingdong")

def login(auth_type):

    def inner_auth_type(fn):

        def inner(*args, **kwargs):
            global login_status

            if login_status:
                fn(*args, **kwargs)
                return

            if auth_type not in auth_types:
                print("用户认证类型无效")
                return

            print("正在跳转登录页面...")

            username = input("请输入用户名>>:")
            password = input("请输入密码>>:")

            file = ""

            if auth_type is "weixin":
                file = open("./data/weixin.json", "r", encoding="utf-8")
            elif auth_type is "jingdong":
                file = open("./data/jingdong.json", "r", encoding="utf-8")

            users = json.load(file)

            while(not (username in users and password == users[username])):
                print("用户名或密码错误")
                username = input("请输入用户名>>:")
                password = input("请输入密码>>:")

            login_status = True
            fn()

        return inner

    return inner_auth_type

@login(auth_types[1])
def home(): print("Welcome to home page")

@login(auth_types[0])
def finance(): print("Welcome to finance page")

@login(auth_types[1])
def book(): print("Welcome to book page")

for page in pages: print(page)

input_page = ''

while (input_page not in pages): input_page = input("请输入您要进入的页面名称>>:")

if input_page == pages[0]: home()
elif input_page == pages[1]: finance()
elif input_page == pages[2]: book()

input_page = ''
while (input_page not in pages): input_page = input("请输入您要进入的页面名称>>:")

if input_page == pages[0]: home()
elif input_page == pages[1]: finance()
elif input_page == pages[2]: book()

