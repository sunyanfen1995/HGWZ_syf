#encoding=utf-8
""""企业微信客户标签管理"""

import jsonpath
import time
from API_test.Actual_Practice.Api.tag import Tag
import pytest

#todo:底层具体的实现框架代码耦合严重，无法适用变化，比如公司切换了协议，如pb、dubbo
#todo:代码冗余，需要封装
#todo：无法清晰的描述业务
#todo：使用jasonpath表达更灵活的递归过滤


class TestTag():
    def setup_class(self):
        #实例化一次Tag类即可，后面用例中直接调用
        self.tag = Tag()
        # self.group_name = 'python_15'
        # self.group_id = []  #et_N2IEQAAaY8EqZVkcCLi5XbgXvpWbA

    # def teardown(self):
    #     """数据清理,删除指定的组"""
    #     # group_id= jsonpath.jsonpath(self.tag.list().json(), '$..group_id')[0]
    #     # assert self.tag.delect(self.group_id).status_code ==200
    #     pass

    # @pytest.mark.parametrize('tag_id,tag_name',(
    #                          ['et_N2IEQAAcCOHbiU0fku2VJis3Xfdgw', 'tag1_new'],
    #                          ['et_N2IEQAAcCOHbiU0fku2VJis3Xfdgw', 'tag1_中文'],
    #                          ['et_N2IEQAAcCOHbiU0fku2VJis3Xfdgw', 'tag1_@@@@']
    #                                              )
    #                          )
    # def test_tag_list(self, tag_id, tag_name):
    #     group_name = 'python'
    #     tag_name= tag_name + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    #     self.tag.updata(id =tag_id, tag_name= tag_name)
    #     r = self.tag.list()
    #     tags =[
    #         tag
    #         for group in r.json()['tag_group'] if group['group_name']==group_name
    #         for tag in group['tag'] if tag['name'] == tag_name
    #     ]
    #     assert tags != []
    #     assert jsonpath.jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]") is not None
    #     assert jsonpath.jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name
    #

    def test_tag_list_fail(self):
        pass

    #作业：
    # 新增标签
    # 删除标签
    # 数据清理

    #报错：40014 无效的token
    #报错：40071 tag name 已经存在   处理方案：1.删除对应tag（推荐）；  2.在已有tag_name的基础上追加名字（时间戳，手写计数器）

   # @pytest.mark.parametrize('tag_name',['tag_add_abc4','tag_add_中文4','tag_add_@@@4'],ids=['添加字母','添加中文','添加字符'])
    @pytest.mark.skip
    def test_tag_add(self):
        """创建全新的组和标签"""
        group_name = 'python_1212'
        tag_name = [
            {"name":"tag1"},
            {"name":"tag2"},
            {"name":"tag3"}
        ]
        tag_name = tag_name + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        r= self.tag.add(group_name=group_name, tag_name= tag_name)
        assert r.status_code == 200
        assert tag_name in jsonpath.jsonpath(r.json(), '$..name')

    @pytest.mark.skip
    def test_add_and_detect(self):
        # todo: 测试数据要放到数据文件中
        group_name = 'python_1212'
        tag_name = [
            {"name": "tag1"},
            {"name": "tag2"},
            {"name": "tag3"}
        ]
        r = self.tag.add_and_detect(group_name, tag_name)
        print(r)
        assert r

    # 报错：40068 非法的tag_id
    # 0.添加tag
    # 1.如果删除tag有问题，
    # 2.再次进行重试（重试次数：n）  手动执行：需要借助pytest的钩子（rerun插件）
    #   a. 添加一个接口
    #   b. 对新添加的接口进行删除
    #   c. 查询删除的结果
    @pytest.mark.skip
    def test_delect_tag(self):
        """删除指定tag_id"""
        print(self.tag.list().json())
        tag_id = jsonpath.jsonpath(self.tag.list().json(), '$..id')[0]
        # tag_id='et_N2IEQAA59aBAEJdui6_DGm0RU5k5A'
        r = self.tag.delect_tag(tag_id)
        assert r.status_code == 200
        assert tag_id not in jsonpath.jsonpath(self.tag.list().json(), '$..id')

    # @pytest.mark.skip
    def test_delete_and_detect_group(self):
        r= self.tag.delect_and_detect_group(['xxxxx'])
        assert r.json()['errcode'] == 0











