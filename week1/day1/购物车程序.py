#!/usr/bin/env python
# encoding: utf-8
"""
@author: wj
@license: (C) Copyright 2013-2017.
@contact: 1693841903@qq.com
@file: 购物车程序.py
@version: 1.0
@time: 2018/1/22 16:13
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
import sys
import functools
salary = input('salary = ')
goodsList = ['iphone6s', 'mac book', 'coffee', 'python book', 'bicycle']
goodsPriceList = [5800, 9000, 32, 80, 1500]
for value in goodsList:
    index = goodsList.index(value)
    print("%d. %s %d" % (index + 1, value, goodsPriceList[index]))

salary = int(salary.split('= ')[-1])
buyGoodsList = []
buyGoodsPricerList = []
while salary > 0:
    inputNum = input('>>>:')
    inputChar = inputNum.split(':')[-1]
    if inputChar.isdigit():
        index = int(inputChar)
        price = goodsPriceList[index - 1]
        if salary < price:
            print('余额不足, %d' % (salary - price))
        else:
            salary -= price
            print('已加入%s到购物车,当前余额%d' % (goodsList[index - 1], salary))
            buyGoodsList.append(goodsList[index -1])
            buyGoodsPricerList.append(price)
    else:
        if inputChar == 'quit':
            print('您以购买以下商品:')
            for value in buyGoodsList:
                print('%s %d' % (value, buyGoodsPricerList[buyGoodsList.index(value)]))
            print('您的余额为:%d' % salary)
            print('欢迎下次光临')
            break
        else:
            print('请输入正确的命令')
# else:
#     print(buyGoodsList)
