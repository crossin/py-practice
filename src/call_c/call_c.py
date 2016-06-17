# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import ctypes
import time
import functools


def my_timer(func):
    @functools.wraps(func)
    def inner_fun(*args, **kw):
        start_time = time.time()
        ans = func(*args, **kw)
        end_time = time.time()
        print('Time:', end_time - start_time)
        return ans
    return inner_fun


@my_timer
def test_py(n):
    for i in range(n):
        i % 997


@my_timer
def test_c(n):
    libtest = ctypes.cdll.LoadLibrary('mod.o')
    libtest.modntimes(997, n)


if __name__ == '__main__':
    n = 10000000
    test_py(n)
    test_c(n)
