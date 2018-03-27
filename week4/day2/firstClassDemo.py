#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '第一个面向对象的demo'
__author name__ = 'gouzi'
__create time__ = '2018/3/27'
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

class firstClass:
    def foo(self, name):
        print(name)

    def boo(self, age):
        print(age)
        return age

    def poo(self, arg):
        print(self, self.gender, arg)

obj = firstClass()
obj.foo('wangjun')


age = obj.boo(12)
print('return %d' % age)


# 在对象中存放内容
obj.gender = 'male'
p = obj.poo('hah')
print(p)
