#encoding=utf-8
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver=None):
        self.driver = driver

    def find(self, by, locator):
        """
        find方法封装
        :param by:  定位方式
        :param locator:  定位内容
        :return:
        """
        return self.driver.find_element(by, locator)

    def find_and_click(self,by, locator):
        """找到元素并点击"""
        return self.find(by, locator).click()

    def find_by_scroll(self, text):
        """滚动查找到指定文本元素"""
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("{text}").instance(0));')


