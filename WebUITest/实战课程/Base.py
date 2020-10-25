#encoding=utf-8
from selenium import webdriver


class Base():
    def setup_method(self, method):
        #方法级（setup_method/teardown_method）:开始于方法始末（在类中。每个方法执行一次）
        #复用浏览器：设置option的debug地址，并传入driver中
        options = webdriver.ChromeOptions()
        options.debugger_address = '127.0.0.1:9222' #换成'localhost:9222' 也可以
        self.driver = webdriver.Chrome() #复用的话加入：options=options
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self,method):
        self.driver.quit()

