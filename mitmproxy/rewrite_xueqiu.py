#encoding=utf-8
import json
from mitmproxy import http

"""
实现rewrite功能
"""

def response(flow: http.HTTPFlow):
    # 加上过滤条件
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 把响应数据转化成python对象，保存到data中
        data = json.loads(flow.response.content)
        # 修改第一支股票的名称
        print(data)
        # data['data']['items'][0]['quote']['name'] = "hogwarts000000001"
        # data['data']['items'][1]['quote']['current'] = 0.1
        # second_stock_name = data['data']['items'][1]['quote']['name']
        data['data']['items'][1]['quote']['name'] *= 2
        data['data']['items'][2]['quote']['name'] = ''

        # 把修改后的内容赋值给 response 原始数据格式,data变成字符串
        flow.response.text = json.dumps(data)

