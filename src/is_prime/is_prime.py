# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import random


def is_prime_1(n):
    '''这是最朴素的素数判别算法，应该很容易理解'''
    if n <= 1:
        return False
    if n == 2:
        return True
    if n & 0x1 == 0:
        return False
    # 这里有一点点局部的优化，但是并没有带来时间复杂度的质变。
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_prime_2(num):
    test_times = 3
    # 循环验证的次数，越大则误判率越低。
    if num <= 1:
        return False
    for i in range(test_times):
        bound = 111111
        if num < bound:
            bound = num
        a = random.randint(1, bound - 1)
        # 从[1, bound-1]中随机选择一个数，进行判断，
        # witness(a, num)为False是一个数为素数的必要不充分条件。
        if witness(a, num):
            return False
    return True


def witness(a, num):
    ''' 这是本算法的核心部分，比较难以理解，
        光靠几行简单的注释是没有办法解释清楚的，
        如果有兴趣的话，可以参考《算法导论》，那里有详细的介绍和分析
    '''
    temp = num - 1
    t = 0
    while (temp & 0x1) == 0:
        t += 1
        temp >>= 1
    u = (num - 1) >> t
    x0 = pow(a, u, num)
    x1 = x0
    for i in range(t):
        x1 = (x0**2) % num
        if x1 == 1 and x0 != 1 and x0 != num - 1:
            return True
        x0 = x1
    if x1 != 1:
        return True
    return False

if __name__ == '__main__':
    for i in range(1000):
        assert is_prime_1(i) == is_prime_2(i)

    print(is_prime_2(35782337279234634575247))
