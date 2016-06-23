# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import threading
import requests
import functools
import time

# 代理列表
PROXIES_LIST = ['203.66.159.44:3128', '86.188.142.244:8080',
                '178.88.64.83:3128', '202.100.167.145:80',
                '203.66.159.46:3128', '107.151.152.218:80',
                '202.100.167.182:80', '202.100.167.144:80',
                '202.100.167.180:80', '107.151.152.222:80',
                '202.100.167.142:80', '107.151.152.221:80',
                '165.138.66.247:8080', '165.138.66.32:8080',
                '14.136.207.38:3128', '192.163.208.245:8080',
                '202.100.167.160:80', '119.93.82.148:80',
                '5.135.254.35:3128', '183.91.33.42:8080', ]

# 测试地址
TEST_URL = 'http://1212.ip138.com/ic.asp'


def my_timer(func):
    # 我们之前实现的计时器
    @functools.wraps(func)
    def inner_fun(*args, **kw):
        start_time = time.time()
        ans = func(*args, **kw)
        end_time = time.time()
        print('Time:', end_time - start_time, 's')
        return ans
    return inner_fun


def get_via_proxy(url, proxy):
    '通过代理访问网页'
    proxies = {'http': proxy}
    try:
        r = requests.get(url, proxies=proxies)
        content = r.content.decode('gbk')
    except:
        content = None
    return content


@my_timer
def test_sigle_thread():
    proxies = PROXIES_LIST.copy()
    for i in proxies:
        get_via_proxy(TEST_URL, i)


@my_timer
def test_multi_thread(thread_num=10):
    # 先将代理列表拷贝一份，这样在pop时，原列表不会被修改
    proxies = PROXIES_LIST.copy()

    def thread_loop():
        '''多线程编程的核心就是完成这个函数，这是每个线程要执行的函数'''
        while len(proxies) > 0:
            # 我们让每个线程并发地访问共享的变量，
            # 每次都从中取出一个，直到发现已经取完则停止。

            # 思考题：
            # 其实这里有一个非常大的bug，
            # 不过一般只有在高并发下才会暴露出来，你能发现是什么问题么？
            proxy = proxies.pop()
            get_via_proxy(TEST_URL, proxy)

    thread_list = []
    for i in range(thread_num):
        # 新建线程，并指定线程要做的任务
        thread_list.append(threading.Thread(target=thread_loop, name=str(i)))

    for i in thread_list:
        i.start()
    # 让线程启动，并等待结束
    for i in thread_list:
        i.join()


if __name__ == '__main__':
    test_sigle_thread()
    test_multi_thread()
