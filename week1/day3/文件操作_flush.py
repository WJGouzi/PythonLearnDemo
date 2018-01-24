#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 文件操作_flush.py
@version: 1.0
@time: 2018/1/24 16:01
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
# flush 遍历文件的方法
# 就是边写边存
# import sys, time
# for i in range(30):
#     print('',end='*',flush=True)
#     time.sleep(.1)

# file = open('洛神赋1','a')
# file.truncate(5) # 从光标处开始截断
# file.write('asdasd')
# print(file.fileno()) # 3 拿到文件的编号
# print(file.isatty()) # 是否为终端 False
# file.close()



################# r+ ####################
# file = open('洛神赋','r+') ***
# print(file.readline())
# print(file.write('hah')) # 照常读取，读取之后会在最后的位置进行添加
# file.close()

################# w+ ####################
# file = open('洛神赋1','w+') # 先清空 *
# print(file.readline())     # 没内容
# print(file.write('hah'))   # 光标在hah之后
# print(file.readline())     # 依然没有内容
# file.seek(0)               # 移动光标回到首位
# print(file.readline())     # 可以读取了 hah
# file.close()

################# a+ ####################
# file = open('洛神赋1','a+')
# print(file.tell()) # 8
# file.write('\nasda')
# print(file.tell()) # 13
# print(file.readline())
# file.close()

###########  修改硬盘中的内容(理论上是不能完成的) #############
file = open('洛神赋', 'r+')
file1 = open('洛神赋1', 'w') #
num = 0
for line in file:
    num += 1
    # file.write('i like it' if num == 2 else '') # 不能完成 因为添加数据只能添加到文件的最后。
    line = ' '.join([line.strip(), 'i like it']) if num == 2 else line.strip()  # 取出文件1的内容
    file1.write(''.join([line, '\n'])) # 一行行的写入到文件2中去
file.close()
file1.close()


