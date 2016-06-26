# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import random
import math


def calculate_pi(iter_times):
    '''我们计算落在第一象限内、半径为1的1/4圆的面积，最后乘以4就是pi'''
    count = 0
    for i in range(iter_times):
        if(random.random()**2 + random.random()**2 < 1):
            # 随机生成x, y值作为点坐标，显然，如果和原点距离小于1，则落在圆内
            count += 1
    return 4 * count / iter_times


def calculate_area(iter_times):
    count = 0
    for i in range(iter_times):
        x = random.random()
        y = -random.random()
        # 因为random()生成的是(0, 1)随机数，但是显然我们的区域的纵坐标为负，
        # 因此要取负。
        if y > x**2 - 1 and y < math.log(x):
            # 很容易发现，区域内的点应该满足这个约束条件
            count += 1
    return count / iter_times


if __name__ == '__main__':
    iter_times = 1000000
    # 迭代次数，越大越精确
    my_pi = calculate_pi(iter_times)
    print(my_pi, abs(math.pi - my_pi))
    print(calculate_area(iter_times))
