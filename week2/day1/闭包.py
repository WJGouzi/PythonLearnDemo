#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 闭包.py
@version: 1.0
@time: 2018/1/29 09:58
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

# 装饰器
# 1.作用域: 根据LEGB方法进行查找（local，encluding，global，built-in）
# 2.高阶函数
#   1>函数名可以作为参数返回
#   2>函数名可以作为返回值返回
# 3.闭包
#   如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包。


def outter():
    x = 10        # 外部的作用域
    def inner():  # 条件1:内部函数
        print(x)  # 条件2:外部的环境变量
    return inner  # 结论: inner就是一个闭包

outter()()

#  关于闭包：闭包 = 函数块 + 定义函数时的一个环境