#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from AppUITest.实战课程.page.app import App


class TestContact:

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()
    @pytest.mark.skip()
    def test_addcontact(self):
        name = "hogwarts__004"
        gender = "男"
        phonenum = "13500000003"

        result = self.main.goto_address() \
            .click_addmember(). \
            add_member_menual(). \
            add_contact(name, gender, phonenum).get_toast()
        assert '添加成功' == result

    def test_delcontact(self):
        """删除联系人"""
        manage_page = self.main.goto_address().click_editbtn() #进入管理页
        #获取未删除前的人数
        before_num = manage_page.get_list_number()
        print(before_num)
        del_result= manage_page.click_second_member().click_deletbtn()
        assert '删除成员' in del_result
        after_num = manage_page.get_list_number()
        print(after_num)
        assert before_num is not after_num




if __name__ == '__main__':
    pytest.main(['test_contact.py','-s','-v'])