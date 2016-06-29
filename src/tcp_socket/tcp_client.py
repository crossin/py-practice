# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import socket

if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 创建socket，这里和服务器端是一样的

    client_socket.connect(('127.0.0.1', 23333))
    # 连接到指定地址:端口，这里我们连接到本机。

    client_socket.send('Hello! I am a client!'.encode('utf_8'))
    # 发送一条信息，注意，发送的只能是“字节”，所以需要对unicode的字符串进行编码

    print(client_socket.recv(1024))
    # 打印接受到的信息，1024代表缓冲区大小。

    client_socket.close()
    # 和文件读写一样，记得关闭socket

    input()
    # 最后这个input()，作用是避免程序窗口一闪而过看不见输出，没有其他实际意义。
