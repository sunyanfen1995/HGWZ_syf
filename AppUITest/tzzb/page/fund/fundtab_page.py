#encoding=utf-8
from appium.webdriver.common.mobileby import MobileBy

from AppUITest.tzzb.page.base_page import BasePage

#基金tab页
class FundtabPage(BasePage):

    add_btn = (MobileBy.ID, 'com.hexin.zhanghu:id/addAccTv')

    def goto_addfund(self):
        """
        点击原生按钮跳转去添加
        :return:
        """
        self.find_and_click(self.add_btn)
        return

