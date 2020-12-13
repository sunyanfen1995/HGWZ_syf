#encoding=utf-8

from selenium.webdriver.remote.webdriver import WebDriver

from WebUITest.实战课程.PO_Demo.register_page import RegisterPage


class LoginPage():
    #python的类型注解，使得下面可以联想出driver方法
    #python解释型语言，不需要指定类型
    #java是编译型语言，运行在虚拟机上；c语言也是编译型语言
    def __init__(self, driver:WebDriver):
        #接受上一个页面的driver，进行driver的复用
        self.driver = driver

    def scan(self):
        #扫码
        pass
    def goto_register(self):
        #进入注册页
        self.driver.find_element_by_css_selector('.login_registerBar_link').click()
        return RegisterPage(self.driver)

