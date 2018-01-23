#!/usr/bin/env python
# encoding: utf-8
"""
@author: wj
@license: (C) Copyright 2013-2017.
@contact: 1693841903@qq.com
@file: 省市县三级菜单.py
@version: 1.0
@time: 2018/1/23 15:49
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

print('省市区三级菜单'.center(50, '-'))
citys = {'四川':{
                '成都': {
                        '青羊区':{},
                        '锦江区':{},
                        '武侯区':{},
                        '双流区':{}
                        },
                '德阳': {
                        '旌阳区':{},
                        '中江县':{},
                        '罗江区':{},
                        '绵竹市':{},
                        '什邡市':{},
                        '广汉市':{}
                        },
                },
         '福建':{
                '福州': {
                        '福州区':{},
                        '桥东区':{},
                        '哈哈去':{}
                        },
                '漳州': {
                        '漳浦':{},
                        '诏安':{}
                        }
                }
        }

currentCity = citys
# parentCity = citys
parentList = [] # 将保存所有的父级，最后一个元素永远都是最后一个父级

while True:
    for key in currentCity:
        print(key)
    choice = input('>>:').strip()
    if len(choice) == 0: continue
    if choice in currentCity:
        # parentCity = currentCity
        parentList.append(currentCity) # 进入到下层的时候，将当前层的父级追加到list中
        currentCity = currentCity[choice]
    elif choice == 'quit':
        # currentCity = parentCity
        currentCity = parentList.pop() if len(parentList) != 0 else citys # 当quit的时候，将取出list中的最后一个值，这就是当前层的父级。
    else:
        print('输入错误')

