#encoding=utf-8
import json
import requests

import time

from API_test.实战课程.base_api import BaseApi


class Tag(BaseApi):

    #token 供后面直接调用
    #方法1：使用类变量
    # token = None
    #方法2：初始化
    # def __init__(self):
    #     super.__init__()  #继承父类的init 方法来获取token
        # self.token = self.get_token()

    def __init__(self):
        super().__init__()
    # def get_token(self):
    #     """获取token"""
    #     corpid = 'ww3ad1d98f7b75e8c6'
    #     corpsecret = 'T5IMG_1NzwXl4H3ALsE4OoUZOVuPXVstWT3UeDF49V0'
    #     r = requests.get(
    #         'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
    #         params={'corpid': corpid, 'corpsecret': corpsecret}
    #     )
    #     token = r.json()['access_token']
    #     return token

    def list(self):
        """查询全部标签"""
        # r = requests.post(
        #     'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        #     params={
        #         'access_token': self.token
        #     },
        #     json={
        #         'tag_id': []  # 结构化数据，把json对象自动转化成字符串类型的内容
        #     }
        # )

        data = {
            "method": "post",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            "params": {
                'access_token': self.token
            },
            "json": {
                 'tag_id': []
            }
        }
        r = self.send(data)
        print(json.dumps(r.json(), indent=2))
        return r

    def updata(self, id, tag_name):
        """编辑标签"""

        # r = requests.post(
        #     'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
        #     params={
        #         'access_token': self.token
        #     },
        #     json={
        #         'id': id,  # tag id
        #         'name': tag_name  # tag_name
        #     }
        # )
        data = {
            "method": "post",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            "params": {
                'access_token': self.token
            },
            "json": {
                'id': id,  # tag id
                'name': tag_name  # tag_name
            }
        }
        r = self.send(data)
        print(json.dumps(r.json(), indent=2))
        return r

    def find_group_id_by_name(self,group_name):
        """ 判断group_name是否存在，不存在则抛异常"""
        for group in self.list().json()['tag_group']:
            if group_name in group['group_name']:
                return group['group_id']
        print('group name not in group')   # todo: 替换成logging
        return ""
        #raise ValueError('group name not in group')  #思考：为什么不是return False？因为当group_id是“”，也是会等效于False

    def is_group_id_exist(self, group_id):
        """查询group_id是否存在"""
        for group in self.list().json()['tag_group']:
            if group_id in group['group_id']:
                return True
        print('group id not in group')   # todo: 替换成logging
        return ""

    def add(self,group_name, tag_name, **kwargs):   #**kwargs 代表其他非必要字段
        """添加标签"""
        # r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
        #                   params={
        #                       'access_token': self.token
        #                   },
        #                   json={
        #                       "group_name": group_name,
        #                       "tag":tag_name
        #                       **kwargs
        #                   }
        # )
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "params": {"access_token": self.token},
            "json": {"group_name": group_name,
                     "tag": tag_name,
                     **kwargs
                     }}
        r = self.send(data)
        print(json.dumps(r.json(), indent=2))
        return r

    def add_and_detect(self,group_name, tag_name, **kwargs):
        """添加的数据如果存在，则删除，起到数据清理的作用"""
        r = self.add(group_name, tag_name, **kwargs)
        # 40071 元素存在
        if r.status_code==200 and r.json()['errcode'] =='40071':
            group_id = self.find_group_id_by_name(group_name)
            if not group_id:
                return ""
            self.delect_group(group_id)
            self.add(group_name, tag_name, **kwargs)
        result = self.find_group_id_by_name(group_name)

        return result






    #查询tag_id--->删除tag_id
    #如果正常，返回成功；如果异常，手动获取
    # 注意点： tag_id 和 group_id有一个有问题的话  那这个请求就不会成功
    def delect_group(self,group_id):

        """删除组"""
        # r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
        #                   params={ 'access_token': self.token},
        #                   json={"group_id":group_id }
        #                  )

        data = {
            "method": 'post',
            "url":"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {
                'access_token': self.token
            },
            "json": {
                "group_id": group_id
            }
        }
        r = self.send(data)
        print(json.dumps(r.json(), indent=2))
        return r


    def delect_tag(self,tag_id):

        """删除标签"""
        # r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
        #                   params={ 'access_token': self.token},
        #                   json={"group_id":tag_id }
        #                  )

        data = {
            "method": "post",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            "params": {
                'access_token': self.token
            },
            "json": {
                "group_id": tag_id
            }
        }
        r = self.send(data)
        print(json.dumps(r.json(), indent=2))
        return r

    #思路：可以指定一个group_id，如果不存在，则生成一个
    def delect_and_detect_group(self,group_ids):
        """删除并查询group"""
        delect_group_ids= []
        r = self.delect_group(group_ids)
        if r.json()['errcode'] == 40068:  #非法的id
            for group_id in group_ids:  #这边考虑到删除接口中可以传入多个group_id，所以要多一层判断
                # 如果不存在，则生成一个；如果存在 就直接存入列表中
                if not self.is_group_id_exist(group_id):
                    print("新添加一个group_id")
                    group_id = self.add_and_detect("TMP00123", [{"name":"tag123"}])
                    delect_group_ids.append(group_id)  #将group_id追加到列表中
                else:
                    delect_group_ids.append([group_id])
        r = self.delect_group(delect_group_ids)
        print('最后删除的结果是：',r.json())
        return r












