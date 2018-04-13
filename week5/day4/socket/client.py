#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: client.py
@version: 1.0
@time: 2018/4/13 10:21
@desc: 客户端
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
import socket

sk = socket.socket()
addr = ('127.0.0.1', 8800)
sk.connect(addr)
print(sk)
'''
<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 51463), raddr=('127.0.0.1', 8800)>
'''

# 接收消息
# data = sk.recv(1024)
# decodeData = str(data, 'utf8')
# print(decodeData)

# 发送消息
inp = str(input('输入内容:'))
inpData = bytes(inp, 'utf8')
sk.send(inpData)          # send和recv中传入的参数一定是byte值
sk.close()
print(sk)                 # <socket.socket [closed] fd=-1, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>
