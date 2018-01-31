#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 文件操作.py
@version: 1.0
@time: 2018/1/24 10:29
@desc: 文件操作\\\\\用于存储数据->作用类似于数据库
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
# 文件操作的流程
# 1.拿到文件的操作句柄(也就是文件对象）
# 2.对文件进行操作
# 3.关闭文件->如果不进行操作的话，是不安全的-->

##### 读操作 ####
# #1.创建文件操作的句柄
# file = open('洛神赋','r')
# #2.读
# fileData = file.read(5)  # 取的是5个字符
# print(fileData)
# #3.关闭文件
# file.close()

##### 写操作 ####
# file2 = open('洛神赋1','w')      # 当文件存在的时候，如果是进行写操作的话，就会将存在的文件进行清空，如果不存在就会去创建1个文件
# file2.write('hello world\n')    # 会将数据写入到文件中去。
# file2.write('hello world  111') # 会将数据拼接到文件的最后面去
# file2.close()                   # 这里会将缓存区中的数据写入到磁盘中，也就是说在文件关闭后，才会就将数据写入到文件内。


#### 追加内容 ####
# file3 = open('洛神赋1','a')
# file3.write('\n添加的字符\n') # 会将数据写入到文件中去。
# file3.write('hello world ') # 会将数据拼接到文件的最后面去
# file3.close()



file = open('洛神赋','r')
# 读取一行
# print(file.readline()) # '寥落古行宫，宫花寂寞红。' 读取后会把换行符进行打印
# print(file.readline()) # '白头宫女在，闲坐说玄宗。' 读取上一行后，光标移动到了第一行的最后，所以再次readline的时候会从第二行开始
# 读取所有行
# print(file.readlines()) # ['寥落古行宫，宫花寂寞红。\n', '白头宫女在，闲坐说玄宗。\n', '白日依山尽，黄河入海流。\n', '欲穷千里目，更上一层楼。']

# 需求  将第2行加入一个字符串
# num = 0
# for line in file.readlines():
#     num += 1
#     # print(line.strip())   # strip会把每个字符串的换行符进行删除
#     print(line.strip() + 'i like it' if num == 2 else line.strip())
# file.close()
print(''.join(['type is :', str(type(file))]))
####### 一般推荐使用的方法 **************************************************************
# for line in file:  # 这是for内部将对象做成了一个迭代器，用一个去取一个。这里就是用一行就去取一行
#     num += 1
#     print(line.strip() + 'i like it' if num == 2 else line.strip())
# file.close()

###  遍历器进行遍历
# for index, value in enumerate(file.readlines()):
#     print('--'.join([str(index), ' '.join([value.strip(), 'i like it'])]) if index == 2 else '--'.join([str(index), value.strip()]))
# file.close()


### 光标位置的检测
print(file.tell())    # 0
print(file.read(5))   # 寥落古行宫  -->> 中文在UTF-8中占3个字符
print(file.tell())    # 15
### 调整光标位置
print(file.seek(0))   # 0 -> 可以用于断点续传的功能
print(file.read(7))   # 寥落古行宫，宫
file.close()