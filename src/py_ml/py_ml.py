# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.tree import DecisionTreeClassifier as DTC
import csv
import random
import time


def train(clf, train_data):
    # 我们在训练时，要把样本的属性和类别分开传入。
    X = np.array([i[:-1] for i in train_data])
    Y = np.array([i[-1] for i in train_data])
    clf.fit(X, Y)


def read_csv(file_name='fourclass.csv'):
    '''从csv文件中读取数据，把最后一列作为类别标记，其余作为属性'''
    with open(file_name) as csv_file:
        spamreader = csv.reader(csv_file)
        data_set = []
        for row in spamreader:
            for i, item in enumerate(row):
                row[i] = float(item)
            data_set.append(tuple(row))
        return data_set


def test(classifier, input_data):
    random.shuffle(input_data)
    data_size = len(input_data)
    train_data = input_data[int(data_size / 10):]
    train(classifier, train_data)

    # 取数据集中的前10%作为测试数据
    # 由于之前我们已经将数据集打乱过，因此不必担心分布不均匀的情况。
    test_data = input_data[:int(data_size / 10)]
    test_input = [i[:-1] for i in test_data]
    test_ans = [i[-1] for i in test_data]
    test_output = classifier.predict(test_input)

    # 比较预测的结果和真实结果的差别，并返回错误率
    error_counts = 0
    for i, j in zip(test_ans, test_output):
        if(abs(i - j) > 0.0001):
            # 由于结果是浮点数，直接比较或许会不精确，因此采用这种比较方式。
            error_counts += 1
    error_rate = error_counts / len(test_data)
    return error_rate


if __name__ == '__main__':
    ''' 下面演示了线性判别分析，K最近邻分类和决策树算法
        有兴趣的话还可以尝试其他分类算法
    '''
    clf = LDA()
    # clf = KNN()
    # clf = DTC()
    input_data = read_csv('fourclass.csv')
    print(test(clf, input_data))
