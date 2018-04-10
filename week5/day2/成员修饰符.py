#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 成员修饰符.py
@version: 1.0
@time: 2018/4/10 09:42
@desc: 成员修饰符->规定成 私有和共有成员
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

    # 静态的私有字段
    __hobbit = 'pennis'

    def __init__(self, name, age):
        self.name = name
        # 普通的私有字段
        self.__age = age                    # 加上'__'就将共有的成员属性变成了私有的,外部无法直接访问

    def show(self):
        print('name: %(name)s, age: %(age)d' % {'name': self.name, 'age': self.__age})
        print('name: {name}, age: {age}'.format(name=self.name, age=self.__age))            # 这种写法是比较好的
        print(Foo.__hobbit)

    @staticmethod
    def showSth():
        print(Foo.__hobbit)


    # 私有方法
    def __privateFunc(self):
        return 123

    def showPrivateFunc(self):
        r = self.__privateFunc()            # 私有方法的访问
        return r+22


p = Foo('xx', 19)
print(p.name)
# p.age   # 这是访问不了的
p.show()
Foo.showSth()
print(p.showPrivateFunc())


class Boo(Foo):
    def __init__(self, gender):
        self.gender = gender
        self.__job = 'engineer'
        super(Boo, self).__init__('wj', 12)

    def show(self):
        print(self.__job)
        print(self.name)
        print(self.gender)
        # print(self.__age)

obj = Boo('female')
obj.show()
