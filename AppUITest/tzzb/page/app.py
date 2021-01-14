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
            caps['udid'] = "127.0.0.1:7555"  #当多设备时，指定udid作为唯一标识
            caps["appPackage"] = "com.hexin.zhanghu"
            caps["appActivity"] = "com.hexin.zhanghu.main.WelcomeActivity"
            caps["noReset"] = "true"  #不重置应用
            caps["newCommandTimeout"] = 300 #指定连接超时时间为5分钟
            # caps["dontStopAppOnReset"] = "true" # 不停止应用，直接运行测试用例
            # caps['skipDeviceInitialization'] = 'true'
            # caps['skipServerInstallation'] = 'true'
            # caps["settings[waitForIdleTimeout]"] = 0
            # caps["automationName"]= "UiAutomator1" #默认Ui2
            # caps["autoGrantPermissions"] = "true"
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
            self.driver.implicitly_wait(10)
            print('已经启动app')
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        """重启应用"""
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        """停止应用"""
        self.driver.quit()

    def goto_main(self) -> MainPage:
        # 进入到首页
        return MainPage(self.driver)

