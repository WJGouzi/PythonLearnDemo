#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 内置函数.py
@version: 1.0
@time: 2018/1/26 17:32
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
# import builtins
# for item in dir(builtins):
#     print(item)


#  filter函数

str = ['a', 'b', 'c', 'd']
def filterFunc(s):
    if s != 'a':
        return s

ret = filter(filterFunc, str)  #  python2返回的是一个元组，在python3中返回的是一个迭代器。
print(ret)  # <filter object at 0x104102438>
print(list(ret))  # ['b', 'c', 'd']

#  map函数
def mapFunc(s):\
    return s + 'wangjujn'
ret1 = map(mapFunc, str)
print(ret1)  # <map object at 0x103856d68>
print(list(ret1))  # ['awangjujn', 'bwangjujn', 'cwangjujn', 'dwangjujn']

#  reduce函数
from functools import reduce

def reduceFunc(x,y):
    return x + y
print(reduce(reduceFunc, range(1, 10)))  #45,这就是一个值，所有没必要放在迭代器中。


#  匿名函数
print(reduce(lambda x, y: x*y, range(1, 10)))  #  362880
