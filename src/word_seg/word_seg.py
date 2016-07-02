# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import jieba
import jieba.posseg


def word_segementation(file_name):
    with open(file_name, encoding='utf-8') as f_in:
        # 注意编码格式，最好是utf-8编码
        for line in f_in:
            seg_list = jieba.cut(line)
            # 只要将句子传入，就可以得到分词完的列表，当然你还可以设置其他更高级的参数。
            print('/'.join(seg_list))
            # 我们使用‘/’将单词隔开。


def mark_property(file_name):
    with open(file_name, encoding='utf-8') as f_in:
        for line in f_in:
            seg_list = jieba.posseg.cut(line)
            # 我们使用可以标记单词属性的分词器，原理类似，不过或许会慢一些。
            for i in seg_list:
                print(i)

if __name__ == '__main__':
    word_segementation('in.txt')
    mark_property('in.txt')
