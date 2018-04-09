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

class PageFunction:

    def __init__(self, currentPage):
        try:
            p = int(currentPage)
        except Exception as e:
            p = 1
        self.page = p

    @property
    def start(self):
        return (self.page - 1) * 10

    @property
    def end(self):
        return self.page * 10


li = []
for i in range(1001):
    li.append(i)
while True:
    p = input('请输入页码:')
    obj = PageFunction(p)
    try:
        if li[obj.start:obj.end] == []:
            print(li[0:9])
        else:
            print(li[obj.start:obj.end])
    except Exception as e:
        print(li[0:9])

