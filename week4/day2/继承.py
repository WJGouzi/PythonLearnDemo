#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '继承'
__author name__ = 'gouzi'
__create time__ = '2018/3/29'
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

class Father:           # 父类(基类)
    def drink(self):
        print('喝酒')

    def smoke(self):
        print('抽烟')

    def makeHair(self):
        print('烫头')

class Son(Father):      # 子类(派生类)
    def xxoo(self):
        print('xxoo')
    def smoke(self):
        print('smoke is not good')


s = Son()

print(s.drink())
print(s.smoke())
print(s.makeHair())

