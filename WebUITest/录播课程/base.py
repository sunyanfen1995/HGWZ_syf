#encoding=utf-8
from selenium import webdriver

import os


class Base():
    def setup(self):
        browser = os.getenv("browser")#获取环境变量中browser的值
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'headless': #指无痕，创建一个无界面的浏览器
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def teardown(self):
        #关闭driver，资源的回收
        self.driver.quit()
