#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: os模块.py
@version: 1.0
@time: 2018/1/30 16:40
@desc: 跟操作系统进行交互
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


import os

# print(help(os))

# print(os.getcwd())   # 获取工作文件的路径 /Users/wangjun/Desktop/PythonLearnDemo/week2/day2
# print(os.chdir(r''))    # 修改文件路径
# print(os.curdir())      # 返回当前文件夹路径
# print(os.makedirs('wangjun/osTest/test'))  # 生成多层文件夹路径
# print(os.removedirs('wangjun/osTest/'))  # 删除文件夹(只能删除空的，有内容的不能进行删除)  如果上层文件夹是空的，还会删除
# os.mkdir('wangjun1')
# os.mkdir('wangjun1/ha')  # 这里需要提前创建好wangjun1这个文件夹才能创建ha文件夹
# os.rmdir('wangjun1')       # 删除单个文件夹 非空的不会被删除掉 只删除这个不会往上找
# print(os.listdir(r'/Users/wangjun/Desktop/PythonLearnDemo/week2/day2'))  # ['os模块.py', 'random模块.py', 'time模块.py', 'yield伪并发.py', '生成器.py', '迭代器.py']
# os.remove('wangjun1/ss')   # 只能删除文件，不能删除文件夹
# os.rename('wangjun1', 'wangjun')
# info = os.stat('wangjun/')
# print(info)  # os.stat_result(st_mode=16877, st_ino=5893929, st_dev=16777224, st_nlink=2, st_uid=501, st_gid=20, st_size=68, st_atime=1517303178, st_mtime=1517302912, st_ctime=1517302912)
# print(info.st_size)   # 文件的大小
# print(info.st_atime)  # 最后一次访问的时间
#
# print(os.sep)  # 取到路径拼接的分隔符  Windows是'\' Linux是'/'
# print(os.linesep)  # 换行的Windows是'\r\n' Linux是'\n' mac是'\r'
# print(os.pathsep)  # Mac ':' Windows ';'

# print(os.system("dir"))   # 32512

# print(os.path.abspath('wangjun'))   # 拿到文件的绝对路径 /Users/wangjun/Desktop/PythonLearnDemo/week2/day2/wangjun
# print(os.path.split('/Users/wangjun/Desktop/PythonLearnDemo/week2/day2/wangjun'))  # 根据最后一个分隔符进行分隔 ('/Users/wangjun/Desktop/PythonLearnDemo/week2/day2', 'wangjun')
# print(os.path.dirname('/Users/wangjun/Desktop/PythonLearnDemo/week2/day2'))  # 找到这个绝对路径的上一层路径 /Users/wangjun/Desktop/PythonLearnDemo/week2
# print(os.path.dirname(__file__))  # /Users/wangjun/Desktop/PythonLearnDemo/week2/day2
print(os.path.basename('wangjun'))  # wangjun


### 路径拼接
# os.path.join([a, b])  # 最好不要使用'+'


