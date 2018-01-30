#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 生成器.py
@version: 1.0
@time: 2018/1/30 09:57
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
# 生成器就是一种特殊的生成器

# yield
def fib(maxNum):
    n, a, b = 0, 0, 1
    while n < maxNum:
        yield a # 执行到这里，就会退出，退出之前会保存状态，然后下次进入的时候从这里开始
        a, b = b, a + b
        n += 1

print(fib(8))
for i in fib(8):
    # print(i)
    pass
g = fib(8)


#

def bar():
    print('ok1')
    count = yield 1
    print('count is %s' % count)

    print('ok2')
    string = yield 2
    print('string is %s' % string)

b = bar()
# next(b)        # 进入到bar函数中
b.send(None)     # 作用是和next()函数是一致的。如果进入函数之前没有next()函数，那么就只能使用send(None)函数，就相当于是next()函数。
b.send(122)      # 同样和next()一样可以进入到函数，但是可以给yield进行赋值。count is 122

#  流程：
#  创建生成器 -> b.send(None) 进入到函数 -> print('ok1') -> yield 1返回 -> b.send(122) 传给yield1,也就是count=1 -> print('ok2') -> yield 2返回 -> 程序执行完毕，后续的不再进行。


