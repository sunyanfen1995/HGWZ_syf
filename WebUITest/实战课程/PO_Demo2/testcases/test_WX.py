#encoding=utf-8
import pytest

from WebUITest.实战课程.PO_Demo2.pages.mainPage import MainPage


class TestWX():
    def setup(self):
        self.mainPage = MainPage()

    def test_01(self):
        username = 'testsyf95'
        account = 'testsyf95'
        phone_num = '17306400395'
        addmemberPage = self.mainPage.goto_addmenber()
        assert addmemberPage.add_member(username, account,phone_num)
        assert username in addmemberPage.get_member(username)


if __name__ == '__main__':
    pytest.main(['-v','-s','test_WX.py'])