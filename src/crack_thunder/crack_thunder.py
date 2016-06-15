# -*- coding: utf-8 -*-

import base64

TEST_URL = 'thunder://QUFodHRwOi8vZGxkaXIxLnFxLmNvbS9xcWZpbGUvcXEvUVE4LjMvMTgwMzgvUVE4LjMuZXhlWlo='


def crack_thunder(thunder_url):
    thunder_url = thunder_url.strip()
    # 为了提升代码的鲁棒性，我们先把输入两边的空白字符过滤掉。
    assert thunder_url[:10] == 'thunder://'
    # 首先我们要判断这个链接是不是迅雷链接
    base64_str = thunder_url.split('thunder://')[1]
    # 然后我们把后边的base64字符串部分提取出来
    assert base64_str
    org_str = base64.b64decode(base64_str).decode('utf-8')
    # 在这里，需要注意，Python 3 里的全部使用unicode来表示字符串。
    # 而 base64.b64decode 返回的是 'bytes'，因此需要转换一下

    assert org_str[:2] == 'AA' and org_str[-2:] == 'ZZ'
    # 同样，我们要检查解密出来的字符串是否是合法的迅雷下载地址。

    return org_str[2:-2]

if __name__ == '__main__':
    print(crack_thunder(TEST_URL))
