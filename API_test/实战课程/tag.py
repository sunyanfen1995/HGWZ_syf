#encoding=utf-8
import requests

import time


class Tag:

    #token 供后面直接调用
    #方法1：使用类变量
    # token = None
    #方法2：初始化
    def __init__(self):
        self.token = self.get_token()
    def get_token(self):
        """获取token"""
        corpid = 'ww3ad1d98f7b75e8c6'
        corpsecret = 'T5IMG_1NzwXl4H3ALsE4OoUZOVuPXVstWT3UeDF49V0'
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={'corpid': corpid, 'corpsecret': corpsecret}
        )
        token = r.json()['access_token']
        return token

    def list(self):
        """查询全部标签"""
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={
                'access_token': self.token
            },
            json={
                'tag_id': []  # 结构化数据，把json对象自动转化成字符串类型的内容
            }
        )
        return r
    def updata(self, id, tag_name):
        """编辑标签"""

        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            params={
                'access_token': self.token
            },
            json={
                'id': id,  # tag id
                'name': tag_name  # tag_name
            }
        )
        return r

    def add(self,group_name, tag_name):
        """添加标签"""
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
                          params={
                              'access_token': self.token
                          },
                          json={
                              "group_name": group_name,
                              "order": 1,
                              "tag": [{
                                  "name": tag_name
                              }
                              ]
                          }
        )
        return r

    def delect(self,group_id: list=None ,tag_id: list=None):
        """删除标签或者组"""
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
                          params={
                              'access_token': self.token
                          },
                          json={
                              "tag_id": tag_id,
                             "group_id":group_id
                                }
                         )
        return r





