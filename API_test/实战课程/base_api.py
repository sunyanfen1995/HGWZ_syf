#encoding=utf-8
import json
import requests


class BaseApi:

    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        """获取token"""
        corpid = 'ww3ad1d98f7b75e8c6'
        corpsecret = 'T5IMG_1NzwXl4H3ALsE4OoUZOVuPXVstWT3UeDF49V0'
        # r = requests.get(
        #     'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        #     params={'corpid': corpid, 'corpsecret': corpsecret}
        # )
        data={
            "method":"get",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            "params": {'corpid': corpid, 'corpsecret': corpsecret}
        }
        r = self.send(data)
        token = r.json()['access_token']
        return token

    def send(self, **kwargs):
        """对请求方法的改造"""
        r = requests.request(**kwargs)   #requests.request()是get、post等底层实现，详情见源码
        print(json.dumps(r.json(), indent=2))
        return r

