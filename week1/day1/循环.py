#!/usr/bin/env python
# encoding: utf-8
"""
@author: wj
@license: (C) Copyright 2013-2017.
@contact: 1693841903@qq.com
@file: 循环.py
@version: 1.0
@time: 2018/1/22 10:36
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

# 有限循环
for i in range(1, 100):
    print('%d' % i if i % 2 == 1 else '')  # 三目运算符
for i in range(1, 101, 2):    # 2为步长
    print('num is %d' % i)

# 无限循环
counter = 0
while True:
    counter += 1
    if counter > 2**25:
        print(counter)
        break
