#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 反射.py
@version: 1.0
@time: 2018/4/12 11:23
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

    s = '静态成员'

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def show(self):
        return 'name: {name}, age: {age}'.format(name=self.name, age=self.age)

f = Foo('wangjun', 14)
f.name
f.show()

bn = 'name'

############## 以字符串的形式访问对象中的成员变量 ###############

# 拿出这个'wangjun' -> 以字符串的形式取到某个成员
# 1.
print(f.__dict__)
print(f.__dict__[bn])

# 2.通过getattrbute方法拿到属性值
print(getattr(Foo, 's'))
print(f.__getattribute__(bn))
print(getattr(f, bn))

# 以字符串的形式取到某个方法
ip = str(input('输入内容'))
try:
    func = getattr(f, ip)
    print(func)
    ret = func()
    print(ret)
except Exception as e:
    print('输入错误')


print(hasattr(f, 'name'))

setattr(f, 'k1', 'v1')
print(f.k1)

delattr(f, 'k1')
# print(f.k1)           # 删除后就不能进行访问了
