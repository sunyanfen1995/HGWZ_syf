#encoding=utf-8
import jsonpath
import pytest

from API_test.Api.member import Member
from API_test.Utils.utils import Utils

import allure
@allure.feature("通讯录管理--成员管理子模块") #功能点描述
class Test_member():

    def setup_class(self):
        self.member = Member()
        self.data = Utils().get_data_from_yaml()
        self.userid = self.data['userid']
        self.name = self.data['name']
        self.mobile = self.data['mobile']
        self.department = self.data['department']
        # self.userid = "sanzhang"
        # self.name = "ZhangSan"
        # self.mobile = '17300000001'
        # self.department = [1]


    @pytest.mark.run(1)
    @pytest.mark.skip
    @allure.title('添加成员接口')
    def test_add(self):
        # userid = "syf1"
        # name = "sunyanfen"
        # mobile = '17306401210'
        r = self.member.add(self.userid, self.name, self.mobile,self.department)
        assert r.status_code==200
        assert r.json()['errmsg'] == "created"

    @pytest.mark.run(2)
    @pytest.mark.skip
    @allure.title('查询成员接口')
    def test_list(self):
        """测试：查询接口"""
        # userid = "syf2"
        # r = self.member.list(self.userid)
        r = self.member.list('sanzhan11g')
        assert r.status_code == 200
        # assert jsonpath.jsonpath(r.json(), "$.userid")[0] == self.userid   #注意点：jsonpath.jsonpath(r.json(), "$.userid") 最终类型是list
        assert jsonpath.jsonpath(r.json(), "$.userid")[0] == 'sanzhan11g'   #注意点：jsonpath.jsonpath(r.json(), "$.userid") 最终类型是list

    @pytest.mark.run(3)
    @pytest.mark.skip
    @allure.title('删除成员接口')
    def test_delect(self):
        """测试删除接口"""
        userid = "syf1"
        r = self.member.delete(self.userid)
        assert r.status_code== 200
        assert r.json()['errmsg'] == 'deleted'

    @pytest.mark.skip
    @allure.title('添加成员接口：异常情况检测（组合）')
    def test_add_and_detect(self):
        """测试：添加前检测"""
        r = self.member.add_and_detect(self.userid,self.name,self.mobile,self.department)
        assert r.json()['errmsg'] == "created"

    @pytest.mark.skip
    @allure.title('删除成员接口：异常情况检测（组合）')
    def test_delect_and_detect(self):
        """测试：删除前先确认"""
        r = self.member.delect_and_detect(self.userid)
        assert r.json()['errmsg'] == "deleted"

    @pytest.mark.skip
    @pytest.mark.parametrize('id',['syf1', 'syf2', 'syf3'])
    @allure.title('批量删除成员接口：异常情况检测（组合）')
    def test_batchdelect(self,id):
        """批量删除"""
        userlist = self.member.create_userlist(userid=id , name=self.name, mobile=self.mobile,department=self.department)
        r = self.member.bashdelect_and_detect(userlist)
        assert r.json()['errmsg'] == "deleted"

    # def test_batchdelect(self):
    #     r = self.member.bashdelect_and_detect(list=['syf1'])
    #     print(r.json())
    #     assert r.json()['errmsg'] == "deleted"













if __name__ == '__main__':
    pytest.main(['-v','-s','test_member.py'])
