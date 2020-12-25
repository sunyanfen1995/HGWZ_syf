#encoding=utf-8

from API_test.Api.base_api import BaseApi
from API_test.Utils.logger import Logger
from API_test.Utils.utils import Utils


class Member(BaseApi):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        # self.logger = Logger()

    def add(self,userid,name,mobile,department=None,**kwargs):
        """添加成员"""
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {
                'access_token': self.mail_token
            },
            "json":
                {
                    "userid": userid,
                    "name": name,
                    "mobile": mobile,
                    "department": department,
                     **kwargs
                }
                     }
        r = self.send(data)
        return r


    #错误代码：60111  userid not found
    def list(self,userid):
        """
        获取成员列表
        :userid
        :return:
        """
        data={
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
             "params": {
                'access_token': self.mail_token,
                 'userid': userid,

                 #【注意点】如果把这个参数通过json传入，会提示该参数无效，实质是没有传进来，这是为什么么？
                 #通过json传进来是dict类型{userid:syf1}  通过params传进来是str 为'syf1'
            },
            # "json": {
            #      'userid': userid
            # }
        }
        r = self.send(data)
        return r


    #错误代码：60111userid not found
    #错误代码：301005  not allow del corp creator
    def delete(self,userid):
        """删除接口"""
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params": {
                'access_token': self.mail_token,
                'userid': userid
            }
        }
        r = self.send(data)
        return r

    def batchdelete(self,useridlist):
        """
        批量删除接口"
        :param useridlist:  用户列表
        :return:
        """
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete",
            "params": {
                'access_token': self.mail_token
            },
            "json": {
                'useridlist': useridlist
            }
        }
        r = self.send(data)
        return r

    # userid和mobile是唯一的，不能重复
    # 错误代码：40066  invalid party list
    #错误代码：60104  "errmsg": "mobile existed:syf1"
    # 错误代码：60102  "errmsg": "userid existed

    def add_and_detect(self, userid, name, mobile, department,**kwargs):
        """添加成员前检验"""
        r = self.add(userid, name, mobile, department,**kwargs)
        if r.status_code == 200 and r.json()['errcode'] == 60102:
            # userid 已经存在，则直接删除 后添加
            print('userid existed, goto delect')
            # self.logger.info('userid existed, goto delect')

            self.delete(userid)
            # 确认删除成功
            assert self.list(userid).json()['errcode'] == 60111
            # self.logger.debug('userid already delected')
            print('userid already delected')
            # 递归该方法
            return self.add_and_detect(userid, name, mobile, department, **kwargs)

        elif r.status_code == 200 and r.json()['errcode'] == 60104:
            # mobile 手机号码存在，则进行加+1,再重新请求
            print('mobile existed, goto update mobile')
            # self.logger.debug('mobile existed, goto update mobile')
            new_mobile = self.utils.update_mobile(mobile=mobile)
            print(f"new_mobile:{new_mobile}")
            # self.logger.debug(f"new_mobile already get:{new_mobile}")
            return self.add_and_detect(userid=userid, name=name, mobile=new_mobile, department=department, **kwargs)
        elif r.status_code !=200:
            # self.logger.debug(f'requests not success:{r.status_code}')
            return False
        print('userid already add success')
        return r


    def delect_and_detect(self, userid):
        """删除并检测"""
        r = self.delete(userid)
        #如果指定的userid没有
        if r.status_code == 200 and r.json()['errcode'] == 60111:
            print('userid not found, goto add')
            # self.logger.debug('userid not found, goto add')
            if self.add_and_detect(userid=userid, name='Delect', mobile= '173064004322', department=[1]).json()['errmsg'] == "created":
                return self.delect_and_detect(userid)
        elif r.status_code !=200:
            # self.logger.debug(f'requests not success:{r.status_code}')
            return False
        return r


    def create_userlist(self,userid, name, mobile, department,**kwargs):
        """创建userlist并返回结果"""
        userlist = []
        if self.add_and_detect(userid, name, mobile, department,**kwargs).json()['errmsg'] == "created":
            userlist.append(userid)
        return userlist

    def bashdelect_and_detect(self, list):
        """批量删除并检测"""

        #依次查询列表中的userid,如果存在则放入新的list中；
        detected_userlist = [userid for userid in list if self.list(userid).json()['errcode'] != 60111]
        # self.logger.debug(f'detected_userlist:{detected_userlist}')
        print(f'detected_userlist:{detected_userlist}')
        return self.batchdelete(detected_userlist)









