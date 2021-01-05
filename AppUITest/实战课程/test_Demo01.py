#encoding=utf-8
"""企业微信打卡"""
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestWeWork():
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "True"
        caps['dontStopAppOnReset']='True'  #不重置app
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps) #建立连接
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(newUiSelector().text("打卡").instance(0));').click()

    # 设置setting
        self.driver.update_settings({"waitForIdleTimeout": 0})
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)

if __name__ == '__main__':
    pytest.main(['test_Demo01.py','-v','-s'])