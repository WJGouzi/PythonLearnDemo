#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: json_test.py
@version: 1.0
@time: 2018/2/7 09:22
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

import json

# python是将json的所有都封装在json中

dict = {'name': 'wangjun', 'age': 24}

data = json.dumps(dict)

# 写入
with open('json_test', 'w') as f:
    f.write(data)

# 读取
with open('json_test', 'r') as f1:
    print(json.loads(f1.read()))

