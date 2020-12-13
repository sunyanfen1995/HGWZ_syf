#encoding=utf-8
from selenium.webdriver.common.by import By

from frame_project.实战2.base_page import BasePage


class SearchPage(BasePage):

    # def search(self):
    #     self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("alibaba")
    def search(self):
        self.parse_yaml('./main.yaml','search')


