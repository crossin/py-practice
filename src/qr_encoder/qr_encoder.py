# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import qrcode


def encode_url_and_show(url):
    img = qrcode.make(url)
    return img


def encode_words_ec(words):
    qr = qrcode.QRCode(
        version=3,
        # 二维码的版本，一般而言，版本越高，生成的二维码越大
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        # 总共有 'L', 'M', 'Q', 'H' 四种纠错能力
        box_size=10,
        # 每个“block”的大小，越大的话，你生成的二维码也就越大
        border=4,
        # 周边空白区域面积
    )
    qr.add_data(words)
    # 二维码是对二进制的信息进行编码，因此字符串肯定要编码成字节
    # 这里不需要考虑汉字编码的问题，qrcode包里已经自动帮我们处理了，
    # 一些扫描软件里也
    qr.make(fit=True)
    # fit=True代表将根据数据量大小，自动调整二维码尺寸。

    img = qr.make_image()
    return img


if __name__ == '__main__':
    img = encode_url_and_show('http://coolshell.cn/articles/10590.html')
    # img = encode_words_ec('好好学习，天天向上')
    img.show()
    # img.save('qrcode.jpg')
