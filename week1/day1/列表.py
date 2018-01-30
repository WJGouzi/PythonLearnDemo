#!/usr/bin/env python
# encoding: utf-8
"""
@author: wj
@license: (C) Copyright 2013-2017.
@contact: 1693841903@qq.com
@file: 列表.py
@version: 1.0
@time: 2018/1/22 14:19
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


a = []
a1 = list([1,3,5])
print(a1)

# 列表
# ############################ 增删改查 #########################

names = ['wangjun', 'hah', 'hhasda', 'enen', 'dasdasfsdf', 'avvv']
# # 取一个值
print(names[0])
# 取多个值
# 增 切片
print(names[1:3])  # ['hah', 'hhasda'] 从i个取，取到j-1
print(names[1:])  # ['hah', 'hhasda', 'enen', 'dasdasfsdf', 'avvv'] 从第i个开始取，取到最后
print(names[1: -1])  # ['hah', 'hhasda', 'enen', 'dasdasfsdf'] 从第i个开始取，取到最后一个之前
print(names[1::2])  # ['hah', 'enen', 'avvv'] 从左到有去隔一个取
print(names[::-2])  # -2 从右往左隔一个取。这个最后一个值是有方向性的。

# 添加
# append / insert
names.append('jun')  # 默认是插到最后一个位置, 'append'这个方法 会 把names这个列表进行修改的
print('append : ',names)  # append :  ['wangjun', 'hah', 'hhasda', 'enen', 'dasdasfsdf', 'avvv', 'jun']
names + ['haodeya']  # '+' 这个是 不会 把names这个列表的数据修改的
print('+ ',names)  # +  ['wangjun', 'hah', 'hhasda', 'enen', 'dasdasfsdf', 'avvv', 'jun']
names.insert(3, 'enenenn') # 将数据插入到任意一个位置
print(names)

# 修改
names[len(names)-2] = 'mySelf'
print(names)
# 修改多个值
names[1:3] = ['love', 'U']
print(names)


# 删除
# remove / pop / del
names.remove('enen')  # 删除对应的对象，不能用下标进行删除，remove是删除list中的元素的值
print(names)

deleteObject = names.pop(3) # 用索引去删除list中的对象 删除后会返回删除的值 ,,如果不指定index，就会删除最后一个
print(deleteObject)
print(names)


del names[1] # 可以删除某个元素，也可以对某个对象进行删除
print(names)

# names.clear()  # 将列表进行清空


# 查
print('xx' in names)


########################## 内部的方法 ############################
# count
print('wangjun\'s count is :',names.count('wangjun'))

#extend
names.extend('新增的元素')
print(names)
a = [1, 4, 5, 6, 5]
b = [2, 4, 5, 7, 88]
a.extend(b) # 将b添加到a中，对b没有任何的影响，对a来说进行了修改
print(a)
print(b)


# index --->>> 根据内容找位置
print('U\'s index is :',names.index('U'))  # 默认是取到第一个'U'

######   取第二个'5' in 'a' 列表
first5Index = a.index(5)
littleList = a[first5Index+1:]
second5Index = littleList.index(5)
print("first '5' index is %d, second '5' index in little list is %d" % (first5Index, second5Index))
print("second '5' in 'a' list index is %d" % (first5Index + second5Index + 1))

# reverse 反转列表
a.reverse()
print('reverse a is :',a)

# sort 排序
a.sort()
print('sort a is :',a)
names.sort()
print('name sort is :', names) #  按照ASCII进行排序

