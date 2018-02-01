#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 正则计算器.py
@version: 1.0
@time: 2018/2/1 11:26
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
import re

s = '1 - 2 * ( (60-30 +(-40/5-3) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
s1 = '1+2 * (5 * (1+2) + (3/2)) + (1+3) * 3'
# 去除字符串中的空格
def stripBlank(s):
    sb = re.sub(' ', '', s)
    # print(sb)               # 1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))
    return sb

# 检测字符串中有无字母
def checkAlphaInString(s):
    cha = re.findall('[a-zA-Z]', s)
    if len(cha) > 0:
        return False
    else:
        return True

#  检查括号是否符合逻辑
def checkBrackets(s):
    chF = re.findall('\(', s)
    chB = re.findall('\)', s)
    if len(chF) == len(chB):
        # print(chF, chB)
        return True
    else:
        print('您输入的字符串中括号有误,可能有缺失')
        return False



# 处理带负号的乘除
def multiplicationAndDivisionMethod(s):
    rr = re.compile(r'-?[\d\.]+[\*/]-?[\d\.]+')
    while re.search(r'[\*/]', s):
        searchString = re.search(rr, s).group()
        # print(searchString)
        searchLi = re.findall(r'(-?[\d\.]+|\*|/)', searchString)
        # print(searchLi)
        if searchLi[1] == '*':
            result = str(float(searchLi[0]) * float(searchLi[2]))
        else:
            result = str(float(searchLi[0]) / float(searchLi[2]))
        s = re.sub(rr, result, s, 1)
    return s


# 处理加减法，变成数组，全加
def additionAndSubtractionMethod(s):
    searchLi = re.findall(r'([\d\.]+|\+|-)', s)
    print(searchLi)
    sumResult = 0
    for i in range(len(searchLi) - 1):
        print(searchLi[i])
        if searchLi[i] == '-' and searchLi[i+1] == '-':
            searchLi[i] = '+'
            searchLi[i+1] = '+'
    for x in range(len(searchLi)):
        if searchLi[x] == '-':
            searchLi[x] = '+'
            searchLi[x+1] = float(searchLi[x+1]) * (-1)
    for y in searchLi:
        if y == '+':
            y = 0
        sumResult = sumResult + float(y)
    return str(sumResult)



# 处理运算的逻辑
def handleOperatorLogic(s):
    return additionAndSubtractionMethod(multiplicationAndDivisionMethod(s))

# 处理括号
def handleInnerBrackets(s):
    ib = re.search(r'\([^()]+\)', s)
    innerString = ib.group()
    handleString = innerString[1:-1]
    operateString = handleOperatorLogic(handleString)
    return re.sub(r'\([^()]+\)', operateString, s, 1)

# 开始计算
def startCount(s):
    hasAlpha = checkAlphaInString(s)
    if hasAlpha == True:
        pass
        checkB = checkBrackets(s)
        if checkB == True:
            handleString = stripBlank(s)
            while '(' in handleString:
                handleString = handleInnerBrackets(handleString)
                print(handleString)
            else:
                print(''.join(['计算结果如下:', handleOperatorLogic(handleString)]))
    else:
        print('请核实您输入的内容，其中可能含有字母。。')

startCount(s1)