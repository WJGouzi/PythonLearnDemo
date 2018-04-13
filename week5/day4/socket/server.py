#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: server.py
@version: 1.0
@time: 2018/4/13 10:21
@desc: 服务端
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
import socket

# 创建socket对象
# 地址族: family=AF_INET(服务器之间的通信), AF_UNIX(Unix不同进程直接的通信)
# 协议方式: type=SOCK_STREAM(tcp) SOCK_DGRAM(udp)
sk = socket.socket()  # 默认参数 表示的是TCP的协议的连接

address = ('127.0.0.1', 8800)
sk.bind(address)
sk.listen(3)                     # 最多的连接数
print('waiting')
conn,addrs = sk.accept()           # conn才是真实的连接的通道，所以要收发消息都要用conn
print(conn)
'''
( 
    <
        socket.socket fd=5,
        family=AddressFamily.AF_INET, 
        type=SocketKind.SOCK_STREAM, 
        proto=0, 
        laddr=('127.0.0.1', 8800), 
        raddr=('127.0.0.1', 51442)  # 51442 这是客服端的端口号
    >, 
    ('127.0.0.1', 51442)
)
'''
print(addrs)

# 发送消息
# inp = str(input('输入内容:'))
# inpData = bytes(inp, 'utf8')
# conn.send(inpData)          # send和recv中传入的参数一定是byte值


# 接收消息
data = conn.recv(1024)
decodeData = str(data, 'utf8')
print(decodeData)

conn.close()                  # 关闭掉当前的连接的通道
# sk.close()                    # 就关闭了所有连接的通道()