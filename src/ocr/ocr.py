# -*- coding: utf-8 -*-

from PIL import Image
import re
import string
import base64
import requests
import pytesseract


def check_valid(text):
    '''检查识别的字符是否有效，如果有效则返回识别字符，无效则返回None'''
    def extract_valid_chars(text):
        '''提取有效字符，像￥……*#￥之类的字符将被忽略'''
        text = text.lower()
        valid_chars = string.digits + string.ascii_lowercase
        for c in text:
            if not c in valid_chars:
                text = text.replace(c, '')
        return text

    patten = '^[0-9a-z]{4}$'
    regex = re.compile(patten)

    code = extract_valid_chars(text)
    is_valid = regex.match(code)

    # 如果is_valid是False 的话，代表我们获取的验证码并不符合要求，因此返回None
    if is_valid:
        return code
    else:
        return None


def ocr_with_baidu(f_name):
    with open(f_name, 'rb') as input_file:
        img_base64 = base64.b64encode(input_file.read())
    url = 'http://apis.baidu.com/apistore/idlocr/ocr'
    data = {'fromdevice': "pc", 'clientip': "10.10.10.0",
            'detecttype': "LocateRecognize",
            'languagetype': "CHN_ENG", 'imagetype': "1", 'image': img_base64}
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "apikey": 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        # 在这里填写你自己的apikey
    }
    req = requests.post(url, data, headers=headers)
    resp = req.json()

    words = [i['word'] for i in resp['retData']]
    text = ''.join(words)
    return check_valid(text)


def ocr(f_name):
    im = Image.open(f_name)
    im = im.convert('L')
    # 先将图像二值化处理，有助于提升识别效果。
    text = pytesseract.image_to_string(im)
    return check_valid(text)


if __name__ == '__main__':
    print(ocr('image.jpg'))
    print(ocr_with_baidu('image.jpg'))
