#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: logging模块.py
@version: 1.0
@time: 2018/1/31 10:13
@desc: 日志
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

import logging

# 输出到控制台
# 打印日志的级别
# logging.debug('debug message')      # 没打印 级别不够
#
# logging.info('info message')        # 没打印 级别不够
#
# logging.warning('warning message')  # 默认是从warning级别开始输出
#
# logging.error('error message')
#
# logging.critical('critical message')
# critical > error > warning > info > debug > notset

# 修改级别并且修改打印日志的格式
logging.basicConfig(level=logging.DEBUG,                     # 设定的最低的日志的打印的级别
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',         # 保存的日志的时间的格式
                    # filename='test.log',                     # 打印日志保存的文件名(带着路径的文件名)   ***目前是 控制台打印和文件输出 二选一***   不写默认就输入到控制台
                    filemode='a')                            # 文件模式。写入追加模式(默认的情况)

logging.debug('debug message2')

logging.info('info message2')

logging.warning('warning message2')

logging.error('error message2')

logging.critical('critical message2')







