#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: logging_logger.py
@version: 1.0
@time: 2018/1/31 11:25
@desc: 控制台和文件都记录日志信息
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
#  logger 控制台和文件都记录日志信息

import logging

logger = logging.getLogger()          # 创建logger对象
logger.setLevel(level=logging.DEBUG)  # 设置打印的级别
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')  # 文件输出流的对象，放到文件中去
# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()          # 标准输出流对象，放到控制台中

# 打印的格式
screenFormatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fileFormatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
# 设置打印的格式
fh.setFormatter(fileFormatter)        # 这些可以设置成一个格式。
ch.setFormatter(screenFormatter)

# logger对象添加文件输出流对象和标准输出流对象
logger.addHandler(fh)                 # logger对象可以添加多个fh和ch对象
logger.addHandler(ch)

logger.debug('logger debug message')  # 这里是logger对象进行打印日志
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')