# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import requests


def search_by_bing(key_word='python', search_type='webpage', count_=10):
    _api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
    # 这里填写你的 api-key, 注意要填 Bing Search 的api-key
    params = {'q': key_word, 'count': count_}
    # 构造查询参数，`q`是必选，其他的可选参数，我们只设置了一个。
    headers = {'Ocp-Apim-Subscription-Key': _api_key}

    def search_webpages(key_word):
        _url = 'https://api.cognitive.microsoft.com/bing/v5.0/search'
        resp = requests.get(_url, params=params, headers=headers)

        results = {}
        web_pages = resp.json()['webPages']['value']
        for page in web_pages:
            # 我们根据返回的数据的格式，从中抽取我们需要的`标题-链接`
            results[page['name']] = page['displayUrl']
        return results

    def search_images(key_word):
        # 这个函数和上面的函数是完全类似的，但是由于两者的搜索接口不同，所以要分别实现。
        _url = 'https://api.cognitive.microsoft.com/bing/v5.0/images/search'
        resp = requests.get(_url, params=params, headers=headers)

        results = {}
        images = resp.json()['value']
        for img in images:
            results[img['name']] = img['contentUrl']
        return results

    search_func = {'webpage': search_webpages,
                   'image': search_images}
    # 这个dict的value是函数，这样我们可以自由切换搜索模式，这也是Python中函数作为“一等公民”的体现。
    # 如果还要搜索“news”的话，只要增加一项即可，本函数的接口不会发生任何变化。
    return search_func[search_type](key_word)


if __name__ == '__main__':
    res = search_by_bing('java', 'webpage')
    # 返回我们搜索的结果。
    for k, v in res.items():
        print('name:', k)
        print('url:', v)
