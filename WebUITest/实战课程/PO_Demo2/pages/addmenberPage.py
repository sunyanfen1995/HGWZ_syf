#encoding=utf-8

#添加成员页面
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

import time

from WebUITest.实战课程.PO_Demo2.pages.basePage import BasePage

#直接继承基类，driver不需要再传递过来了
class AddMemberPage(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self.driver = driver

    def add_member(self,username, account,phone_num):
        """添加成员"""
        self.find(By.ID,'username').send_keys(username)
        self.find(By.ID,'memberAdd_acctid').send_keys(account)
        self.find(By.ID,'memberAdd_phone').send_keys(phone_num)
        self.find(By.CSS_SELECTOR,'.js_btn_save').click()

        return True

    def get_member(self,value):
        """获取联系人"""
        #考虑下几种场景：首页获取、中间页获取、最后一页获取
        #获取姓名字段的元素list，find_elements如果为空，则返回[]
        total_list=[]
        # for ele in elem_list:
        #     title_list.append(ele.get_attribute('title'))
        # 进阶：如果有页则通过翻页获取数据
        while True:
            elem_list = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            time.sleep(2)
            # title_list = [ele.get_attribute('title') for ele in elem_list]  # 列表推导式
            # total_list = title_list + total_list
            for ele in elem_list:
                total_list.append(ele.get_attribute('title'))
                webdriver.Chrome().refresh()
                time.sleep(2)


            # 判断预期是否在列表中
            if value in total_list:
                return True

            # 获取翻页数据：切分分子和分母
            result: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
            print(result)
            num, total = result.split('/', 1)  # 指定根据/分割1次,得到的是字符串
            if int(num) == int(total):
                return False
            #点击翻页按钮
            self.find(By,'js_next_page').click()

        return title_list




