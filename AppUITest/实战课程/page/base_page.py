#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
base_page.py 基类模块：主要用于初始化driver, 定义find, 常用的最基本的方法
"""
import logging
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver



class BasePage:
    root_logger = logging.getLogger()
    print(f"root_logger.handlers:{logging.getLogger().handlers}")
    for h in root_logger.handlers[:]:
        root_logger.removeHandler(h)
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        # logging.info("aaaaa")
        logging.info(by)
        logging.info(locator)
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        logging.info('click')
        self.find(by, locator).click()

    def find_by_scroll(self, text):
        logging.info('find_by_scroll')
        logging.info(text)
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("{text}").instance(0));')
    def swipe_up(self,num):
        """向上滑动n次"""
        x = float(self.driver.get_window_size()['width'])
        y = float(self.driver.get_window_size()['height'])
        for i in range(num):
            self.driver.swipe(x/2,y*4/5,x/2,y/5,200)

    def swipe_down(self,num):
        """向下滑动n次"""
        x = float(self.driver.get_window_size()['width'])
        y = float(self.driver.get_window_size()['height'])
        for i in range(num):
            self.driver.swipe(x/2,y/5,x/2,y*4/5,200)

    def get_toast_text(self):
        logging.info('get_toast_text')

        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        logging.info(result)
        return result
