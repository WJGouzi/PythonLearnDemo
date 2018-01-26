#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 递归函数.py
@version: 1.0
@time: 2018/1/26 16:51
@desc:
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓     ┏┓
            ┏┛┻━━━━━┛┻┓
            ┃    ☃    ┃
            ┃  ┳┛  ┗┳  ┃
            ┃    ┻     ┃
            ┗━┓     ┏━━┛
              ┃     ┗━━━┓
              ┃  神兽保佑  ┣┓
              ┃　永无BUG！  ┏┛
              ┗┓┓┏━━━━━┳┓┏┛
               ┃┫┫     ┃┫┫
               ┗┻┛     ┗┻┛
"""

# 阶乘
def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1


print(factorial(7))


#  1.递归可以做的，循环就可以解决
#  2.效率普遍比较低（但是有特殊情况）



def fib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 1
    elif n == 0:
        return 0
    return fib(n-1) + fib(n - 2)

# 0 1 1 2 3 5 8 13 21 34
print(fib(7))


