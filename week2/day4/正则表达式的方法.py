#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 正则表达式的方法.py
@version: 1.0
@time: 2018/2/1 10:38
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
import re

# 1.findall()
# 所有的结果都返回到一个列表中

# 2.search()
# 返回匹配到的第一个对象，对象可以调用group()方法返回结果，

# 3.match()
# 只在字符串开始匹配 和^的意义是一样的 也是返回匹配到的第一个对象，也可以调用group()返回结果
ret = re.match('res', 'ressssddasda')  # <_sre.SRE_Match object; span=(0, 3), match='res'>
print(ret.group())                     # res


# 4.split()
sp = re.split('[a, j]', 'wangjun')     # **********
print(sp)                              # ['w', 'ng', 'un']
# 分割顺序:
#  首先以'a'进行分割 -> 分割成 ['w', 'ngjun'] -> 然后以'j'进行分割 -> 将'ngjun'进行分割 -> ['w', 'ng', 'un']



# 5.sub() 替换
sb = re.sub('j..s', 'jxxb', 'wangjunssasd')      # **********
print(sb)                              # wangjxxbsasd
# 第一个的规则，第二个是需要替换成的内容，第三个是原始的字符串 -> 替换的内容是没有要求的

# 6.compile() 将正则表达式转换成一个正则表达式的对象
re.findall('\.com', 'asda.comsad')
cp = re.compile('\.com')               # 编译的规则 -> 转成了对象
print(cp)                              #
print(cp.findall('asda.comsad'))       # 直接用cp这个对象调用findall()方法，只用传入字符串参数就可以，因为是有了规则了 ['.com']
print(cp.search('asda.comsad').group())






