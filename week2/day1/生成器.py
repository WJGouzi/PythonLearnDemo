#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author name__ = 'gouzi'
__create time__ = '2018/1/29'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏┓
            ┏┛┻━━━┛┻━━━┓
            ┃    ☃    ┃
            ┃  ┳┛  ┗┳  ┃
            ┃    ┻     ┃
            ┗━┓      ┏━┛
              ┃      ┗━━━━━━━┓
              ┃   神兽保佑    ┣┓
              ┃    永无BUG！ ┏┛
              ┗┓┓┏━━┳━┓ ┏━━━┛
               ┃┫┫    ┃┫┫
               ┗┻┛    ┗┻┛
"""

# 生成器
s = (x for x in range(3))
print(s)  # <generator object <genexpr> at 0x10401cf10>
# print(s.__next__())  # 0->尽量不使用这些方法
# print(next(s))  # 1 -> 等价于上面的方法
# print(next(s))  # 2
# print(next(s))  # StopIteration 超出的就报错了


for i in s:       # -> 就是在s中一直调用next()函数
    print(i)      # 0,1,2


# 生成器本身就是一个可迭代对象

# 可迭代对象
# 就是对象中有__iter__()方法，就是可迭代的对象


# 生成器的创建方式
# 1. s = (x for x in range(3))
# 2. yield
def foo():
    print('ok')
    yield 1

    print('ok2')
    yield 2


foo()  # 这里不在执行程序，是因为没有进入到函数内部
#  只要加上'yield'关键字，就代表是创建了一个生成器对象

print(foo())  # <generator object foo at 0x101efcf10> 没有打印里面的文字
g = foo()
a = next(g)  # ok
b = next(g)  # ok2
print(a)  # 1
print(b)  # 2
# 下次进入的时候会从上次跳出的地方继续执行。如果超出了yield的次数会报错

for i in foo():
    print(i)  # i= 1，2
    # 1
    # 2


##  斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for i in fib(10):
    print(i)