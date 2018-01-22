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
############################### 递归 #######################################
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

############################ 有限次循环(for) ##################################
_userName = 'wangjun'
_passWord = '123'
_isPassAuthentication = False
for i in range(3):
    userName = input('User name: ')
    passWord = input('Pass word: ')
    if userName == _userName and passWord == _passWord:
        print('welcome %s login' % userName)
        _isPassAuthentication = True
        break   # 跳出终端
    else:
        print('Invalid user name or password!')
if not _isPassAuthentication:
    print('您输入的次数过多')


##### 另一种写法
for i in range(3):   # 也就是相当于在for后面加了一个else语句
    userName = input('User name: ')
    passWord = input('Pass word: ')
    if userName == _userName and passWord == _passWord:
        print('welcome %s login' % userName)
        break   # 跳出终端   break之后就不会执行最后的else语句
    else:
        print('Invalid user name or password!')
else: # 只要for循环正常执行完毕，没有被打断就会执行else语句
    print('您输入的次数过多')



############################ 无限次循环(while) #################################
def whileFunction():
    count = 0
    while count < 3:
        _userName = 'wangjun'
        _passWord = '123'
        userName = input('User name: ')
        passWord = input('Pass word: ')
        if userName == _userName and passWord == _passWord:
            print('welcome %s login' % userName)
            break  # 跳出终端   break之后就不会执行最后的else语句
        else:
            print('Invalid user name or password!')
        count += 1
        # 每循环三次就判断一次要不要进行下次的输入
        if count == 3:
            keepGoingInput = input('继续输入or 完成 [y/n]:')
            if keepGoingInput == 'y':
                count = 0

    else:  # 只要while循环正常执行完毕，没有被打断就会执行else语句
        print('您输入的次数过多')
whileFunction()