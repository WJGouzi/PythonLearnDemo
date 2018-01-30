#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author name__ = 'gouzi'
__create time__ = '2018/1/29'
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

# 列表生成式
l = [x for x in range(10)]
print(l)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

t = [x * x for x in range(10)]
print(t)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 先到for循环中取元素，取完元素在进行运算，运算完成再放到列表中。


def func(n):
    return n * n * n
f = [func(a) for a in range(10)]
print(f)  # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]


# 简单的赋值方式
T = ('123', 3)
a, b = T  # 元组有几个元素，就用几个变量进行接收。
print('a = %s, b = %d' % (a, b))  # a = 123, b = 3

