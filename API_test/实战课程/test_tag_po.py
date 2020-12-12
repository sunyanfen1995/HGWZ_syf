#encoding=utf-8
""""企业微信客户标签管理"""

import jsonpath
from API_test.实战课程.tag import Tag
import pytest

#todo:底层具体的实现框架代码耦合严重，无法适用变化，比如公司切换了协议，如pb、dubbo
#todo:代码冗余，需要封装
#todo：无法清晰的描述业务
#todo：使用jasonpath表达更灵活的递归过滤


class TestTag():
    def setup(self):
        #实例化一次Tag类即可，后面用例中直接调用
        self.tag = Tag()
        self.group_name = 'python_15'
        self.group_id = []  #et_N2IEQAAaY8EqZVkcCLi5XbgXvpWbA

    def teardown(self):
        """数据清理,删除指定的组"""
        # group_id= jsonpath.jsonpath(self.tag.list().json(), '$..group_id')[0]
        assert self.tag.delect(self.group_id).status_code ==200

    @pytest.mark.parametrize('tag_id,tag_name',(
                             ['et_N2IEQAAcCOHbiU0fku2VJis3Xfdgw', 'tag1_new'],
                             ['et_N2IEQAAcCOHbiU0fku2VJis3Xfdgw', 'tag1_中文'],
                             ['et_N2IEQAAcCOHbiU0fku2VJis3Xfdgw', 'tag1_@@@@']
    )
    )
    def test_tag_list(self, tag_id, tag_name):
        group_name = 'python'
        tag_name= tag_name + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        r = self.tag.list()
        r = self.tag.updata(id =tag_id, tag_name= tag_name)
        r = self.tag.list()
        tags =[
            tag
            for group in r.json()['tag_group'] if group['group_name']==group_name
            for tag in group['tag'] if tag['name'] == tag_name
        ]
        # assert tags != []
        assert jsonpath.jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]") is not None
        assert jsonpath.jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name


    # def test_tag_list_fail(self):
    #     pass

    #作业：
    # 新增标签
    # 删除标签
    # 数据清理


    @pytest.mark.parametrize('tag_name',['tag_add_abc4','tag_add_中文4','tag_add_@@@4'],ids=['添加字母','添加中文','添加字符'])
    def test_tag_add(self,tag_name):
        """创建全新的组和标签"""
        r = self.tag.add(self.group_name, tag_name)
        print(r.json())
        print('=========')
        assert r.status_code == 200
        assert tag_name in jsonpath.jsonpath(r.json(), '$..name')

        # 保存group_id，然后在teardwon里删除
        group_id = jsonpath.jsonpath(r.json(), f"$..[?(@.group_name=='{self.group_name}')]")[0]['group_id']
        self.group_id.append(group_id)
        print(self.group_id)


    def test_tag_delect(self):
        """删除指定tag_id"""
        print(self.tag.list().json())
        tag_id = jsonpath.jsonpath(self.tag.list().json(), '$..id')[0]
        # tag_id='et_N2IEQAA59aBAEJdui6_DGm0RU5k5A'
        r = self.tag.delect(tag_id)
        assert r.status_code == 200
        assert tag_id not in jsonpath.jsonpath(self.tag.list().json(), '$..id')











