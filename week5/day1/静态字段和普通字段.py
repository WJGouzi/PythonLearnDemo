#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 静态字段和普通字段.py
@version: 1.0
@time: 2018/4/9 10:05
@desc:  静态字段和普通字段
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

class Province:
    # 静态字段 -> 保存在类中的(属于类)
    country = '中国'

    def __init__(self, name):
        # 普通字段 -> 保存在对象中(属于对象)
        self.name = name

print(Province.country)
# print(Province.name)   # 这个是不能执行的
sichuan = Province('四川')
print(sichuan.name)
print(sichuan.country)   # 执行时可以通过类访问，也可以通过对象进行访问
