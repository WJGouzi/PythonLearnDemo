#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author name__ = 'gouzi'
__create time__ = '2018/1/25'
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

# 集合(可变)
set1 = set('wangjun') # 无序且是可哈希的-> 去除重复的。
print(set1)  # {'j', 'w', 'u', 'g', 'n', 'a'}
# 所以在set中不能存放列表、字典，因为字典或列表是不可哈希的。

# 不可变集合
s = frozenset('wangjun1')
print(s)  # frozenset({'w', '1', 'g', 'n', 'a', 'u', 'j'})

# d = {set1:123} #不允许的


# 判断某个数据是否在集合内
s2 = set(['wangjun', 'wangjun11', 'hah'])
print('wangjun' in s2)  # True

# 添加一个元素到集合中 -> 将添加的元素作为一个整体
s2.add('i love u')
print(s2)  # {'hah', 'i love u', 'wangjun', 'wangjun11'}


# 更新添加到集合(会保留之前的)->将添加的元素作为序列添加到集合中
s2.update('ops')
print(s2)  # {'p', 's', 'wangjun11', 'wangjun', 'i love u', 'hah', 'o'}
s2.update('www') # -> 将只会添加一个'w' 因为有重复的。
print(s2)  # {'o', 'wangjun11', 'p', 'wangjun', 's', 'w', 'i love u', 'hah'}
s2.update(['wang', 10000])
print(s2)  # {'wang', 'w', 'p', 'i love u', 'hah', 'wangjun11', 10000, 'o', 's', 'wangjun'}
#   总结：
#       对于集合的add方法就是把元素作为一个整体添加到集合中去,且这个元素是要可哈希的。
#       对于update方法就是先将元素进行遍历(也就是说这个元素是课迭代的)，如果有重复的先去掉重复的，然后再添加到集合中。


# 删除、清空
s2.remove('s')
s2.pop()  # 随机删除。
s2.clear()  # 清空
del set1    # 删除集合



##### 集合的关系 #####
a = set([1, 2, 4, 5, 6])
b = set([3, 4, 5, 6, 7, 8])
# 相等的集合
print(set('wangjun') == set('wangjunjun'))  # True
# 超集关系
print(set('wangjun') > set('wangjunWANGJUN'))  # False
print(a.issuperset(b))
# 子集关系
print(set('wangjun') < set('wangjunWANGJUN'))  # True 包含关系（第一个是第二个的严格子集）
print(a.issubset(b))
# 取并集
print(set('wangjunWW') | set('wangjunJJ'))  # {'n', 'j', 'u', 'w', 'a', 'W', 'g', 'J'}
print(a.union(b))   # {1, 2, 3, 4, 5, 6, 7, 8}
# 取交集
print(set('wangjunWW') & set('wangjunJJ'))  # {'n', 'a', 'g', 'w', 'j', 'u'}
print(a.intersection(b))    # {4, 5, 6}
# 取差集
print(set('wangjunWW') - set('wangjunJJ'))  # {'W'}
print(set('wangjunJJ') - set('wangjunWW'))  # {'J'}
print(a.difference(b))  # {1, 2}
print(b.difference(a))  # {8, 3, 7}
# 反向交集
print(a ^ b)    # {1, 2, 3, 7, 8}
print(a.symmetric_difference(b))    # {1, 2, 3, 7, 8}





