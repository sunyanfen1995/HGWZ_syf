#encoding=utf-8
import pytest
from selenium import webdriver
import time
import shelve

from WebUITest.实战课程.Base import Base

"""课程核心：
复用浏览器：前提是手动关掉chrome浏览器，通过命令让chrome
cookie登录：cookie存本地，会过期；session和token存服务端
shelve：python内置的小型数据库，
"""

class TestHgwarts(Base):
    @pytest.mark.skip
    def test_getCookies(self):
        """获取cookies"""
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#apps')
        cookies = self.driver.get_cookies() #获取到的是list类型
        with shelve.open('cookies') as db:
            db['cookie']=cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie) #添加cookies
        self.driver.refresh() #刷新页面
    @pytest.mark.skip
    def test_saveCookies(self):
        """保存cookies到shelve中"""
        cookies=[] #放之前获取到cookie值，保存后就可以把值删除了
        #对shelve的处理类似文件
        with shelve.open('cookies') as db:
            db['cookie']=cookies

