#!/usr/bin/env python
# encoding: utf-8
"""
@author: wj
@license: (C) Copyright 2013-2017.
@contact: 1693841903@qq.com
@file: 字符串.py
@version: 1.0
@time: 2018/1/23 11:53
@desc:
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓     ┏┓
            ┏┛┻━━━━━┛┻┓
            ┃    ☃    ┃
            ┃  ┳┛  ┗┳  ┃
            ┃    ┻     ┃
            ┗━┓     ┏━━┛
              ┃     ┗━━━┓
              ┃  神兽保佑  ┣┓
              ┃　永无BUG！  ┏┛
              ┗┓┓┏━━━━━┳┓┏┛
               ┃┫┫     ┃┫┫
               ┗┻┛     ┗┻┛
"""

## 字符串操作
# 字符串切片
a = 'hello world'
print(a[1:])                  # ello world
# 字符串片段的判断-> 关键字 in
print('ello' in a)            # True

# 字符串的品拼接
b = 'i love u'
c = a + b                     # 效率低
print(c)                      # hello worldi love u

d = ''.join([a, b])           # 比如地址的拼接的时候就会使用到这个方法
print(d)                      # hello worldi love u

e = '******'.join([a, b, d])
print(e)                      # hello world******i love u******hello worldi love u
# 将a,b,d这个三个字符串以 "*****" 进行连接

############################# 内置方法 ######################################

string = 'hello kitty'

print(string.count('l'))                 # 统计字符串中有多少个相关的字符 2   ※
print(string.capitalize())               # 首字母大写 Hello kitty
print(string.center(50,'-'))             # -------------------hello kitty--------------------   文字居左对齐，以'-'总共占位到50个  ※
print(string.ljust(50, '*'))             # hello kitty***************************************   文字居左对齐，以'*'总共占位到50个
print(string.rjust(50, '*'))             # ***************************************hello kitty   文字居右对齐，以'*'总共占位到50个
print(string.encode(encoding='utf-8'))   # b'hello kitty' 加密使用的
print(string.endswith('y'))              # 判断字符串以什么字符串进行结尾 True
print(string.startswith('H'))            # 判断字符串以什么开头  False   ※
string1 = "hello worl\tds {name} {age}"
print(string1.expandtabs(tabsize=16))    # hello worl      ds 控制制表符的宽度大小
print(string.find('l'))                  # 查找字符在字符串中是第几个位置，如果有多个相同的，以第一个为准，且将索引值进行返回 2   ※
print(string1.format(name = 'wangjun', age = 27))           # 格式化输出  hello worl	ds wangjun 27     ※
print(string1.format_map({'name' : 'wangjun', 'age':27}))   # 格式化输出 以字典进行占位 ，将string1中'{}'的内容和format中的内容进行匹配
print(string.index('l'))                 # 和find方法是差不多的，但是这个方法找不到会报错
print('abc456'.isalnum())                # 判断字符串是数字或者字母的 True
print('10'.isdecimal())                  # 判断是10进制的数
print('1245'.isdigit())                  # 判断是否为一个数字
print('123'.isnumeric())                 # 和上面是一样的
print('123abc'.isidentifier())           # 判断是否为一个正确的变量标识符 False
print('adv'.islower())                   # 是否全为小写 True
print('Dds'.isupper())                   # 是否全为大些 False
print('  '.isspace())
print('Tsdas Ssasd'.istitle())           # 是否单词首字母大写 True
print('afASFAsda'.lower())               # 将大写的变成小写     ※
print('afASFAsda'.upper())               # 将小写的变成大写     ※
print('afASFAsda'.swapcase())            # 将大小进行反转
print('    M dascc\n   '.strip())        # 将字符串中的换行符，左右的空格去掉   M dascc      ※
print('    M dascc\n   '.lstrip())       # 将字符串的左边去掉
print('    M dascc\n   '.rstrip())       # 将字符串的右边去掉
print('sdsaaa'.replace('sd','dddd', 1))  # 将字符串中的某些进行替换             ※
print('title title'.rfind('ti'))         # 从右往左进行查找 6
print('ss:ss'.split(':'))                # 分割字符串，返回一个列表             ※
a = 'aa'
b = 'bb'
c = 'cc'
d = ''.join([a, b, c])
print(d)                                 # aabbcc
print('ssssd:sdd:ssddff'.rsplit(':', 1)) # ['ssssd:sdd', 'ssddff'] 1代表分割的次数
print('as das'.title())
