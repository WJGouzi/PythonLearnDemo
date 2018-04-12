#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 单例模式.py
@version: 1.0
@time: 2018/4/12 15:13
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

'''

class SingleTon:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

# 利用全局变量构造单例

instance = None
while True:
    if instance:
        instance.show()
    else:
        instance = SingleTon('wj', 12)
        instance.show()

'''


# 利用的是类方法和类的私有静态成员字段进行构造的单例
class SingleTon:

    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance:
            return cls.__instance
        else:
            cls.__instance = SingleTon('wangjun', 23)
            return cls.__instance

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 调用方法
s = SingleTon.get_instance()
s1 = SingleTon.get_instance()
print(s, s1)
