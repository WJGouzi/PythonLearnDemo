#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: pickle_test.py
@version: 1.0
@time: 2018/2/7 09:36
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

# 这是python自己的一种数据格式，只限于python内部自己使用。
# 数据类型就更加多了

import pickle

def printFunc():
    print('ok')

# 将函数写入到pickle文件中
data = pickle.dumps(printFunc)
with open('pickle_Test', 'wb') as f:  # 以二进制的形式写入到文件 -> 写入到文件的内容不容易阅读。所以这种方法很少使用。
    f.write(data)


# 如果这个放在其他文件的话，上面的那个函数在其他的文件也是需要存在的。
with open('pickle_Test', 'rb') as f1:  # 以二进制的形式读取文件
    func = pickle.loads(f1.read())
    func()

