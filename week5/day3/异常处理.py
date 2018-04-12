#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 异常处理.py
@version: 1.0
@time: 2018/4/12 09:55
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


# while True:
#
#     try:
#         ip = input('请输入内容:')
#         i = int(ip)
#     except Exception as e:                # Exception 可以捕捉所有的错误
#         i = 1
#         print(e)
#     print(i)

try:
    # li = [1, 4.5, 6]                      # 一旦有错误的时候，就不会执行下面的代码，就会跳转到异常处理的代码中
    # li[222]

    ip = input('请输入内容:')
    i = int(ip)
except IndexError as e:                     # IndexError是Exception的子类
    print(classmethod)
except ValueError as e:
    print(e)
except Exception as e:                      # 对某一种错误细分的时候，需要将细分的网上提，所有的错误的放在最下面
    print(e)
else:
    print('没有错')
finally:
    print('不管出错与否都是要执行的')


'''
主动抛出异常
'''

try:
    # 主动触发异常
    raise Exception('主动抛出的异常')
except Exception as e:
    print(e)


# 例子

def db():
    return False

def index():
    try:
        ret = db()
        if ret == True:
            print('数据库成功')
        else:
            print('主动抛出异常')
            raise Exception('数据库连接失败')
    except Exception as e:
        stringError = str(e)
        print(stringError)
index()



class Myerror(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

error = Myerror('自定义的错误类型')
print(error)

try:
    raise Myerror('触发自定义的错误类型')
except Myerror as e:
    print(e)                                    # 内部触发了Myerror的__str__方法



'''
断言 assert 条件 -> 如果满足就执行下面的代码，如果不满足就直接报错(一般不放在try中)
                -> 强制用户服从这个条件，可捕获错误，但是一般不捕获这个错误
'''

assert 1 == 2
print(2)