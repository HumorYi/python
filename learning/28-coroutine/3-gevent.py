#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/12/17 15:19
@Description: 协程 - gevent

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/12/17 15:19
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

"""
import gevent


def func1():
    print('\033[31;1m李闯在跟海涛搞...\033[0m')
    gevent.sleep(2)
    print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m')


def func2():
    print('\033[32;1m李闯切换到了跟海龙搞...\033[0m')
    gevent.sleep(1)
    print('\033[32;1m李闯搞完了海涛，回来继续跟海龙搞...\033[0m')

# spawn 大量生产
gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2)
])
"""

import gevent, time
from gevent import monkey
from urllib.request import urlopen

monkey.patch_all()

start = time.time()


def f(url):
    print('GET: %s' % url)
    # 爬取链接数据
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))


urls = ['https://www.python.org/', 'https://www.yahoo.com/', 'https://github.com/']
tasks = []

for url in urls:
    # f(url)
    tasks.append(gevent.spawn(f, url))

gevent.joinall(tasks)
end = time.time()
print('time is %s' % (end - start))
