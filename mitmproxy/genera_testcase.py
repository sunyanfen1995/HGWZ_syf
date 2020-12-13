#encoding=utf-8
"""
批量生成等价类用例
"""
import json
from mitmproxy import http

rult = [1, 3, 5, 100]
#统计url
url_index = dict()
def response(flow: http.HTTPFlow):
    # 拿到请求的url
    url =flow.request.url.split('.json')[0]
    #
    if url not in url_index.keys():
        url_index[url] = 0
    else:
        url_index[url] += 1

    seed = url_index[url] % len(rult)


# 加上过滤条件
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 把响应数据转化成python对象，保存到data中
        data = json.loads(flow.response.content)

        # 对数据进行批量修改
        #data_new = json_travel(data, text=2)
        data_new = json_travel(data, text= rult[seed])
        #传值
        flow.response.text = json.dumps(data_new)



#实现批量修改
# 类型： dict\ list\ string\ int\ float
def json_travel(data, array=None, text=1, num=1):
    """
    #实现json数据的倍数操作
    :param data:  要修改的内容
    :param array:  列表的修改规则  为none默认不修改
    :param text:    字符串的修改规则  为1默认不修改
    :param num:     整型或浮点型的修改规则  为1默认不修改
    :return: data_new
    """
    #定义返回的数据

    data_new = None
    # 判断传入data的类型
    #如果是字典
    if isinstance(data, dict): #判断一个对象是否是一个已知的类型，类似 type()。
        #把修改后的数据定义为字典类型
        data_new = dict()
        #对传入的响应数据继续遍历
        for key, value in data.items():
            # 每一个key 对应的value， 需要对value再调用json_travel进行遍历（如果不了解，可以写个字典的数据看下）
            data_new[key] = json_travel(value, array, text, num)  #递归遍历字典
    #如果是list
    elif isinstance(data, list):
        data_new = list()
        # 遍历list中的全部元素，同理dict
        for item in data:
            item_new = json_travel(item, array, text, num)
            #如果传入的array为空，则对列表元素不进行处理
            if array is None:
                data_new.append(item_new)
            else:
                # 判断传入的array值是否满足修改规则
                # 如果传入的array是整数 且 大于0
                if isinstance(array, int) and array >=0:
                    #对每个元素进行加倍
                    for i in range(array):
                        data_new.append(item_new)
                else:
                    #不满足修改规则，则不用修改
                    data_new = data
    # 如果是string类型
    elif isinstance(data, str):
        #如果 text是正整数
        if isinstance(text, int) and text>= 0:
            #对字符串做加倍操作
            data_new = data * text
        else:
            data_new = data
    # 如果是int 或者 float 这样的数字
    elif isinstance(data, int) or isinstance(data, float):
        #对数字做乘积运算
        data_new = data * num
    # 其他数据类型保持原样
    else:
        data_new = data

    return data_new


def json_travel_demo(data, array=None, text=1, num=1):
    """
    完成json数据的倍数操作
    :param data: 要修改的内容
    :param array: 列表的修改规则，为None默认不修改
    :param text: 字符串的修改规则，为1默认不修改
    :param num: 整数或者浮点数的修改规则，为1默认不修改
    :return: data_new
    """
    print('1111')
    # 定义返回的数据
    data_new = None

    # 判断传入data的类型
    if isinstance(data, dict):
        # 把修改后的数据定义为一个空字典
        data_new = dict()

        # 对传入的响应数据进行遍历
        for k, v in data.items():
            # 每一个key所对应的value，也就是v传入的json_travel继续处理
            data_new[k] = json_travel(v, array, text, num)

    # 如果是列表，对列表的每一项进行遍历
    elif isinstance(data, list):
        data_new = list()

        # 遍历列表中的所有元素
        for item in data:
            item_new = json_travel(item, array, text, num)

            # 如果传入的array为空，对列表的元素不做处理
            if array is None:
                data_new.append(item_new)
            else:
                # 判断传入的array修改规则，是否可以正常修改
                if isinstance(array, int) and array >= 0:
                    # 对每一个元素进行加倍修改
                    for i in range(array):
                        data_new.append(item_new)
                else:
                    data_new = data

    # 如果是字符串
    elif isinstance(data, str):
        # 如果 text 为正整数
        if isinstance(text, int) and text >= 0:
            # 对于字符串做加倍操作
            data_new = data * text
        else:
            data_new = data

    # 如果是int或者float这样的数字
    elif isinstance(data, int) or isinstance(data, float):
        # 对数字做乘积运算
        data_new = data * num

    # 其他数据类型保持原样
    else:
        data_new = data

    return data_new

