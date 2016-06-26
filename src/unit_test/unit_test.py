# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals


import unittest


class Dog:
    '''我们实现了一个“狗狗”类，它有几个方法和属性'''

    def __init__(self, name):
        self.name = name
        self.age = 1

    def bark(self):
        return 'My name is ' + self.name

    def grow_up(self, k):
        self.age += k

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name


class TestDog(unittest.TestCase):

    def setUp(self):
        '''每次测试前，都会调用这个函数，我们每次都新建一个狗狗对象'''
        print('Test begin!')
        self.mydog = Dog('Bob')

    def tearDown(self):
        '''每次测试后，调用这个函数，你可以在此时释放一些资源。'''
        print('Test over!')

    # 注意，所有测试方法都要以test开头，这样单元测试模块会自动调用这些方法
    def testBark(self):
        # 我们测试这只狗“叫”得是否正常
        self.assertTrue(self.mydog.bark().startswith('My name is'))
        # 我们使用单元测试模块提供的assert方法，而不是Python内建的assert
        self.assertTrue(self.mydog.bark().endswith(self.mydog.get_name()))

    def testAge(self):
        # 我们测试这只狗生长速度是否正常
        old_age = self.mydog.get_age()
        self.mydog.grow_up(3)
        self.assertEqual(old_age + 3, self.mydog.get_age())


if __name__ == '__main__':
    unittest.main()
    # 运行测试
    # 我们这里只是做了个简单示范，一般建议测试代码和程序代码分离。
