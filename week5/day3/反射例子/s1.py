#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: s1.py
@version: 1.0
@time: 2018/4/12 14:34
@desc:  getattr在模块中的使用方式
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
import s2

r1 = s2.NAME
r2 = s2.Func()
print(r1)
print(r2)


print(getattr(s2, 'NAME'))
print(getattr(s2, 'Func')())

cls = getattr(s2, 'Foo')
obj = cls()
print(obj.name)


