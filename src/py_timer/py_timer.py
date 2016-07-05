# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import threading
import sched
import time


def simple_timer():
    def say_hello(word):
        # 作为演示，我们只定义了一个简单的接受一个参数的函数，
        # 显然你可以把它换成任意复杂的函数
        print('hello', word)
    my_timer = threading.Timer(1.0, say_hello, ['python'])
    # 三个参数分别是 时间(s)，要执行的函数，传入的参数。
    # 此处你还可以使用 *args, **kw 方法传参。
    my_timer.start()


def loop_use_threading():
    def say_hello(word):
        print('hello', word)
        my_timer = threading.Timer(1.0, say_hello, ['python'])
        my_timer.start()
        # 有点递归调用的感觉，不是么？
        # 但是放心，由于是启动一个新线程执行任务，
        # 原函数会直接结束返回，因此不用担心栈溢出的风险。
    my_timer = threading.Timer(1.0, say_hello, ['python'])
    my_timer.start()


def loop_use_sched():
    # 和之前的例子是完全类似的道理，也是在“递归调用”
    # 但是比直接用threading要更方便些，并且功能更强大。
    def say_hello(sc, word):
        print('hello', word)
        sc.enter(1.0, 1, do_something, [sc, 'python'])

    my_sc = sched.scheduler(time.time, time.sleep)
    my_sc.enter(1.0, 1, say_hello, [my_sc, 'python'])
    # 这里多了一个参数，表示优先级
    my_sc.run()


if __name__ == "__main__":
    simple_timer()
    # loop_use_threading()
    # loop_use_sched()
