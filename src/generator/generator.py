# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals


def fib_func(num):
    # 这是普通的计算第num个斐波拉契数的函数
    a = 0
    b = 1
    for i in range(num):
        (a, b) = (b, a + b)
    return a


def fib_with_num(num):
    ''' 计算第n个斐波拉契数，
        这个方法的优点是避免了重复计算，
        譬如计算1至n个斐波拉契数，上边的方法需要o(n^2)次计算，
        而此方法只要o(n)次计算，
        因为生成器函数保存了函数运行的上下文，减少了重复计算。
    '''
    a = 0
    b = 1
    for i in range(num):
        # 注意yield要写在上面而不是下面，不然就漏了第一个数了。
        yield a
        (a, b) = (b, a + b)


def fib_with_bound(bound):
    a = 0
    b = 1
    # 显然，只要当前的a值还没有到给定的界，那么便继续循环迭代下去。
    while a <= bound:
        yield a
        (a, b) = (b, a + b)


if __name__ == '__main__':
    # 分别验证三种方法的计算结果
    for i in range(10):
        print(fib_func(i))

    for i in fib_with_num(10):
        print(i)

    for i in fib_with_bound(100):
        print(i)
