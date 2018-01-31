#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: configParser模块.py
@version: 1.0
@time: 2018/1/31 14:14
@desc:配置文件
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
import configparser

config = configparser.ConfigParser()
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9'}
#
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'  # mutates the parser
# topsecret['ForwardX11'] = 'no'  # same here
# config['DEFAULT']['ForwardX11'] = 'yes'
#
# with open('example.ini', 'w') as configfile:
#     config.write(configfile)

# 读取文件
config.read('example.ini')  # 关联文件对象
# print(config.sections())    # 默认的是不会读取出来的 ['bitbucket.org', 'topsecret.server.com']
# print(config.defaults())    # 返回的是有序的字典  OrderedDict([('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'), ('forwardx11', 'yes')])
# print('bitbucket.org' in config)          # True
# print(config['bitbucket.org']['User'])    # hg
# print(config.has_section('bitbucket.org'))  # True


# 遍历config中的key
# for key in config:
    # print(key)
    # DEFAULT
    # bitbucket.org
    # topsecret.server.com

# for key in config['bitbucket.org']:
    # print(key)
    # user
    # serveraliveinterval
    # compression
    # compressionlevel
    # forwardx11
    # 这里是有特殊情况。首先将 'bitbucket.org' 下的键进行遍历，然后再讲default中的键进行打印。

# for key in config.defaults():
#     print(key)
#     # serveraliveinterval
#     # compression
#     # compressionlevel
#     # forwardx11


# 删除大项
# config.remove_section('topsecret.server.com')
# config.write(open('example1.ini', 'w'))  # 这里是必然的步骤，因为文件一旦写定了就不能进行修改了，所以需要重新生成文件进行记录。
# config.write(open('example.ini', 'w'))   # 这里是将之前的文件进行覆盖，并不是修改。

# 删除某一个模块下的键
config.remove_option('bitbucket.org', 'user')
config.write(open('example1.ini', 'w'))   # 这里是将之前的文件进行覆盖，并不是修改。


# 修改
config.set('bitbucket.org', 'user', 'wangjun')
config.write(open('example.ini', 'w'))   # 这里是将之前的文件进行覆盖，并不是修改。
