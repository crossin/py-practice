# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import re


def find_pattern(file_name, pattern):
    with open(file_name, encoding='utf-8') as f_in:
        for line in f_in:
            matchs = pattern.search(line)
            # 如果找到，则输出匹配内容，注意此处是`search`不是`match`
            if matchs is not None:
                print(matchs.group())
                # 注意此处是`group`不是`groups`

if __name__ == '__main__':
    re_fun_name = re.compile(r'(?<=def )\w+')
    re_url = re.compile(r'https?://[/#\w\.\?\-]*')
    # 先对正则表达式进行预编译，以提升性能。

    find_pattern('index.html', re_fun_name)
    # find_pattern('in.txt',re_url)
