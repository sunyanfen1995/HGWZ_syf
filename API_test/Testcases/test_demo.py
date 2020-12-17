#encoding=utf-8
import json
import requests

import os


# def test_get_token():
#     corpid = 'ww3ad1d98f7b75e8c6'
#     corpsecret = 'Mbq6tbs5vG5yUTgrUoOtkeiZ7jEYRGyuTjXAiU-6Fiw'
#     r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
#                      params={
#                          'corpid':'ww3ad1d98f7b75e8c6',
#                         'corpsecret':'Mbq6tbs5vG5yUTgrUoOtkeiZ7jEYRGyuTjXAiU-6Fiw'
#                      }
#                      )
#     print(json.dumps(r.json(), indent=2))
#     token = r.json()['access_token']
#     return token



def test_update_mobile(moble='17306400329'):
        """更细手机号"""
        # return str(int(moble)+1)
        print(str(int(moble) + 1))
        print(type(str(int(moble) + 1)))

