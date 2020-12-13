#encoding=utf-8

"""
实现map local
"""
from mitmproxy import http


def request(flow: http.HTTPFlow):
    #修改判断条件
    if 'quote.json' in flow.request.pretty_url:
        # 打开本地的数据文件：
        with open("D:\\python_learn\\HGWZ_ceshikaifa\\mitmproxy\\quote.json", encoding= 'utf-8') as f:
            # url符合预期，则创建一个response
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(), # 读取文件内容
                {"Content-Type": "application/json"}  # 指定返回数据的格式：json
            )

