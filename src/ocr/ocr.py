from PIL import Image
import re
import string
import base64
import requests
import pytesseract


def check_valid(text):
    def extract_valid_chars(text):
        '''extract valid chars, like 1 0 a b, $#^) will be dismissed'''
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

    # if is_valid is False, means we get a wrong code
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
        # replace xxxx with your own apikey
    }
    req = requests.post(url, data, headers=headers)
    resp = req.json()

    words = [i['word'] for i in resp['retData']]
    text = ''.join(words)
    return check_valid(text)


def ocr(f_name):
    im = Image.open(f_name)
    # Binarization
    im = im.convert('L')
    text = pytesseract.image_to_string(im)
    return check_valid(text)


if __name__ == '__main__':
    print(ocr('image.jpg'))
    print(ocr_with_baidu('image.jpg'))
