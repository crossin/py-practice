# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

try:
    from functools import partial
    from functools import reduce
except:
    pass


def read_file(file_name):
    '''读取文件，并返回点列表'''
    num_list = []
    with open(file_name) as f_in:
        # 试试用map来替代这个循环？
        for line in f_in:
            (x_r, y_r) = map(lambda x: float(x), line.split())
            ''' 此处使用了map函数，将向量x坐标和y坐标由字符串转换为小数
                同时也使用了匿名函数，你也完全可以写成：
                def f(x):
                    return float(x)
                map(f, ...)
                两者完全等价
            '''
            num_list.append((x_r, y_r))

    return num_list


def get_sorted_list(num_list):
    filted_points = filter(lambda p: p[0]**2 + p[1]**2 < 1, num_list)
    # 此处使用filter函数，只保留长度小于1的向量。
    return sorted(filted_points, key=lambda p: p[0]**2 + p[1]**2, reverse=True)
    # 同样的道理，这里应该很好理解了吧？


def add(a, b):
    return a + b


if __name__ == '__main__':
    num_list = read_file('in.txt')
    top_10 = get_sorted_list(num_list)[:10]
    print(reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), top_10))

    add_8 = partial(add, b=8)
    # 其实这就是柯里化，将多参数函数“拍扁”为单参数函数。
    print(add_8(3))
