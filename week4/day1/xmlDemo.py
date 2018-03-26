#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'xml'
__author name__ = 'gouzi'
__create time__ = '2018/3/26'
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

import xml.etree.ElementTree as ET



tree = ET.parse('xmlFile')
rootNode = tree.getroot()
print(rootNode.tag)

# 遍历的是xml所有节点
# for child in rootNode:
#     print(child.tag, child.attrib)
#     for i in child:
#         print(i.tag, i.attrib)

# 遍历的是所有关于year节点
for node in rootNode.iter('year'):
    print(node.tag, node.text)





# 修改节点中的值

# for node in rootNode.iter('year'):
#     nodeText = int(node.text)+1
#     node.text = str(nodeText)
#     node.set("changed", "yes")
#
# tree.write("xmlFile1")  # 如名字一样将覆盖之前的文件，如果不一致则重新生成一个文件


# 删除节点
xmlTree = ET.parse('xmlFile1')
xmlRootNode = xmlTree.getroot()
for country in xmlRootNode.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        xmlRootNode.remove(country)

xmlTree.write("xmlFile2")



