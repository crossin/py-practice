# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import requests
import re

TEST_URL = 'http://1212.ip138.com/ic.asp'


def get_via_proxy(url, proxy):
    proxies = {'http': proxy}
    # 使用requests进行代理访问就是这么简单！
    r = requests.get(url, proxies=proxies)

    return r.content('gbk')
    # 我们访问的这个网址是gbk编码的


def extract_proxies(page_content):
    proxy_pattern = re.compile(r'((\d{1,3}\.){1,3}\d{1,3}:\d{1,5})')
    # 这是一个代理地址的正则表达式的必要不充分条件，不过一般情况下已经够用了。
    matches = proxy_pattern.findall(page_content)
    # findall函数返回的是group信息，因此要稍微处理一下结果
    return list(map(lambda x: x[0], matches))


def test_k_times(url, proxy_list, k=3):
    proxies = {'http': ''}
    for i in range(3):
        # 两重循环的顺序能换一下么？
        for proxy in proxy_list:
            proxies['http'] = proxy
            try:
                r = requests.get(url, proxies=proxies)
                # 如果不出意外的话，每次将输出我们来自不同的ip
                print(r.content.decode('gbk'))
                # 你可以解析一下html页面，只输出我们想要的内容么？
            except:
                # 我们只采用了非常简单粗暴的异常处理方式，
                # 但实际上这种方式效果非常好，虽然它会掩盖错误原因。
                continue


if __name__ == '__main__':
    ''' 从网页抓取代理列表
        r = requests.get('http://xxxxxx.html')
        proxy_list=extract_proxies(r.text)
    '''
    with open('page.html', encoding='utf-8') as f_in:
        # 直接从我们给的文件中解析
        proxy_list = extract_proxies(f_in.read())

    test_k_times(TEST_URL, proxy_list)
