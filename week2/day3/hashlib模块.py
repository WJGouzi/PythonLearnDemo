#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: hashlib模块.py
@version: 1.0
@time: 2018/1/31 09:54
@desc: 加密模块
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
import hashlib
# 从明文转为密文的加密模块

# MD5 和 SHA加密方法

# MD5
m = hashlib.md5()     # 拿到的是md5的哈希对象  <md5 HASH object @ 0x101c8f490>
print(m)

m.update('hello world'.encode('utf8'))
print(m.hexdigest())  #  5eb63bbbe01eeed093cb22bb8f5acdc3



# SHA
s = hashlib.sha256()        # 用的最多
print(s)

s.update('hello world'.encode('utf8'))
print(s.hexdigest())        # b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
