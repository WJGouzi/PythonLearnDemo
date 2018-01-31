#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 正则.py
@version: 1.0
@time: 2018/1/31 15:22
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

# 正则表达式的作用： 用来匹配字符串

# 匹配:
#


s = 'hello world'

# 找到w和l中的两个字符 是找不到的，因为字符串提供的匹配是完全匹配。因为这种需求是模糊匹配，所以是找不到的。

# 判断是不是电话号码 这也是是模糊匹配 --->>> 所以引入正则表达式

# 引入re模块 这是正则表达式的模块
import re

# ret = re.findall('w\w{2}l',s)  # 将s字符串以前面参数的规则进行匹配
# print(ret)  # ['worl']

# print(re.findall('alex', 'asda[alex]fgghrtgrsadasdwalexrwsaxzvrewdas'))  # ['alex', 'alex']
# 普通字符



# 元字符
# . ^ $ * + ? { } [ ] | ( ) \

# . 通配符
# ret = re.findall('w..l',s)  # 将s字符串以前面参数的规则进行匹配
# print(ret)
# print(re.findall('w..l', 'wh\nlsss'))  # [] 所以不能匹配换行符
# 作用: 代表的是所有的字符(除了换行符),一个'.'只能代指任意的一个字符。


# ^ 尖角符
# print(re.findall('^h...o', 'hdaslheelo'))
# 作用: 只从字符串的开始位置进行匹配

# $ 美元符
# print(re.findall('h...o$', 'hdaslheelo'))  # 'heelo']
# 作用: 只从字符串的结束位置进行匹配


# * + ? { } 重复匹配 -> 默认是贪婪匹配

# * 重复匹配  0到无穷 (推荐使用)
# print(re.findall('w*as', 'wangjunwwwwasdaswasasgjun'))  # ['wwwwas', 'as', 'was', 'as']
# * 就是重复的匹配之前的'w',重复的次数是从[0, +∞), 然后将找到的所有的元素放在列表中

# + 重复匹配  1到无穷 (推荐使用)
# print(re.findall('w+as', 'wangjunwwwwasdaswasasgjun'))  # ['wwwwas', 'was']
# + 就是重复的匹配之前的'w',重复的次数是从[1, +∞), 然后将找到的所有的元素放在列表中


# ? [0, 1]  (推荐使用)
# print(re.findall('w?as', 'wangjunwwwwasdaswasasgjun'))  # ['was', 'as', 'was', 'as']
# ? 就是匹配之前的'w',重复的次数是[0, 1], 然后将找到的所有的元素放在列表中


# {} 贪婪匹配 重复匹配
# print(re.findall('a{3}d','aaadsas'))  # ['aaad']
# 大括号中的重复匹配次数是自定义的
# print(re.findall('a{1,3}d', 'aadssadasdadsfsdaaad'))  # ['aad', 'ad', 'ad', 'aaad']
# 匹配次数为1~3次，且不能有空格
# 如果是{1,} 这代表的是 1~+∞匹配


# 结论
# * = {0,+∞}
# + = {1,+∞}
# ? = {0,1}





# [] : 字符集
print(re.findall('a[b,s]cd','abcd'))  # ['abcd']
# 字符集中的字符只能是选一个进行匹配
print(re.findall('[a-z]', 'asda'))    # ['a', 's', 'd', 'a']             '[a-z]' 表示的是a~z的所有字母的集合
# 还可以取消一些元字符的特殊功能的匹配
print(re.findall('[w,*]', 'ww3*'))    # ['w', 'w', '*'] 这些 元字符都可以匹配出来


