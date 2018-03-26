#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 装饰器.py
@version: 1.0
@time: 2018/1/29 14:11
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
#  封闭开放原则
#  对修改封闭，对扩展开放

import time
def foo():
    print('foo.....')
    time.sleep(1)

#  拓展功能
def showTime(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print('spend time is %s' % (end - start))
    return inner

foo = showTime(foo)  # 进行装饰。
foo() # 原始的功能不进行修改，添加新的功能。


#  简便的写法
@showTime   #  bar = showTime(bar)
def bar():
    print('bar.....')
    time.sleep(2)
bar()


#  功能函数加参数的情况
def addFunc(*a, **b):
    # print('a + b = %s' % (a + b))
    sum1 = 0
    for i in a:
        sum1 += i
    print('sum = %s' % sum1)
    time.sleep(1)


def showTimeFunc(f):
    def inner(*x, **y):
        start = time.time()
        f(*x, **y)
        end = time.time()
        print('spend time is %s' % (end - start))
    return inner


addFunc(1, 3, 4, 5)


#  装饰器函数加参数 -> 就相当于是给装饰器再次嵌套
def showTimeWithLog(text='false'):
    print('text is ' + text)
    def showTimeFunc(f):
        def inner(*x, **y):
            start = time.time()
            f(*x, **y)
            end = time.time()
            print('spend time is %s' % (end - start))
            if text == 'true':
                print('打印日志')
            else:
                print('yes')
        return inner
    return showTimeFunc

@showTimeWithLog('true')   # 先执行的是showTimeWithLog函数，然后返回的是ShowTimeFunc
def func():
    print('\nfunc.....')
    time.sleep(2)
func()

@showTimeWithLog()
def printf():
    print('\nprintf.....')
    time.sleep(1)
printf()
