#encoding=utf-8
from appium.webdriver.common.mobileby import MobileBy

from AppUITest.tzzb.page.base_page import BasePage


#请选择记账方式页
from AppUITest.tzzb.page.fund.loginfundacc_page import LoginFundAccPage


class AddFundAccPage(BasePage):
    curr_page_title = (MobileBy.ID, 'com.hexin.zhanghu:id/titleTv')
    auto_content = (MobileBy.ID, 'com.hexin.zhanghu:id/aContTv')
    auto_title = (MobileBy.ID, 'com.hexin.zhanghu:id/aTitleTv')
    ajj = (MobileBy.XPATH,'//*[@resource-id="com.hexin.zhanghu:id/addAFundCl" and @index=1]')

    def get_page_title(self):
        """获取页面标题"""
        return self.find(*self.curr_page_title).text

    def get_auto_title(self):
        """获取自动记账标题"""
        return self.find(*self.auto_title).text

    def get_auto_content(self):
        """获取自动记账文案"""
        return self.find(*self.auto_content).text

    def get_autoAcc(self):
        """获取列表中自动账户,并返回"""

        all_auto_fund = self.find(MobileBy.ID,'com.hexin.zhanghu:id/nameTv')
        auto_fund_num = len(all_auto_fund)
        auto_fund_name = []
        for num in range(auto_fund_num):
            auto_fund_name.append(all_auto_fund[num].text)
        return auto_fund_name

    def goto_login_ajj(self):
        """点击跳转爱基绑定页"""
        self.find_and_click(*self.ajj)
        return LoginFundAccPage(self.driver)


