#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: shelve模块.py
@version: 1.0
@time: 2018/2/7 09:52
@desc:
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓     ┏┓
            ┏┛┻━━━━━┛┻┓
            ┃    ☃    ┃
            ┃  ┳┛  ┗┳  ┃
            ┃    ┻     ┃
            ┗━┓     ┏━━┛
              ┃     ┗━━━━┓
              ┃  神兽保佑  ┣┓
              ┃　永无BUG！  ┏┛
              ┗┓┓┏━━━━━┳┓┏┛
               ┃┫┫     ┃┫┫
               ┗┻┛     ┗┻┛
"""

import shelve

# shelve逼pickle简单，就只有一个open方法，返回的是类似于字典的对象，可读可写，key值必须是字符串，value可以python的任意数据类型。
# 这个不能做任意语言的传输。
f = shelve.open('shelve_text')
f['info'] = {'name': 'wj', 'age': 23}
f['shoppingcart'] = {'price': 15, 'date': '12/12/12'}


data = f.get('info')
data1 = f.get('shoppingcart')

print(data1)