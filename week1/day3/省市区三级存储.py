#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author name__ = 'gouzi'
__create time__ = '2018/1/24'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏┓
            ┏┛┻━━━┛┻━━━┓
            ┃    ☃    ┃
            ┃  ┳┛  ┗┳  ┃
            ┃    ┻     ┃
            ┗━┓      ┏━┛
              ┃      ┗━━━━━━━┓
              ┃   神兽保佑    ┣┓
              ┃    永无BUG！ ┏┛
              ┗┓┓┏━━┳━┓ ┏━━━┛
               ┃┫┫    ┃┫┫
               ┗┻┛    ┗┻┛
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


cityFile = open('citys','w+')
cityFile.write(str(citys))
cityFile.seek(0)
cityDict = eval(cityFile.read())
parentList = []
addList = [] # 增加的添加在列表中。
while True:
    for key in cityDict:
        print(key)
    choose = input('>>>:').strip()
    if len(choose) == 0: continue
    if choose in cityDict:
        parentList.append(cityDict)
        cityDict = cityDict[choose]
    elif choose == 'quit':
        cityDict = parentList.pop() if len(parentList) != 0 else cityDict
        # break
    elif choose == 'add': # 增加的功能
        addCity = input('addCity>>>:').strip()
        cityDict[addCity] = {}
        addList.append(cityDict)
        cityFile.seek(0)
        cityFile.write(str(parentList[0]) if len(parentList) != 0 else str(cityDict))
        cityFile.flush()
        # print(addList)
    else:
        print('输入不正确')
cityFile.close()
