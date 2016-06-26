# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import pickle


class Dog:
    '''这是一个狗类，它具有一些成员对象/方法'''

    def __init__(self, name):
        self.age = 1
        self.name = name

    def bark(self):
        print('My name is:', self.name)


def test_object():
    dog1 = Dog('Bob')
    with open('object.data', 'wb') as f_out:
        # 序列化
        pickle.dump(dog1, f_out)
        # 你也可以使用dumps方法

    with open('object.data', 'rb') as f_in:
        # 反序列化
        dog2 = pickle.load(f_in)

    # 我们将原来的“一号狗”序列化后，重新加载，
    # 新产生的狗和原来的狗应该是完全一样的，就好像克隆似的。
    dog1.bark()
    dog2.bark()
    print(dog1.age, dog2.age)


def test_class():
    with open('class.data', 'wb') as f_out:
        pickle.dump(Dog, f_out)

    with open('class.data', 'rb') as f_in:
        NewDog = pickle.load(f_in)

    dog1 = Dog('Jack')
    dog2 = NewDog('Alice')
    # 我们再来用新的‘狗类’来创建一只狗，
    # 这两只狗分别属于完全相同的两个类，但是却是不同的实体。
    dog1.bark()
    dog2.bark()
    print(dog1.age, dog2.age)

if __name__ == '__main__':
    # 分别测试一下对象的实例化以及类的实例化。
    test_object()
    test_class()
    # 你会发现，两者序列化的方法完全一样，这是因为Python中一切皆对象。
