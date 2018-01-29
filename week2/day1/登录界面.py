#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: 登录界面.py
@version: 1.0
@time: 2018/1/29 15:59
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
# 登录界面

pages = ['home', 'finance', 'book']
lastPage = ''
def loginFunc(type):
    def login(func):
        def loginWithFile():
            f = open('JDUserFile' if type == 'jingdong' else 'WXUserFile', 'r')
            info = f.read()
            f.close()
            print(info)
            infoDict = eval(info)
            isLogin = infoDict['islogin']
            if isLogin == False:
                userInfoDict = infoDict['info']
                userName = input('user name is :')
                passWord = input('pass word is :')
                if userName == userInfoDict['userName'] and passWord == userInfoDict['passWord']:
                    print('登录%s账户成功' % type)
                    f = open('JDUserFile' if type == 'jingdong' else 'WXUserFile', 'w')
                    f.seek(0)
                    modifyDict = {'islogin' : True, 'info': {'userName': userName, 'passWord': passWord}}
                    f.write(str(modifyDict))
                    f.close()
                    func()
                else:
                    print('您输入的账号或密码有误')
        return loginWithFile
    return login


# while True:
#     for i in pages:
#         print('page is %s' % i)
#     choice = input('>>>:').strip()
#     if choice in pages:
#         if choice == 'home':
#             @loginFunc('jingdong')
#             def home():
#                 print('this is home page')
#             home()
#         elif choice == 'finance':
#             @loginFunc('weixin')
#             def finance():
#                 print('this is finance page')
#             finance()
#         else:
#             @loginFunc('jingdong')
#             def book():
#                 print('this is book page')
#             book()
#     else:
#         print('请输入正确的选项')


@loginFunc('jingdong')
def home():
    print('this is home page')
@loginFunc('weixin')
def finance():
    print('this is finance page')
@loginFunc('jingdong')
def book():
    print('this is book page')

while True:
    for i in pages:
        print('page is %s' % i)
    choice = input('>>>:').strip()
    if choice in pages:
        if choice == 'home':
            home()
            lastPage = 'home'
        elif choice == 'finance':
            finance()
            lastPage = 'finance'
        elif choice == 'book':
            book()
            lastPage = 'book'
        else:
            print('请输入正确的选项')
    elif choice == 'quit':
        pass
        # f = open('WXUserFile' or 'JDUserFile', 'r')
        # info = f.read()
        # f.close()
        # infoDict = eval(info)
        # userName = infoDict['info']['userName']
        # passWord = infoDict['info']['passWord']
        # f1 = open('WXUserFile' or 'JDUserFile', 'w')
        # f1.seek(0)
        # modifyDict = {'islogin': False, 'info': {'userName': userName, 'passWord': passWord}}
        # f1.write(str(modifyDict))
        # lastPage = ''
    else:
        print('请输入正确的选项')
