#encoding=utf-8
from selenium import webdriver


class TestWindows():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_handles(self):
        """多页面的处理"""
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle)  #打印当前句柄
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        #获取当前全部handles，得到的是一个list
        handles = self.driver.window_handles
        #切换至最后一个handle
        self.driver.switch_to_window(handles[-1])
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('username')
        time.sleep(3)
        #切换回原来的handle
        self.driver.switch_to_window(handles[0])
        self.driver.switch_to.window(handles[0])
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        time.sleep(3)
