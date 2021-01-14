#encoding=utf-8
from appium.webdriver.common.mobileby import MobileBy

from AppUITest.tzzb.page.base_page import BasePage


class ChiCangPage(BasePage):
    _curr_page_title = (MobileBy.ID, '')
    def get_page_title(self):
        return self.find(*self._curr_page_title).text


