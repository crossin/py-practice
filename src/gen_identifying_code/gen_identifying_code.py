# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

from PIL import Image, ImageDraw, ImageFont
import os
import random
import string


def deform_char(ch):
    font_list = ['simhei.ttf', 'simsun.ttc',
                 'simkai.ttf', 'STXINWEI.TTF', 'SIMLI.TTF']
    # 我们选取几个候选字体

    def rd(n):
        # 这个函数只是一个“快捷方式”，为了让我们的代码简短一点。
        return random.randint(0, n)

    new_img = Image.new("RGBA", (120, 120), (255, 255, 255, 255))
    draw_img = ImageDraw.Draw(new_img)
    font = ImageFont.truetype(os.path.join(
        "fonts", random.choice(font_list)), 40)
    draw_img.text((40, 40), ch, font=font,
                  fill=(rd(255), rd(255), rd(255), 255))
    # 先随机选取字体和颜色，然后再进行随机的拉伸变化，你还可以选择任何其他的图像变换操作。
    new_img = new_img.transform((120, 120), Image.QUAD,
                                (rd(40) + 0, rd(40) + 0, rd(40) + 0, rd(40) + 80,
                                 rd(40) + 80, rd(40) + 80, rd(40) + 80, rd(40) + 0),
                                Image.BICUBIC)
    return new_img.crop((20, 20, 100, 100))


def deform_word(word):
    word_len = len(word)
    new_img = Image.new('RGBA', (80 * word_len, 80))
    # 初始化一个空的图片，我们采用rgba四通道的图片，我们可以自由选择图像透明度。
    for i, char_i in enumerate(word):
        # 我们逐字进行变换，并拼接，这样比对一整个单词进行变化效果要好得多。
        new_img.paste(deform_char(char_i), (i * 80, 0, i * 80 + 80, 80))
    return new_img


def gen_identifying_code(word_len=4):
    word = random.sample(string.ascii_letters + string.digits, word_len)
    # 我们选择所有大小写字母+数字，作为基本词元。当然，你也可以选择汉字。
    im = deform_word(word)
    im.show()
    # im.save('code.png')

if __name__ == '__main__':
    gen_identifying_code()
