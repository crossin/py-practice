# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import random
import requests


def get_city_id(city_name):
    '''获取城市的id，为后边的做准备'''
    city_url = 'http://apis.baidu.com/baidunuomi/openapi/cities'
    headers = {'apikey': '14cdd85738c717e546a5b6852c3e1631'}

    r = requests.get(city_url, headers=headers)
    cities = r.json()['cities']
    for city in cities:
        # 注意此处没有使用`==`，而是使用了`in`
        if city_name in city['city_name']:
            return city['city_id']
    # 如果找到输入的城市，则返回城市的id，如果没找到，就退出
    print('city not found')
    assert 0


def get_shops_list(city_id, keyword, location):
    shops_url = 'http://apis.baidu.com/baidunuomi/openapi/searchshops'
    headers = {'apikey': '14cdd85738c717e546a5b6852c3e1631'}
    payload = {'city_id': city_id, 'location': location,
               'keyword': keyword, 'sort': 4}
    ''' 获取给定关键词搜索到的店铺的名称，并按照销量排序，
        此处输入了位置信息，输入自己所在的坐标即返回自己附近的餐馆
        还有很多可选参数，请参考：
        http://apistore.baidu.com/apiworks/servicedetail/508.html
    '''
    r = requests.get(shops_url, params=payload, headers=headers)
    return r.json()['data']['shops']


def get_all_deals(shop_list):
    deal_list = []
    for shop in shop_list:
        for deal in shop['deals']:
            deal_list.append([deal['title'],
                              deal['description'],
                              deal['promotion_price'] / 100,
                              deal['score']])
            # 在一大堆信息中，我们只选取了餐馆的名字、描述、价格和评分
    return deal_list

if __name__ == '__main__':
    city_id = get_city_id('南京')
    shop_list = get_shops_list(city_id, '黄焖鸡', '32.0219605,118.7987918')
    deal_list = get_all_deals(shop_list)
    # 搜索南京市给定位置附近销量大的黄焖鸡
    print(random.choice(deal_list))
    # 随机选一个团购单下单吧！
