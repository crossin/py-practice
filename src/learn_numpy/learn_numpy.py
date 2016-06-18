# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import numpy as np
import random
import functools
import time


def my_timer(func):
    '''这是一个计时器，如果不熟悉的话，可以去参考`装饰器`那一题'''
    @functools.wraps(func)
    def inner_fun(*args, **kw):
        start_time = time.time()
        ans = func(*args, **kw)
        end_time = time.time()
        print('Time:', end_time - start_time, 's')
        return ans
    return inner_fun


def matrix_mul(a, b):
    '''自己实现矩阵乘法'''
    assert len(a[0]) == len(b)
    # 矩阵乘法对两个矩阵的尺寸是有限制的
    ans = [[0] * len(a) for i in range(len(b[0]))]
    # 建立空的矩阵，用以存放结果，
    # 注意到，对于行我们直接用`*`，但是对列用了列表生成式，想想这是为什么？
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                ans[i][j] += a[i][k] * b[k][j]
    return ans


def matrix_pow(m, k):
    '''自己实现矩阵的乘方'''
    ans = m
    for i in range(k - 1):
        ans = matrix_mul(ans, m)
    return ans


@my_timer
def test_matrix_py(size_=10, times_=10000):
    rmatrix = [[random.random() for i in range(size_)] for j in range(size_)]
    # 生成一个二维的列表，并且当初矩阵来看待
    ans = matrix_pow(rmatrix, times_)


@my_timer
def test_matrix_np(size_=10, times_=10000):
    rarray = np.random.random(size=(size_, size_))
    # numpy自带的随机函数，可以直接返回一个给定尺寸的多维列表，是不是很方便？
    rmatrix = np.asmatrix(rarray)
    # asmatrix函数把多维列表转为矩阵，并且从效率上考虑，不会进行数据拷贝
    ans = rmatrix**times_
    # numpy已重载了多个操作符，因此非常方便！不必像我们之前那样手工计算。

if __name__ == '__main__':
    test_matrix_np()
    test_matrix_py()
    ''' 以下是我的电脑的运行结果，对于如此的性能差异，是不是很吃惊？
        Time: 0.004990100860595703 s
        Time: 4.397124290466309 s
    '''
