#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: metaClass元类.py
@version: 1.0
@time: 2018/4/12 09:08
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

class myTpye(type):

    def __init__(self, *args, **kwargs):
        super(myTpye, self).__init__(*args, **kwargs)
        print('执行的是myType的__init__方法')


    def __call__(self, *args, **kwargs):
        print('执行的是myType的__call__方法')
        ret = self.__new__(self, *args, **kwargs)
        self.__init__(ret)


class Foo(object, metaclass=myTpye):                        # 不去由type创建，而由mytype进行创建

    def __init__(self):
        print('执行的是Foo的__init__方法')
        print('Foo的对象创建完成')


    def __new__(cls, *args, **kwargs):
        print('真正的创建这个Foo类的对象')
        return object.__new__(cls, *args, **kwargs)


    def __call__(self, *args, **kwargs):
        print('执行的是Foo的__call__方法')
        return self.__init__(self.__new__(self, *args, **kwargs))


    def bar(self, *args, **kwargs):
        self.__call__(self, *args, **kwargs)
        print(12343)


####################

# def bar1(self):
#     print('123')

# Boo = type('Boo', (object,), {'func': bar1})                # 申明了一个类
# Boo1 = type('Boo1', (object,), {'func': lambda x: 33})      # Boo和Boo1同样是对象，是type的对象

f = Foo()                                                     # 首先执行的是myType的__init__，然后执行__call__方法
f.bar()

# b = Boo1()
# b.bar1()
