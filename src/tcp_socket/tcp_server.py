# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import socket

# 这是服务器端代码，记得先运行服务器端代码后运行客户端代码哦！

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 前者代表使用ipv4协议，后者代表TCP协议

    server_socket.bind(('127.0.0.1', 23333))
    # 监听本机端口，注意不要冲突，并且注意系统防火墙设置。

    server_socket.listen()
    # 开始监听端口

    (sock, addr) = server_socket.accept()
    # 这里是阻塞式的，只有接受到一个请求才会返回。
    sock.send('Hello! I am a server!'.encode('utf_8'))
    print(sock.recv(1024))

    # 我们在接收并发送一条信息后就结束程序，
    # 你能用之前学过的多线程知识，用多线程来处理请求么？
    sock.close()
    server_socket.close()
    input()
