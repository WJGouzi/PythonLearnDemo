#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 单例的例子.py
@version: 1.0
@time: 2018/4/12 15:36
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

import tornado.ioloop
import tornado.web

class mainHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        import time
        self.write('现在的时间戳为: ' + str(time.time()))
        self.write('haha')

application = tornado.web.Application([(r"/index", mainHandler)])

try:
    if __name__ == "__main__":
        application.listen(8888)
        tornado.ioloop.IOLoop.instance().start()
except KeyboardInterrupt as e:
    print('关闭了网页')
