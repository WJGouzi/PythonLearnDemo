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
    def smoke(self):    # 重写父类中的方法, self永远指代的是自己,并不是指代的父类或者爷爷类
        print('smoke is not good')

    def makeHairSon(self):
        print('sas')
        # 调用父类中的方法
        super(Son, self).makeHair()   # 方法1：这是在自己的方法中执行继承父类的方法(推荐使用)(super是固定写法)
        Father.smoke(self)            # 方法2：这也是执行父类中方法

s = Son()

print(s.drink())
print(s.smoke())
print(s.makeHair())
print(s.makeHairSon())
