#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 多继承的例子.py
@version: 1.0
@time: 2018/4/8 15:25
@desc: 例子
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

class BaseHandler:
    def __init__(self):
        print('base handler!')                                  # step 3

class BaseRequestHandler(BaseHandler):
    def __init__(self):
        print('base request handler!')                          # step 2
        BaseHandler.__init__(self)

    def serverHandler(self):
        print('base request handler server handler!')           # step 5
        self.proccessRequest()

    def proccessRequest(self):
        print('base request handler proccess request!')



class MinX:
    def proccessRequest(self):
        print('Minx proccess request handler')                  # step 6

class Request(MinX, BaseRequestHandler):
    pass

r = Request()                                                   # step 1(执行的步骤)
r.serverHandler()                                               # step 4