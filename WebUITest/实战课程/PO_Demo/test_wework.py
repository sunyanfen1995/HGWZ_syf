#encoding=utf-8
from WebUITest.实战课程.PO_Demo.index_page import IndexPage


class TestWX():

    def setup(self):
        self.index = IndexPage()
    def test_register(self):
        assert self.index.goto_register()



