#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 函数.py
@version: 1.0
@time: 2018/1/26 09:17
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



def showInfo(name, age):
    print('name is %s' % name)
    print('age is %d' % age)

# 关键参数
showInfo('wangjun', 27)
    # name is wangjun  age is 27
#  没有关键字的时候就需要按照位置进行传入参数

# 关键字参数
showInfo(age=16, name='wangjun')
    # name is wangjun  age is 27
#  如果有关键字传入的时候，位置就不重要了，只要对应传入的参数类型匹配就可以了。

# 默认参数
def showStudentInfo(name, age, gender='boy'):
    # 默认参数一定要放在参数的后面
    print('%s is %d years old %s' % (name, age, gender))

showStudentInfo('wangjun', 24)  # wangjun is 24 years old boy
showStudentInfo('wang', 18, 'girl')  # wang is 18 years old girl
#  当调用的时候如果没有传入默认参数的时候，函数的就会使用自己定义好的默认参数。
#  当调用函数的有默认参数，那就修改掉函数的默认参数，传入调用函数中默认的实参。


# 可变参数
# 例子1 -> 将参数转成元组
def add(*args):
    print(args) #  -> 将传入进来的参数变成一个元组
    num = 0
    for i in args:
        num += i
    print(num)
add(1)  # 1
add(1,4,5)  # 10


# 例子2 -> 将参数转为字典
def func(name, age, gender = 'boy', *args, **kwargs):
    print('%s is %d years old %s -- %s  :  %s' % (name, age, gender, args, kwargs))

func('wangjun', 26, 'boy', 12345,33, job = 'IT', hobbit = 'girls')

# 参数位置的顺序：
#   关键字参数 -> 默认参数 -> 可变参数

