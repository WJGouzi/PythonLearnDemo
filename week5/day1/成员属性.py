#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author name__ = 'gouzi'
__create time__ = '2018/4/9'
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

    # 第一种成员属性的写法
    @property               # 添加一个装饰器，就相当于是getter方法
    def per(self):
        print('per')
        return 2

    @per.setter             # 添加一个装饰器，然添加一个setter字段 -> 就相当于是给属性添加了一个setter方法
    def per(self, value):
        print(value)
        return value

    @per.deleter            # 和下面的del是成对出现的
    def per(self):
        print('delete method')


    # 成员属性另一种写法(getter方法)
    def f1(self):
        return 123
    perr = property(fget=f1)  # 等同于上面加上@property装饰器的写法

    def f2(self, value):
        print(value)
        # return value
    perr1 = property(fset=f2)

    def f3(self):
        print('delete')

    perr2 = property(fget=f1, fset=f2, fdel=f3, doc='这个是注释')

# 第一种成员属性的调用方式
f = Foo()
p = f.per
print(p)
p = 11
print(p)
del f.per


# 另一种成员属性的调用方式
fo = Foo()
pr = fo.perr
print(pr)
pr = 212
print(pr)
print(fo.perr2)
fo.perr2 = 12112
del fo.perr2

