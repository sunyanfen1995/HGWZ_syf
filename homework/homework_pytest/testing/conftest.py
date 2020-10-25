#encoding=utf-8
import pytest
import yaml


# 测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
#即解决使用ids时中文乱码问题；
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(scope='function', autouse=True)
def login():
    print('登录计算机')
    print('开始计算')
    yield 
    print('计算结束')



