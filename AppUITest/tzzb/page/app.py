#encoding=utf-8
from appium import webdriver

from AppUITest.tzzb.page.base_page import BasePage
from AppUITest.tzzb.page.main_page import MainPage


class App(BasePage):

    def start(self):
        """启动应用"""
        if self.driver == None:
            #创建一个driver对象
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = "com.hexin.zhanghu"
            caps["appActivity"] = ".main.WelcomeActivity"
            caps["noReset"] = "True"
            # 不停止应用，直接运行测试用例
            # caps["dontStopAppOnReset"] = "true"
            caps['skipDeviceIcaps["appActivity"] =nitialization'] = 'true'
            caps['skipServerInstallation'] = 'true'
            # caps["settings[waitForIdleTimeout]"] = 0
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub',caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()

    def restart(self):
        """重启应用"""
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        """停止应用"""
        self.driver.quit()

    def goyo_main(self) -> MainPage:
        # 进入到首页
        return MainPage()

