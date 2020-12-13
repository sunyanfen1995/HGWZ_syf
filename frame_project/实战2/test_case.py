#encoding=utf-8
import pytest

from frame_project.实战2.main_page import MainPage


class TestMian:
    def test_mian(self):
        MainPage().goto_marketpage().goto_search().search()

if __name__ == '__main__':
    pytest.main(['test_case.py','-s','-v'])
