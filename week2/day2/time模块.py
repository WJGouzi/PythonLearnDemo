#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: time模块.py
@version: 1.0
@time: 2018/1/30 11:39
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


import time
import datetime


############# time ##############
# print(help(time))

print(time.time())       # 拿到的就是时间戳  1517293346.276133 以秒的形式进行返回的   ********
# time.sleep(3)          #  ********
print(time.clock())      # 0.075765   这里计算的是CPU的工作时间

print(time.gmtime())     # 结构化的时间 time.struct_time(tm_year=2018, tm_mon=1, tm_mday=30, tm_hour=6, tm_min=36, tm_sec=3, tm_wday=1, tm_yday=30, tm_isdst=0) 每周的第1天 就是周二

print(time.localtime())  # 本地时间  time.struct_time(tm_year=2018, tm_mon=1, tm_mday=30, tm_hour=14, tm_min=41, tm_sec=23, tm_wday=1, tm_yday=30, tm_isdst=0)
# 取的是电脑的时间


print(time.strftime('%Y-%m-%d %H-%M-%S', time.localtime()))   # 字符串时间 将结构化时间转换成字符串的时间 2018-01-30 14-47-51    ********
structTime = time.strptime('2018-01-30 14-47-51', '%Y-%m-%d %H-%M-%S')  # 将字符串时间转换成结构化的时间
print(structTime)   # time.struct_time(tm_year=2018, tm_mon=1, tm_mday=30, tm_hour=14, tm_min=47, tm_sec=51, tm_wday=1, tm_yday=30, tm_isdst=-1)
print(structTime.tm_year)   # 2018

# 拿到的时间的三种形式：
#  时间戳   结构化时间   格式化时间

print(time.ctime())     # 默认为空 Tue Jan 30 14:55:13 2018
print(time.ctime(12341234234))    # Sun Jan 29 16:37:14 2361 将时间戳转化成一个固定格式的时间样式
print(time.mktime(time.localtime()))   # 将结构化的时间转成一个时间戳  1517295505.0

############# datetime ##############
print(help(datetime.date))
print(datetime.datetime.now())   # 2018-01-30 15:00:33.392242     ********