#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: sys模块.py
@version: 1.0
@time: 2018/1/30 17:24
@desc:  和python解释器进行交互
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

import sys

print(sys.argv)  #  argv[0] is the script pathname if known
def post():
    print('post ok')

def download():
    print('down load ok')
# if sys.argv[1] == 'post':
#     post()
# elif sys.argv[1] == 'download':
#     download()
#  在python解释器中(终端)输入 python3 sys模块.py post   或者    python3 sys模块.py download
#  这里会返回['sys模块.py', 'post']   或者    ['sys模块.py', 'download']
#  这里第一个参数是这个文件的路径，第二个参数是传入的参数
#  如果在sys.argv的第二个参数等于'post' 或者是 'download'，就会去执行相应的函数
#  以上的作用就是在函数执行中加入参数,来控制程序

print(sys.version)   #   3.6.3 (v3.6.3:2c5fed86e0, Oct  3 2017, 00:32:08)   [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)]
print(sys.platform)  # darwin

print(sys.stdout)
