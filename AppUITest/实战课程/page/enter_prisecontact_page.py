#encoding=utf-8
"""管理通讯录页面"""
import time

from AppUITest.实战课程.page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy




class EnterpriseContactPage(BasePage):

    def click_second_member(self):
        """点击第二个成员
        :return 编辑页面
        """
        self.find_and_click(MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/b9n"]/android.widget.RelativeLayout[2]')
        from AppUITest.实战课程.page.contactadd_page import ContactAddPage
        return ContactAddPage(self.driver)

    def get_list_number(self):
        """获取列表数量"""
        time.sleep(2)
        self.swipe_up(3)
        # bottom_text = self.find(MobileBy.XPATH, "//*[@class='android.widget.TextView' and @textConstains='为家兔']").text
        bottom_text:str = self.find(MobileBy.XPATH, '//android.widget.TextView[contains(@text, "未加入")]').text
        result = bottom_text.split('，', 1)[0]  #获取总人数
        self.swipe_down(3)
        return  result






