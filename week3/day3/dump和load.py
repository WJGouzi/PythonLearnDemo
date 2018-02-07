#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: dump和load.py
@version: 1.0
@time: 2018/2/7 09:47
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


# dump

import json

# python是将json的所有都封装在json中

dict = {'name': 'wangjun', 'age': 24}



# 写入
with open('json_test2', 'w') as f:
    json.dump(dict, f)     # 内部做了write方法

# 读取
with open('json_test2', 'r') as f1:
    print(json.load(f1))   # 省略了read方法