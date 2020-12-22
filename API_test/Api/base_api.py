#encoding=utf-8
import json
import requests

from API_test.Utils.logger import Logger


class BaseApi:

    logger = Logger()
    def __init__(self):
        self.token = self.get_token()
        self.mail_token = self.get_mail_token()


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
        Logger().info(f'r:{r.json()}')
        self.logger.info(f'r:{r.json()}')
        # print('r:',r.json())
        token = r.json()['access_token']
        Logger().info(f'token:{token}')

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
        Logger().logger.info(f'token:{token}')
        assert r.status_code == 200
        return token

    # def send(self, kwargs):
    #     """对请求方法的改造"""
    #     r = requests.request(**kwargs)   #requests.request()是get、post等底层实现，详情见源码
    #     print(json.dumps(r.json(), indent=2))
    #     return r

    @staticmethod
    def send(kwargs):
        r = requests.request(**kwargs)
        Logger().info(f'url: {r.url}')
        Logger().info(f'params: {kwargs["params"]}')
        # print(f'url: {r.url}')
        # print(f'params: {kwargs["params"]}')
        if 'json' in kwargs:
            # print(f'json: {kwargs["json"]}')
            Logger().debug(f'json: {kwargs["json"]}')
        # print(json.dumps(r.json(), ensure_ascii=False, indent=4))
        Logger().info(json.dumps(r.json(), ensure_ascii=False, indent=4))

        return r


