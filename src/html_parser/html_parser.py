# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self._found_h1 = False
        # 用一个变量标记是否找到了标题

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            # a代表超链接
            for i in attrs:
                if i[0] == 'href':
                    # 找到超链接地址，并输出
                    print(i[1])
        elif tag == 'h1':
            # 发现了标题，但是标题内容不在里面
            self._found_h1 = True

    def handle_endtag(self, tag):
        # 别忘了在标题结尾时，把变量置为False
        if tag == 'h1':
            self._found_h1 = False

    def handle_data(self, data):
        if self._found_h1:
            # 处理数据时，如果发现当前数据是标题内容，则输出
            print("Title:", data)


def parse(file_name):
    parser = MyHTMLParser()
    with open(file_name, encoding='utf-8') as f_in:
        for line in f_in:
            parser.feed(line)

if __name__ == '__main__':
    parse('index.html')
