#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#基类：最基本的方法，进行diver实例化、find等操作
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    base_url = ""
    def __init__(self, driver: WebDriver = None):
        #判断driver是否已经实例化
        if driver == None:
            # 首次调用BasePage时为none，则需要创建；
            options = Options()
            options.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=options)
        else:
            #页面传递的时则直接复用driver，不需
            self.driver = driver
        self.driver.implicitly_wait(3)
        # 如果调用基类的类中指定了base_url,则直接传进来，
        if self.base_url !='':
            self.driver.get(self.base_url)

    def find(self,by, locator):
        """封装find方法"""
        return self.driver.find_element(by, locator)

    def finds(self,by, locator):
        return self.driver.find_elements(by, locator)

    def wait_to_click(self,loctor):
        """等到直到元素出现可点击"""
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(loctor))

