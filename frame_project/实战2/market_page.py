#encoding=utf-8
from selenium.webdriver.common.by import By

from frame_project.实战2.base_page import BasePage
from frame_project.实战2.search_page import SearchPage


class MarkerPage(BasePage):

    # def goto_search(self):
    #     self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
    #     return SearchPage(self.driver)

    def goto_search(self):
        self.parse_yaml('./main.yaml','goto_search')
        return SearchPage(self.driver)

