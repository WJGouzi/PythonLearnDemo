#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author name__ = 'gouzi'
__create time__ = '2018/2/4'
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
# import calculate  # 将这个模块的所有的变量以及函数加载处理后赋值给calculate

# from calculate import addCalculate   # 从模块中进行调用函数方法，这样的话节约资源。


# from calculate import *  # 将所有calculate.py中的函数和变量都引用过，尽量不要使用，这样会和自己写的方法名重复后，就不能调用模块的方法

# from calculate import addCalculate as add  # 把引用的的方法改名字

# def addCalculate(x, y):
#     return x + y +2
# print(add(1, 2))

from programModule import loggorPrint

from programModule.calculate import calculateMethod
print(calculateMethod.add(1, 3))

print(loggorPrint.logging())


# 搜索路径