#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 特殊成员.py
@version: 1.0
@time: 2018/4/10 15:06
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
class Foo:
    def __init__(self):
        print('some thing')

    def __call__(self, *args, **kwargs):        # 添加一个__call__(xxx)
        print('对象自动执行')

    def __int__(self):
        return 111

    def __str__(self):
        return 'wangjun'


obj = Foo()
obj()                                           # 默认是不执行的，添加以后就可以执行。



# 将Foo类型转化成int类型的需求
# 只要在int(对象)，就会自动去执行__int__方法，并且将返回值自动返回给int对象。
ret = int(obj)
print(ret)

s = str(obj)                                    # 用的比较多
print(s)


# 例子 -> 将对象的一些信息转换成一个字符串，便于展示相关的信息给用户
class Boo:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __str__(self):
        return 'name : {name}, age : {age}'.format(name=self.name, age=self.__age)

b = Boo('wangjun', 13)
print(b)                    # 内部类似于执行了str(b)并将返回值拿到
print(str(b))

