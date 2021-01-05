#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
编辑联系人页面
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

# from app.page.member_invite_menu_page import MemberInviteMenuPage
from AppUITest.实战课程.page.addresslist_page import AddressListPage
from AppUITest.实战课程.page.base_page import BasePage


class ContactAddPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def add_contact(self, name, gender, phonenum):
        # 设置 【用户名】【性别】【手机号】
        self.find(MobileBy.XPATH,
                  "//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(name)
        self.find(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']").click()

        if gender == "男":
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
            self.find(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.find(MobileBy.XPATH, "//*[@text='女']").click()

        self.find(MobileBy.XPATH,
                  '//*[contains(@text, "手机") and contains(@class, "TextView")]/..//android.widget.EditText').send_keys(
            phonenum)
        # 点击【保存】
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()

        from AppUITest.实战课程.page.member_invite_menu_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)

    def click_deletbtn(self):
        """点击删除按钮,确定
        ：:return 跳转通讯录列表页
        """
        self.find_and_click(MobileBy.ID,'com.tencent.wework:id/eh7')
        title = self.find(MobileBy.ID,'com.tencent.wework:id/bjr').text
        self.find_and_click(MobileBy.XPATH, '//*[@text="确定" ]')
        from AppUITest.实战课程.page.enter_prisecontact_page import EnterpriseContactPage
        return title

