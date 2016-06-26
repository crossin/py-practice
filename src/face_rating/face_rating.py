# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import requests
import base64
import time
import re


class XiaoBingV3:
    """ 这次我们采用了面向对象的方法来设计程序。
        微软的小冰系统可不止只有打分系统，但是目前我们只实现了打分功能，
        如果有兴趣的话，还可以将其他的功能也都实现，只要扩展这个类即可。
    """

    def __init__(self):
        """__init__"""
        self.upload_url = 'http://kan.msxiaobing.com/Api/Image/UploadBase64'
        self.comp_url = 'http://kan.msxiaobing.com/Api/ImageAnalyze/Process'
        # 这是我们通过分析http包，得到的请求地址

    def _get_raw_img_url(self, in_file):
        """ 打分系统只支持对一个图片网址打分，并不支持原始图片格式。
            因此我们需要先将图片上传，并获取图片的网址，以供打分使用。
            显然，这个过程应该是对用户透明的，因此我将其定义为内部方法。
        """
        with open(in_file, 'rb') as f_stream:
            img_base64 = base64.b64encode(f_stream.read())

        resp = requests.post(self.upload_url, data=img_base64)
        return 'http://imageplatform.trafficmanager.cn' + resp.json()['Url']

    def _get_judgements(self, img_url):
        """ 传入一个图片地址，返回小冰对它的评语。
        """
        sys_time = int(time.time())
        payload = {'service': 'yanzhi',
                   'tid': '04a01fbe5f5c4b7496034ad9cf41ff01'}
        form = {  # don't ask me why, it's just magic numbers~
            'msgId': str(sys_time) + '233',
            'timestamp': sys_time,
            'senderId': 'mtuId' + str(sys_time - 242) + '717',
            'content[imageUrl]': img_url,
        }
        # 这里许多参数都没有实际意义，只是为了模仿真实用户请求。
        resp = requests.post(self.comp_url, params=payload, data=form)
        return resp.json()['content']['text']

    @staticmethod
    def _extract_point(text):
        """ 从返回的评语中，提取出分数，并按照百分制返回。
        """
        match = re.search(r'\d\.?\d?', text)
        # 使用正则表达式，提取出分数，并转换为百分制。
        point_str = match.group(0)
        return int(float(point_str) * 10)

    def rank(self, input_, is_num=False):
        """ 
            这是我们目前对外提供的唯一接口。
            给定输入文件地址，返回其打分结果，如果想要数字格式的分数，
            只要将`is_num`参数设为True即可。
        """
        raw_url = self._get_raw_img_url(input_)

        judgement = self._get_judgements(raw_url)
        if is_num:
            return self._extract_point(judgement)
        return judgement


if __name__ == '__main__':
    xb = XiaoBingV3()
    print(xb.rank('Lenna.png', is_num=False))
