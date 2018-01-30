#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 迭代器.py
@version: 1.0
@time: 2018/1/30 11:17
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


# 生成器都是迭代器, 迭代器不一定是生成器

l = [1, 4, 5, 6]
# l.__iter__()
a = iter(l)  # 返回了一个迭代器对象
print(a)  # <list_iterator object at 0x101dba4a8>
for i in iter(l):
    print(i)

# 迭代器满足两个条件：
#  1.有iter()方法
#  2.有next()方法
print(next(a))  # 1

#  for循环的三件事
for i in l:
    pass
    # 将l转换成为迭代器对象
    # 将不断调用迭代器的next()方法
    # 处理StopIteration的异常

from collections import Iterator, Iterable
print(isinstance(l, Iterable))  # True 列表是可迭代
print(isinstance(l, Iterator))  # False 列表不是迭代对象
print(isinstance(a, Iterable))  # True 是否为可迭代
print(isinstance(a, Iterator))  # True 是否为迭代对象
