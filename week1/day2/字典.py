#!/usr/bin/env python
# encoding: utf-8
"""
@author: wj
@license: (C) Copyright 2013-2017.
@contact: 1693841903@qq.com
@file: 字典.py
@version: 1.0
@time: 2018/1/23 09:39
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


# 字典中的key值必须是不可修改类型的数据，且key值是唯一的。
# 字典中的键值对也是和其他的语言中的一样是无序的

# #######################
# 可变类型：列表、字典
# 不可变类型：整型、字符串、元组

dic1 = {'name':'wangjun', 'age':27, 'hobby':'girl', 'isHandsome':True}
print(dic1)

dic2 = dict((('name', 'wangjun'),)) # ',' 是必要的不然会报错
print(dic2)

dic3 = dict([['name', 'wangjun'],['age', 18],])
print(dic3)

# 以上的三种创建字典的方式都是合理的，dic2和dic3的创建是使用了类的工厂方法进行创建，在dict()的括号里，包含的是一组键值对，键值对可以是用元组或者是列表的形式展示的。


########################## 字典操作 ################################
# 增
dic1['goodAt'] = 'iOS'
print(dic1)

age0 = dic2.setdefault('age', 18)
print('dic2 set default :',dic2) # dic2 set default : {'name': 'wangjun', 'age': 18}
print(age0) # 18
age = dic1.setdefault('age', 18)
print('dic1 set default :',dic1) # dic1 set default : {'name': 'wangjun', 'age': 27, 'hobby': 'girl', 'isHandsome': True, 'goodAt': 'iOS'}
print(age) # 27
#  setdefault 方法会先在字典中去找相对应的key值，如果没有对应的key值就添加，如果找到了就不会做任何的处理， setdefault是有返回值的


# 查
# 查某一个键对应的值
print('dic3 name is :',dic3['name']) # wangjun
# 查键
print('dic3 keys are :', dic3.keys(),'type is :', type(dic3.keys())) # dic3 keys are : dict_keys(['name', 'age']) type is : <class 'dict_keys'>
# 查值
print('dic3 values are :', dic3.values(), 'type is :',type(dic3.values())) # dic3 values are : dict_values(['wangjun', 18]) type is : <class 'dict_values'>
# 查键值对
print('dic3 items are :', dic3.items(), 'type is :', type(dic3.items())) # dic3 items are : dict_items([('name', 'wangjun'), ('age', 18)]) type is : <class 'dict_items'>
#  以上的类型都不是列表类型，如果需要可以强转成list类型(在python2中就是list类型的)



# 改
# 修改某一个键对应的值
dic1['goodAt'] = 'Python' # 如果这个键在字典中没有对应的，那么就会将这个键值对添加到字典中； 如果有这个键，那么就会修改掉这个键对应的值
print(dic1)

dic4 = {'age': 18, 'name': 'wangjun', 'gender': 'female'}
dic5 = {1:'haha', 2:'enen'}
dic4.update(dic5)
print(dic4) # {'age': 18, 'name': 'wangjun', 'gender': 'female', 1: 'haha', 2: 'enen'}
print(dic5) # {1: 'haha', 2: 'enen'}
dic6 = {'age': 27, 'name': 'wangjun', 'hobby': 'football'}
dic4.update(dic6)
print(dic4) # {'age': 27, 'name': 'wangjun', 'gender': 'female', 1: 'haha', 2: 'enen', 'hobby': 'football'}

#  dict1.update(dict2)方法，如果在dict2中没有dict1的键，那么dict2会直接添加到dict1中，并修改dict1的数据，但dict2中的数据是不会进行更改的。
#  如果dict2中有dict1相同的键，那么dict1中的键值对会被dict2的键值对覆盖掉。

# 删
# 删除某个键值对
del dic4[1]
print(dic4)
# 清空字典
dic6.clear()
print(dic6)
# 删除指定的键值对，并返回一个值
value1 = dic4.pop(2)
print(value1)
print(dic4)
# 随机删除,并返回一个键值对，以元组进行展示
value2 = dic4.popitem() # 一般不用
print(value2)
print(dic4)


########################## 字典的其他操作 ################################

# 创建字典的其他的方法（基本不用）
dict1 = dict.fromkeys(['host1','host2', 'host3'], 'wangjun') # 将列表中的每一个元素当做键， 后面的那个数据为字典的值
print(dict1) # {'host1': 'wangjun', 'host2': 'wangjun', 'host3': 'wangjun'}

dict2 = dict.fromkeys(['host1','host2', 'host3'], ['wangjun', 'enen'])
print(dict2) # {'host1': ['wangjun', 'enen'], 'host2': ['wangjun', 'enen'], 'host3': ['wangjun', 'enen']}
dict2['host2'][1] = 'haha'
print(dict2) # {'host1': ['wangjun', 'haha'], 'host2': ['wangjun', 'haha'], 'host3': ['wangjun', 'haha']}
# 所以是基本不使用，这是由于深浅拷贝的问题


# 字典的嵌套
# 类似Json一样的


# 排序
print(sorted(dic1)) # ['age', 'goodAt', 'hobby', 'isHandsome', 'name']
print(sorted(dic1.items())) # [('age', 27), ('goodAt', 'Python'), ('hobby', 'girl'), ('isHandsome', True), ('name', 'wangjun')]



# 字典的遍历
for key in dic1: # 默认遍历的是字典的键 # 推荐使用的方法
    print('key value is : %s -- %s' % (key, dic1[key]))
# key value is : name -- wangjun
# key value is : age -- 27
# key value is : hobby -- girl
# key value is : isHandsome -- True
# key value is : goodAt -- Python

for key, value in dic1.items(): # 效率不高
    print('key is : %s, value is %s' % (key, value))
# key is : name, value is wangjun
# key is : age, value is 27
# key is : hobby, value is girl
# key is : isHandsome, value is True
# key is : goodAt, value is Python