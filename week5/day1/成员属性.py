#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author name__ = 'gouzi'
__create time__ = '2018/4/9'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏┓
            ┏┛┻━━━┛┻━━━┓
            ┃    ☃    ┃
            ┃  ┳┛  ┗┳  ┃
            ┃    ┻     ┃
            ┗━┓      ┏━┛
              ┃      ┗━━━━━━━┓
              ┃   神兽保佑    ┣┓
              ┃    永无BUG！ ┏┛
              ┗┓┓┏━━┳━┓ ┏━━━┛
               ┃┫┫    ┃┫┫
               ┗┻┛    ┗┻┛
"""

class Foo:

    @property               # 添加一个装饰器，就相当于是getter方法
    def per(self):
        print('per')
        return 2

    @per.setter             # 添加一个装饰器，然添加一个setter字段 -> 就相当于是给属性添加了一个setter方法
    def per(self, value):
        print(value)
        return value

    @per.deleter            # 和下面的del是成对出现的
    def per(self):
        print('delete method')


f = Foo()
p = f.per
print(p)
p = 11
print(p)
del f.per
