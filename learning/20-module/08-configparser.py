#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/9/29 11:20
@Description: configparser 配置文件

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/9/29 11:20
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import configparser

config = configparser.ConfigParser()
filename = 'example.ini'

"""
# 创建配置文件

config["DEFAULT"] = {
    'ServerAliveInterval': '45',
    'Compression': 'yes',
    'CompressionLevel': '9',
    'ForwardX11': 'yes'
}

config['bitbucket.org'] = {
    'User': 'hg'
}

config['topsecret.server.com'] = {
    'HostPort': '50022',
    'ForwardX11': 'no'
}

config.write(open(filename, 'w'))

"""

# 读取配置文件
config.read(filename)

# 查看配置文件的选项(除了 DEFAULT )
# print(config.sections())

# 查看配置文件的 DEFAULT 选项
# print(config.defaults())

# 打印单独键的 key 时，同时也会把 DEFAULT 选项的 key 打印出来，因为 DEFAULT 是所有 key 共用的
# for key in config['bitbucket.org']: print(key)

# 删除选项
config.remove_section('topsecret.server.com')

# 判断是否存在 key
# print(config.has_section('topsecret.server.com'))
# print('bytebong.com' in config)


# 修改 config key 对应的 key val
# config.set('bitbucket.org', 'user', 'bamboo')

# 删除 config key 对应的 key
config.remove_option('bitbucket.org', 'user')

# 注意：删除和修改配置时，要想配置生效，必须得重新写入文件覆盖就有内容
config.write(open(filename, 'w'))














