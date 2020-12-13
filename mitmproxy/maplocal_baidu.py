#encoding=utf-8

"""
实现map local
"""
from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    # 判断url是不是预期的url，如下百度首页
    if flow.request.pretty_url == "https://www.baidu.com/":
        # url符合预期，则创建一个response
        flow.response = http.HTTPResponse.make(
            200,  # (optional) status code
            b"Hello World",  # (optional) content
            {"Content-Type": "text/html"}  # (optional) headers
        )
