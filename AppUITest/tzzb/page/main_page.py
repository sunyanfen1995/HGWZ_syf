#encoding=utf-8
from appium.webdriver.common.mobileby import MobileBy

from AppUITest.tzzb.page.base_page import BasePage
from AppUITest.tzzb.page.fund.fundtab_page import FundTabPage


class MainPage(BasePage):


    fund_tab = (MobileBy.XPATH, "//*[@resource-id='com.hexin.zhanghu:id/tv_table_label' and @text='基金']" )

    def goto_fundtabpage_by_tab(self):
        """
        通过点击基金tab进入基金tab页
        :return:
        """
        self.find_and_click(*self.fund_tab)
        # print('当前在首页')
        # self.driver.find_element_by_xpath("//*[@resource-id='com.hexin.zhanghu:id/tv_table_label' and @text='基金']").click()
        return FundTabPage(self.driver)
