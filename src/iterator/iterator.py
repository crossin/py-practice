# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals


class Fib_with_bound:
    ''' 所谓的迭代器，其实就是满足特定接口的一个对象，在这里，只要实现了
        `__iter__`和`__next__`方法的类的实例即可被称为迭代器
    '''

    def __init__(self, bound):
        # 先初始化，设定最大值
        # 只有在生成一个新的迭代器对象时，这个方法才会执行。
        self.bound = bound

    def __iter__(self):
        # 这相当于迭代过程的初始化，
        # 先设定斐波拉契数列的前两项，
        # 每次要迭代时，这个方法只会在最开始执行一次，并返回一个可迭代对象。
        self.a = 0
        self.b = 1
        # 这里，我们直接返回了自身，因为自己已经实现了next方法，
        # 可以直接迭代，也可以返回别的可迭代对象。
        return self

    def __next__(self):
        # 以后每次迭代时，都将执行这个方法，是否停止取决于是否抛出异常
        # 注意，对于Python2，需要将这个函数名改为`next(self)`，其余没有区别
        next_num = self.a
        if next_num > self.bound:
            # 迭代到末尾时，抛出一个停止迭代的异常，系统便知道要停止了
            # 不然就将无限迭代下去。
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        # 记得返回每次迭代后的值。
        return next_num


class Fib_with_num:

    def __init__(self, nums):
        # 先设定最大值
        self.nums = nums

    def __iter__(self):
        self.count = 0
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        # 每次调用next方法时，先将计数加一
        self.count += 1
        next_num = self.a
        if self.count > self.nums:
            # 当迭代了指定次数后，迭代终止。
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return next_num


if __name__ == '__main__':
    # fib = Fib_with_num(10)
    fib = Fib_with_bound(100)

    # 在for循环这里，先执行一次`__iter__`方法，然后每次循环时，
    # 都执行一次`__next__`方法，直至停止。
    for i in fib:
        print(i)
