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


################################ * + ? { } 重复匹配 -> 默认是贪婪匹配  ########################################

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




################################ [] | () \  ################################################################

# [] : 字符集
# print(re.findall('a[b,s]cd','abcd'))               # ['abcd']
# # 字符集中的字符只能是选一个进行匹配
# print(re.findall('[a-z]', 'asda'))                 # ['a', 's', 'd', 'a']             '[a-z]' 表示的是a~z的所有字母的集合
# # 还可以取消一些元字符的特殊功能的匹配
# print(re.findall('[w,*]', 'ww3*'))                 # ['w', 'w', '*'] 这些 元字符都可以匹配出来 有例外的情况('\', '^', '-' 这三种特殊的不能匹配出来)
# print(re.findall('[1-9a-zA-Z]', '12asdASDAD'))     # ['1', '2', 'a', 's', 'd', 'A', 'S', 'D', 'A', 'D']
# print(re.findall('[1-9,a-z,A-Z]', '12asdASDAD'))   # ['1', '2', 'a', 's', 'd', 'A', 'S', 'D', 'A', 'D']
# print(re.findall('[^t]', 'asdaetwqrt'))            # 尖角号是除了t全部进行匹配 ['a', 's', 'd', 'a', 'e', 'w', 'q', 'r']
# print(re.findall('[^t,a]', 'asdaetwqrt'))          # 尖角号是除了t和a全部进行匹配 ['s', 'd', 'e', 'w', 'q', 'r']


# \
# 斜杠后面跟上特殊字符 去除字符的特殊功能
# 斜杠后面加上普通功能 给普通字符添加特殊功能(一部分的普通字符)
# 例如
# \d 匹配的是任何十进制的数字 -> [0-9]
# \D 匹配的是任何非数字字符  -> [^0-9]
# \s 匹配的是任何空白字符    -> [\t\r\n\f\v]
# \S 匹配的是任何的非空白字符 -> [^\t\r\n\f\v]
# \w 匹配的是任何字母数字字符 -> [0-9a-zA-Z]
# \W 匹配的是任何非字母数字字符 -> [^0-9a-zA-Z]
# \b 匹配的是与一个特殊字符的边界，也就是一个单词和特殊字符之间的位置

# 普通变为特殊字符
# print(re.findall('\d{11}', 'asd1598292552715982925527asfsg'))      # ['15982925527', '15982925527']
# # 以上的例子说明的是当匹配成功一个后，下次匹配会从上次成功处接着进行匹配
# print(re.findall('\s', 'asd1s25527 asfsg'))                        # [' ']
# print(re.findall('\w', 'as27 asfsg'))                              # ['a', 's', '2', '7', 'a', 's', 'f', 's', 'g']
# print(re.findall(r'I\b', 'I am a student LI$T'))                   # ['I', 'I']  空格和 $ 都是特殊字符
# 前面加上 r-> 这就是用正则表达式进行解释的
# print(re.findall(r'\bblow', 'blow'))     # 这是拿不到的，因为python解释中'\b'有特殊意义，所以要转义  添加r就是使用re模块，进行转义

# 将特殊的变为普通的
# ret1 = re.search('a', 'dfdfsaasd')       # 返回的是一个对象  <_sre.SRE_Match object; span=(5, 6), match='a'> 找到的是第一个位置
# print(ret1.group())                      # 匹配满足条件的第一个结果 a
# print(re.search('a.', 'adfs').group())   # ad
# # print(re.search('a\.', 'adfs').group())  # 没有匹配成功的话就调用group()方法会报错的 AttributeError: 'NoneType' object has no attribute 'group'
# print(re.search('a\.', 'a.dfs').group())  # 将'.'的适配任何字符的作用去除掉，然后就在字符串中去匹配'a.'

# \\的处理
# print(re.findall('\\\\', 'asdaD\pd'))      # ['\\']
# 首先是用python解释器进行解释'\'，所以转移成'\\'，但是在re模块中'\'也是有特殊意义的，所以也需要转义，所以将python中的'\\'交给re模块，所以转成'\\\\'
# print(re.findall(r'\\', 'aad\ss'))         # ['\\']
# 这里就告诉re模块，使用原生的，不需要python解释器，所以使用'\\'就可以了（添加了r）






# () 分组的
# print(re.findall('(as)+', 'sasdfsfsas'))     # ['as', 'as']
# ret1 = re.search('(as)+', 'sasdfsfsas')      # as
# print(ret1.group())
#
# print(re.search('(as)|3', 'asaeer323').group())  # as
# print(re.findall('(as)|3', 'as323'))             # ['as', '', '']


### 经常使用的 #######
gr = re.search('(?P<id>\d{3}):(?P<port>\w{3})', '192.168.2.215:222')
print(gr.group())               # 215:222
print(gr.group('id'))           # 215
print(gr.group('port'))         # 222
# 以上的  ?P<xxx> 是固定格式 也就是给这个组起一个名字叫xxx， 正则匹配起作用的只是  \d{3} 和 \w{3}
gr1 = re.findall('(?P<id>\d{3}):(?P<port>\w{3})', '192.168.2.215:222')
print(gr1)                      # [('215', '222')]
