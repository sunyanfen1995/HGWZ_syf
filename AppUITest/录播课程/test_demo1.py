#encoding=utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import pytest


class TestDemo():
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps['platforVersion'] = '6.0'
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".common.MainActivity"
        caps["noReset"] = "True"
        caps['dontStopAppOnReset'] = 'True'
        caps['skipServerInstallation'] = True
        caps['unicodeKeyBoard'] = 'true'
        caps['resetKeyBoard'] = 'true'
        # caps['dontStopAppOnReset'] = 'True'  # 不重置app
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)  # 建立连接
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
    @pytest.mark.skip
    def test_getattribute(self):
        """雪球搜索：获取坐标位置 ，判断是否可找到等"""
        elem = self.driver.find_element(By.ID,'com.xueqiu.android:id/tv_search')
        print('当前元素的文本属性是：',elem.text)
        print('当前元素的位置：',elem.location)
        print('当前元素的大小：',elem.size)
        search_enable = elem.is_enabled() #是否可用
        if search_enable == True:
            elem.click()
            self.driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys('alibaba')
            alibaba_elem = self.driver.find_element_by_xpath('//*[@id="com.xueqiu.android:id/name" and @text="阿里巴巴"]')
            alibaba_atr=alibaba_elem.get_attribute('displayed')
            if alibaba_atr == 'true':
                print('搜索成功')
            else:
                print('搜索失败')

    @pytest.mark.skip
    def test_touchaction_move(self):
        action = TouchAction(self.driver)
        window_rect= self.driver.get_window_rect() #获取屏幕像素
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_end).release().perform()  #从一个点到另一个点，释放点，并执行操作

    @pytest.mark.skip
    def test_touchcation_unlock(self):
        """手势解锁"""
        action = TouchAction(self.driver)
        action.press(x=243,y=395).move_to(x=711,y=395).move_to(x=1198,y=395).move_to(x=1198,y=865).move_to(x=1198,y=1323).release().perform()

    @pytest.mark.skip
    def test_get_current_price(self):
        """xpath的层级定位"""
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys('alibaba')
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()
        #从搜索列表上获取第二个阿里巴巴港股现价: 先定位到09988港股，再通过三个..定位到父节点，最后定位父节点下的价格元素
        current_text = self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(f'当前价格是：{current_text}')
        assert float(current_text)>200

    @pytest.mark.skip
    def test_uiautomator(self):
        """点击我的-->点击登录-->输入账号密码-->点击登录"""
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("帐号密码登录")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys('admin')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys('123456')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

    @pytest.mark.skip()
    def test_uiautomator_scroll(self):
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().textContains("科技边脚里奥").'
                                                        'instance(0));').click()

        print('ok')







if __name__ == '__main__':
    pytest.main(['test_demo1','-s', '-v'])








