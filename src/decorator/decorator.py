# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import time
import functools


def my_timer(func):
    # 添加这个装饰器是为了使方法签名一致，
    # 试试不加这个装饰器，然后运行 help(my_timer) 看看输出结果？
    @functools.wraps(func)
    def inner_fun(*args, **kw):
        start_time = time.time()
        # 运行原函数
        ans = func(*args, **kw)
        end_time = time.time()
        print('Time:', end_time - start_time, 's')
        # 别忘了返回原输出结果
        return ans
    return inner_fun


class Test:
    '''这是一个样例类，类中只有一个成员x'''

    def __init__(self):
        self._x = None

    @property
    def x(self):
        # 这是x的getter方法，我们对返回值进行检查，如果x为空，则输出报错信息
        if self._x is None:
            print('x is None!')
        else:
            return self._x

    @x.setter
    def x(self, val):
        # 这是x的setter方法，
        # 检测x的值是否符合要求
        if val > 100 or val < 0:
            print('input is illegal!')
        else:
            self._x = val


# 我们对这个函数运行时间进行测试，试着删掉@my_timer看看运行结果？
@my_timer
def test_time(n):
    for i in range(n):
        i * n

if __name__ == '__main__':
    test_time(10000000)
    t = Test()
    print(t.x)
    t.x = 43
    print(t.x)
    t.x = 444
