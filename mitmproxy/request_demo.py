#encoding=utf-8

"""
增加请求头参数
"""
from mitmproxy import http

#request 方法名称不能修改，否则无法失败，其他插件也是同理
def request(flow: http.HTTPFlow):   #flow就是mitmdump抓到的数据，
    flow.request.headers["myheader"] = "syf"
    print(flow.request.headers)
