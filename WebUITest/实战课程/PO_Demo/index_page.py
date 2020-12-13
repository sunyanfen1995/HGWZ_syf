#encoding=utf-8
from selenium import webdriver
from WebUITest.实战课程.PO_Demo.login_page import LoginPage
from WebUITest.实战课程.PO_Demo.register_page import RegisterPage

class IndexPage():
    def __init__(self):
        # 初始化driver
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/')

    def goto_login(self):
        #点击并跳转登录页
        self.driver.find_element_by_css_selector('.index_top_operation_loginBtn').click()
        return LoginPage(self.driver) #将driver传递给下一个页面

    def goto_register(self):
        # 点击并跳转注册页页
        self.driver.find_element_by_css_selector('.index_head_info_pCDownloadBtn').click()
        return RegisterPage(self.driver)

