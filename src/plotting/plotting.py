# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import math
import numpy as np
import matplotlib.pyplot as plt


def read_file(file_name):
    '''这里我们直接借用了之前的代码'''
    point_list = []
    with open(file_name) as f_in:
        for line in f_in:
            (x, y) = map(lambda x: float(x), line.split())
            point_list.append((x, y))
        return point_list


def plot_scatter(point_list):
    plt.title("This is my first plot!")
    # 分别设置图表的标题、x/y轴的标签
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.scatter(list(map(lambda p: p[0], point_list)),
                list(map(lambda p: p[1], point_list)))
    # 将每个点的x和y坐标分别传入
    # 这里我们使用了map函数将所有点的x和y坐标分别提取，
    # 数据量比较大时，推荐使用NumPy
    plt.show()


def my_func(x):
    return math.sin(x) + math.log(abs(x) + 1) + x

def plot_func(func):
    plt.title("This is my second plot!")
    # 分别设置图表的标题、x/y轴的标签
    plt.xlabel("X")
    plt.ylabel("Y")
    x = range(-30, 30)
    # 我们准备绘制(-30, 30)之间的函数图像。
    plt.plot(x, list(map(my_func, x)))
    # 这里，我们使用map函数来得到给定区间内的函数值
    plt.show()


if __name__ == '__main__':
    point_list = read_file('in.txt')
    plot_scatter(point_list)
    plot_func(my_func)
