#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author name__ = 'gouzi'
__create time__ = '2018/1/21'
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

name = input('name is ')
age = input('age is ')
job = input('job is ')
salary = input('salary is ')
if salary.isdigit():
    salary = int(salary)
else:
    exit('salart must be A NUMBER!')

print(''' 
----------- info of %s --------------
Name is %s 
Age is %d
Job is %s
Salary is %.2f
You will be retired in %d years!
---------------- end ---------------------
''' % (name, name, int(age), job, salary, 65 - int(age)))
