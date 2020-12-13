#encoding=utf-8
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage():

    def __init__(self, driver:WebDriver):
        self.driver = driver

    #注册方法
    def register(self):
        self.driver.find_element_by_id('corp_name').send_keys()
        self.driver.find_element_by_id('manager_name').send_keys()
        self.driver.find_element_by_id('register_tel').send_keys()
        self.driver.find_element_by_id('submit_btn').click()
        return True

