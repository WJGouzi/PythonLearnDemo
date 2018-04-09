#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 方法.py
@version: 1.0
@time: 2018/4/9 10:52
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

    # 普通方法 -> 放在类中
    def bar(self):
        pass

    # 加上这个装饰器就变成了静态对象 -> 放在类中,在没有创建对象的时候依然能进行调用。
    @staticmethod
    def staticFunc():   # 这个self不是必要的(也就是这个对象不是必要的)
        print('1243')

    @staticmethod
    def staticFunc1(a1, a2):
        print(a1, a2)

    # 加上这个装饰器就变成了类方法 -> 放在类中，一般的方法需要传一个参数(除self以外的参数，便于区分)
    @classmethod
    def classMethodFunc(cls):   # 一般不写self，一般写成cls(类名)
        print(cls)
        print('class method')





obj = Foo()
obj.bar()
# Foo.bar(obj)  # 一般不使用
Foo.staticFunc()
Foo.staticFunc1(1, 3)
Foo.classMethodFunc()
