# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

from PIL import Image
from PIL import ImageFilter


def resize_to_half(img):
    (width, height) = img.size
    # 获取原图大小，然后将将其尺寸减半传入resize方法，注意要改为整数
    half_img = img.resize((int(width / 2), int(height / 2)))
    # 还可以用thumbnail方法，但是它直接修改了原图，不推荐
    return half_img


def convert_to_grey(img):
    # 将图像转为灰度图像，如果要转为二值图像可以传入'1'
    return img.convert('L')


def rotate_90_clockwise(img):
    # 作为演示用途，我们直接将参数硬编码了，
    # 实际使用时没有必要特意编写这样一个函数，直接使用rotate方法即可。
    return img.rotate(90)


def gauss_blur(img):
    # 使用高斯滤波器对图像进行模糊处理
    return img.filter(ImageFilter.GaussianBlur)


if __name__ == '__main__':
    with Image.open('Lenna.png') as img:
        # 以下依次是对图像进行：改变大小、改变颜色模式、旋转、模糊操作
        half_img = resize_to_half(img)
        half_img.save('Lenna_half.png')

        grey_img = convert_to_grey(img)
        grey_img.save('Lenna_grey.png')

        rotate_img = rotate_90_clockwise(img)
        rotate_img.save('Lenna_rotate.png')

        blur_img = gauss_blur(img)
        blur_img.save('Lenna_blur.png')
