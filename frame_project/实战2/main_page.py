#encoding=utf-8
import yaml
from selenium.webdriver.common.by import By

from frame_project.实战2.base_page import BasePage
from frame_project.实战2.market_page import MarkerPage


class MainPage(BasePage):
    # def goto_marketpage(self):
    #     self.find((By.XPATH, '//*[@resource-id="com.xueqiu.android:id/post_status"]')).click()  # 制造弹窗
    #     self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
    #     return MarkerPage(self.driver)

    def goto_marketpage(self):
        self.parse_yaml('./main.yaml',"goto_market")
        return MarkerPage(self.driver)



