#encoding=utf-8
import json
import requests

from API_test.Utils.logger import Logger


class BaseApi:

    logger = Logger()
    def __init__(self):
        # self.token = self.get_token()  #用不着  就注释了 省的这个方法要执行一遍
        self.mail_token = self.get_mail_token()

    #
    def get_token(self):
        """获取token"""
        corpid = 'ww3ad1d98f7b75e8c6'
        corpsecret = 'T5IMG_1NzwXl4H3ALsE4OoUZOVuPXVstWT3UeDF49V0'
        # r = requests.get(
        #     'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        #     params={'corpid': corpid, 'corpsecret': corpsecret}
        # )
        data={
            "method": "get",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            "params": {'corpid': corpid, 'corpsecret': corpsecret}
        }
        r = self.send(data)
        # Logger().info(f'r:{r.json()}')
        self.logger.info(f'r:{r.json()}')
        # print('r:',r.json())
        token = r.json()['access_token']
        Logger().info(f'获取的token:{token}')
        return token


    def get_mail_token(self):
        """获取通讯录的Secret"""
        corpid =  'ww3ad1d98f7b75e8c6'
        corpsecret  = 'Mbq6tbs5vG5yUTgrUoOtkTu4gZK8KoOPXpvL4vunqpQ'

        data = {
            "method": "get",
            "url":'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            "params": {'corpid': corpid, 'corpsecret': corpsecret}
        }
        r = self.send(data)
        token = r.json()['access_token']
        # Logger().logger.info(f'获取的mail_token:{token}')
        return token

    # def send(self, kwargs):
    #     """对请求方法的改造"""
    #     r = requests.request(**kwargs)   #requests.request()是get、post等底层实现，详情见源码
    #     print(json.dumps(r.json(), indent=2))
    #     return r

    @staticmethod
    def send(kwargs):
        r = requests.request(**kwargs)
        # print(f'url: {r.url}')
        # print(f'params: {kwargs["params"]}')
        if 'json' in kwargs:
            print(f'json: {kwargs["json"]}')
            # Logger().debug(f'json: {kwargs["json"]}')
        # print(json.dumps(r.json(), ensure_ascii=False, indent=4))
        Logger().info(json.dumps(r.json(), ensure_ascii=False, indent=4))
        return r

    # params = {}
    # def send(self, data):
    #     """数据驱动:转化数据 """
    #     raw_data = json.dumps(data)  # json-->str
    #     for key, value in self.params.items():
    #         raw_data = raw_data.replace("&{" + key + "}", value)  # 什么意思
    #     data = json.loads(raw_data)  # 当前是dict格式
    #     return requests.request(**data).json()  # **data:**可以解析字典，以键值对形式


