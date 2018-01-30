#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: yield伪并发.py
@version: 1.0
@time: 2018/1/30 11:01
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
import time
def consumer(name):
    print("%s 准备吃包子啦!" % name)
    while True:
       baozi = yield
       print("包子[%s]来了,被[%s]吃了!" % (baozi, name))

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()  # 生成了生成器
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(0.5)
        print("做了2个包子!")
        c.send(i)
        c2.send(i)

producer("alex")