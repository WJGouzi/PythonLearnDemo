#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author name__ = 'gouzi'
__create time__ = '2018/4/10'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏┓
            ┏┛┻━━━┛┻━━━┓
            ┃    ☃    ┃
            ┃  ┳┛  ┗┳  ┃
            ┃    ┻     ┃
            ┗━┓      ┏━┛
              ┃      ┗━━━━━━━┓
              ┃   神兽保佑    ┣┓
              ┃    永无BUG！ ┏┛
              ┗┓┓┏━━┳━┓ ┏━━━┛
               ┃┫┫    ┃┫┫
               ┗┻┛    ┗┻┛
"""

class Foo:

    def __init__(self, age, name):
        self.name = name
        self.age = age

    def __add__(self, other):
        # self = p1
        # other = p2
        print('name : {name}, age : {age}'.format(name=self.name, age=self.age))
        # return self.age + other.age
        return Foo(self.age + other.age, self.name + other.name)

    def __del__(self):
        # 这是在类被销毁的时候进行调用
        print('这是由python内部自动调用的')


p1 = Foo(19, 'wang')
p2 = Foo(20, 'jun')

p3 = p1 + p2
# 两个对象相加的时候，会自动的执行第一个对象的__add__方法，然后将第二个对象作为参数传入到函数中(other形参)
print(p3.name, p3.age, p3, type(p3))
# 其余加减乘除是一样的


class Boo:
    '''
    这是注释，会将注释也当成类的成员。
    '''

    def __init__(self, age, name):
        self.name = name
        self.age = age

b = Boo(11, 'kj')
d = b.__dict__
print(d)
print(Foo.__dict__)


# li = [11, 22, 33, 44, 55]
# r1 = li[3]
# li[2] = 222
# del li[1]

class ListClass:

    def __init__(self, age, name):
        self.name = name
        self.age = age

    def __getitem__(self, item):
        '''
        如果item是int类型就代表这个是索引
        如果item是slice对象就代表这个要切片
        :param item: 传入的参数
        '''
        if isinstance(item, int):
            print('这是索引处理')
            return item + 10
        elif isinstance(item, slice):
            print('这是切片处理')
            print(item)
            return 11

    def __setitem__(self, key, value):
        print(key, value)

    def __delitem__(self, key):
        print(key)


li = ListClass(22, 'wjj')
r = li[8]                       # 自动执行li对象中的__getitem__方法，将8当做参数传给item，且需要将结果返回
print(r)
li[3] = 10                      # 自动执行li对象中的__setitem__方法，key = 3, value = 10作为参数传入到方法中，且不需要返回值
del li[11]                      # 自动执行li对象中的__delitem__方法，key = 11作为参数传入到方法中,并且不需要返回值

li[1:3:1]                       # 在python2.x中执行的是__slice__方法，但在python3.x中执行还是__getitem__方法
                                # 这里传入的参数就是一个slice对象，所以在python3.x中需要对这个参数进行判断
                                # 如果是int类型就代表是索引，如果是slice对象就代表要切片
                                # 以上的处理方式可以用到__setitem__和__delitem__方法中
