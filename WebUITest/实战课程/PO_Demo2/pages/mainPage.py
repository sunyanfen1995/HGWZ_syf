#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

from WebUITest.实战课程.PO_Demo2.pages.addmenberPage import AddMemberPage
from WebUITest.实战课程.PO_Demo2.pages.basePage import BasePage

#直接继承基类
class MainPage(BasePage):
    base_url='https://work.weixin.qq.com/wework_admin/frame#index'
    # def __init__(self):
    #     #初始化
    #     options = Options()
    #     options.debugger_address = '127.0.0.1:9222'
    #     self.driver = webdriver.Chrome(options=options)
    #     self.driver.implicitly_wait(3)
    #     self.driver.maximize_window()
    #     #复用浏览器后要注意当前启动浏览器的页面
    #     self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

    def goto_addmenber(self):
        """跳转添加成员"""
        #在首页点击添加
        # self.driver.find_element_by_css_selector('.index_service_cnt_itemWrap>nth-child(1)').click()
        #在首页-联系人入口添加
        self.find( By.CSS_SELECTOR,"#menu_contacts").click()
        sleep(2)
        #注意：此处a标签的索引值是2，因为是从父节点div下所有的子节点开始计算的，包括a前面还有其他节点

        #self.find(By.CSS_SELECTOR,'.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        #进行显示等待
        loctor = (By.CSS_SELECTOR,'.js_has_member>div:nth-child(1)>a:nth-child(2)')

        # elem:WebDriver = WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(loctor))
        #elem = self.wait_to_click(loctor)
        #elem.click()
        #处理点击添加按钮不跳转的问题（企业微信的bug）
        def wait_for_next(x:WebDriver):
            try:
                x.find_element(*loctor).click()
                return x.find_element(By.ID,'username')
            except:
                return False
        #反复点击这个按钮直到跳转页面
        WebDriverWait(self.driver,10).until(wait_for_next)#注意：传的在这个wait_for_next不用加（）

        return AddMemberPage(self.driver)
