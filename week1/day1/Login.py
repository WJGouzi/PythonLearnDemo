#!/usr/bin/env python
# encoding: utf-8
"""
@author: wj
@license: (C) Copyright 2013-2017.
@contact: 1693841903@qq.com
@file: Login.py
@version: 1.0
@time: 2018/1/22 10:37
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

def login():
    _userName = 'wangjun'
    _passWord = '123'
    userName = input('User name: ')
    passWord = input('Pass word: ')
    if userName == _userName and passWord == _passWord:
        print('welcome %s login' % userName)
    else:
        print('Invalid user name or password!')
        login()

# login()

#循环
for i in range(1, 100):
    print('%d' % i if i % 2 == 1 else '')  # 三目运算符
for i in range(1, 101, 2):    # 2为步长
    print('num is %d' % i)

