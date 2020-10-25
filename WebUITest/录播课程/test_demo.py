#encoding=utf-8
from selenium import webdriver
import time
class TestHgwarts():
    def setup(self):
        #如果driver没有配置到环境变量，则需要指定executable_path
        # self.driver = webdriver.Chrome(executable_path='')
        #实力化driver
        self.driver = webdriver.Chrome()
        #浏览器最大化
        self.driver.maximize_window()
        #全局动态的隐式等待
        self.driver.implicitly_wait(5) #只能判断是否有出现元素
        time.sleep(5)


    def teardown(self):
        #关闭driver，资源的回收
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text('社团').click()
        self.driver.find_element_by_link_text('求职面试圈').click()
