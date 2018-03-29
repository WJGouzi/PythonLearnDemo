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


class secondClass:
    def __init__(self, name, age):
        '''
        这里是初始化相关的内容
        :param name: 这里的name可以进行初始化
        :param age: 这里的age可以进行初始化
        '''
        self.name = name    # -> 这里就相当于是s.name = 'ssss'
        self.age = age      # -> 这里就相当于是s.age = 12
        self.blood = 'o'    # -> 这里相当于是默认的参数(所有的类都是有的。)
    def foo(self):
        print(self.name, self.age, self.blood)

s = secondClass('wj', 12)
print(s.foo())

