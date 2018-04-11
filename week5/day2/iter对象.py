

#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: iter对象.py
@version: 1.0
@time: 2018/4/11 09:29
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

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __iter__(self):
        print('iter方法')
        return iter((self.name, self.age))


li = Foo('wangjun', 19)
# 0.如果类中有__iter__方法，那么这个对象则是可迭代对象
# 如果for循环遇到的是迭代器，那么直接执行__next__方法
# 如果for循环遇到的是可迭代对象，那么会执行对象.__iter__，生成迭代器后执行__next__方法
# 1.执行li对象的类Foo中的__iter__方法，并且获取返回值(这个返回值必须是可迭代的)
# 2.循环上一步得到的返回值
for i in li:
    print(i)