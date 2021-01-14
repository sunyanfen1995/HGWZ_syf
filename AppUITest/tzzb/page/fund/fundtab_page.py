#encoding=utf-8
from appium.webdriver.common.mobileby import MobileBy

from AppUITest.tzzb.page.base_page import BasePage

#基金tab页
from AppUITest.tzzb.page.fund.addfundacc_page import AddFundAccPage


class FundTabPage(BasePage):

    add_btn = (MobileBy.XPATH, '//*[@text="添加账户"]')
    curr_page_title = (MobileBy.ID, 'com.hexin.zhanghu:id/titleTv')
    curr_fund_name = (MobileBy.ID, 'com.hexin.zhanghu:id/login_qs_qsname_tv')



    def get_page_title(self):
        return self.find(*self.curr_page_title).text


    def goto_addfund(self):
        self.find_and_click(*self.add_btn)
        return AddFundAccPage(self.driver)



