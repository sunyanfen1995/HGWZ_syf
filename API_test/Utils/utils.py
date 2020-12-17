#encoding=utf-8
import yaml

import os


class Utils:

    def get_token(self):
        """获取token"""
        pass

    def get_data_from_yaml(self):
        """从yaml中读取测试数据"""
        with open('../Data/member.yaml',encoding='utf-8') as f:
            data = yaml.load(f)
            return data['Test_data']

    def update_mobile(self,mobile):
        """更细手机号:进行+1处理"""
        return str(int(mobile)+1)

    #todo：schema的二次封装
    def json_schema(self,response):
        """对返回结果进行格式检验"""
        pass


