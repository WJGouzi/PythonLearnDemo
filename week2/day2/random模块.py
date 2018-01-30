#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: random模块.py
@version: 1.0
@time: 2018/1/30 15:02
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
import random
# 创建随机数
print(help(random))
print(random.random())  # 限定到0~1
print(random.randint(1, 5))  # [1, 5] 之间的整数的随机数
print(random.choice('wangjun'))  # 字符串中的随机字符


l = [1, 23, 4, 5, 6]
print(random.choice(l))
print(random.sample(l,2))   # 随机在l列表中找2个值
print(random.randrange(1, 5))   # [1, 5) 之间的整数的随机数

### 随机生成一个验证码
def modifyFunc():
    code = ''
    for i in range(5):
        # addNum = random.randrange(10)
        # addAlpha = chr(random.randrange(97, 123))
        # if i == random.randint(0,4):
        #     code += str(addNum)
        # else:
        #     code += str(addAlpha)
        code += str(random.choice([random.randrange(10), chr(random.randrange(97, 123))]))  # mp475
    print(code)
    return code
modifyFunc()   # bux4k

print(chr(122)) # 将ASCII码转为字母