#encoding=utf-8
from appium.webdriver import webdriver


class TestBrowser():
    def setup(self):
        des_caps = {
            'platformName':'android',
            'platformVersion':'6.0',
            'browserName':'Brrowser',
            'devicesName':'127.0.0.1:7555 ',
            'chromedriverExecutable':''  #指定chromedriver的地址
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des_caps)  # 建立连接
        self.driver.implicitly_wait(5)

