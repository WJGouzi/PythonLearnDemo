#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: with语句.py
@version: 1.0
@time: 2018/1/25 14:07
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

#  文件的处理中的with语句

# file = open('洛神赋','r')

# 推荐使用的方法
# with open('../day3/洛神赋','r') as file: # './' 代表的是当前的文件夹的层级 '../' 代表的上一层文件夹的层级
#     file.readline()
#     print(file.readlines())
#     这里不需要添加file.close()方法，退出这个代码块就会自动关闭这个文件

# 同时在一个代码块中进行读写操作 -> with 同时管理多个文件对象。
with open('../day3/洛神赋','r') as readfile, open('洛神赋', 'w') as wirtefile:
    for line in readfile:
        wirtefile.write(line)
        # 将day3中的文件的所有内容写入到一个新的文件中去。


import copy
a = [[1, 2], 3, 4]
b = copy.deepcopy(a)
b[0][0] = 5
print(a)
print(b)
