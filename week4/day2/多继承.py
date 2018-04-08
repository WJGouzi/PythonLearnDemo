#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 多继承.py
@version: 1.0
@time: 2018/4/8 10:44
@desc: 多继承
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

class Father0:           # 父类0(基类1)
    def drink(self):
        print('喝酒0')

    def smoke(self):
        print('抽烟0')

    def makeHair(self):
        print('烫头0')


class Father(Father0):           # 父类1(基类1)
    def drink(self):
        print('喝酒1')

    def smoke(self):
        print('抽烟1')

    def makeHair(self):
        print('烫头1')


class Father2:           # 父类2(基类)
    def drink(self):
        print('喝酒2')

    def smoke(self):
        print('抽烟2')

    def makeHair(self):
        print('烫头2')




class Son(Father, Father2):
    '''
    1.多继承关系是从左往右进行继承
    2.当这条线上继承的关系找到底的时候，如果没有找到才在另一条线上继续查找继承关系
    '''
    pass
s = Son()
print(s.drink())


'''
Python支持多继承
1、一条道走到黑
2、如果有同一个根，根是最后执行的。
'''




