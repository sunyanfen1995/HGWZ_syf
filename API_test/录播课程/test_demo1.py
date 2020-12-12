#encoding=utf-8

import pytest
import requests
from jsonpath import jsonpath
from hamcrest import *


class TestDemo():
    # def test_get(self):
    #     payload = {
    #         "level": 1,
    #         "name": 'syf'
    #     }
    #     r = requests.post('https://httpbin.testing-studio.com/get', params=payload)
    #     print(r.text)


    # def test_post(self):
    #     payload={
    #         "level": 1,
    #         "name": 'syf'
    #     }
    #     r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
    #     print(r.text)

    # def test_updata_file(self):
    #     """文件上传"""
    #     files = {'file': open('demo.json','rb')}
    #     r = requests.post('https://httpbin.testing-studio.com/get', file= files)
    #     print(r.text)


    # def test_assert_json(self):
    #     """断言json"""
    #     url = "https://ceshiren.com/categories.json"
    #     r = requests.get(url)
    #     print(jsonpath(r.json(),'$..name'))
    #     assert jsonpath(r.json(),'$..name')[0] == '开源项目'


    def test_hamcrest(self):
        assert_that(2,equal_to(3))








if __name__ == '__main__':
    pytest.main('-v', '-s', 'test_demo1.py')
