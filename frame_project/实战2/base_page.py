#encoding=utf-8
import yaml
from appium import webdriver

# @singleton#装饰器
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.mobile import Mobile

from frame_project.实战2.handle_black import handle_black


class BasePage:
    #类变量，加下划线表示是保护类型，那么外部就不能直接引用了
    _black_list=[(MobileBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/iv_close"]')] #关闭弹窗
    _max_num=3
    _error_num=0

    black_list = [(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/iv_close"]')]  # 关闭弹窗
    max_num = 3
    error_num = 0

    def __init__(self, driver=None):
        """初始化应用"""
        if driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".common.MainActivity"
            caps["noReset"] = "True"
            caps['skipDeviceInitialization'] = 'true'
            caps['skipServerInstallation'] = 'true'
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        else:
            self.driver = driver
        self.driver.implicitly_wait(5)

    # # 方法2：使用装饰器的方式处理黑名单
    @handle_black
    def find(self,by,locator=None):
        """查找元素
        """
        # 如果只有一个元素，则进行解元组，如self.find(（By.xxx，“xxxx”）)
        if locator is None:
            result = self.driver.find_element(*by)
        else:
            # 传进来by和locator  self.find(By.xxx，“xxxx”）
            result = self.driver.find_element(by, locator)
        return result



    # #方法1：通过修改原代码实现代码增强，处理黑名单
    # def find(self, by , locator=None):
    #     """查找元素
    #     """
    #     try:
    #         # 如果只有一个元素，则进行解元组，如self.find(（By.xxx，“xxxx”）)
    #         if locator is None:
    #             result = self.driver.find_element(*by)
    #         else:
    #             # 传进来by和locator  self.find(By.xxx，“xxxx”）
    #             result = self.driver.find_element(by, locator)
    #         self._error_num=0
    #         return result
    #     #捕获异常
    #     except Exception as e:
    #         #设置计数器，判断是否超过最大错误次数
    #         if self._error_num> self._max_num:
    #             raise e
    #         self._error_num+=1
    #         # 从黑名单中进行遍历元素
    #         for black_ele in self._black_list:
    #             ele = self.driver.find_elements(*black_ele)
    #             if len(ele)>0:
    #                 ele.click()
    #                 return self.find(by,locator)
    #         raise e #不存在黑名单元素就最直接抛出异常

    def parse_yaml(self,path, func_name):
        """步骤驱动
        :path yaml文件
        :func_name 功能模块名称
        """
        with open(path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        self.parse(data[func_name])

    def parse(self,steps):
        """
        解析yaml内容
        :param steps:
        :return:
        """
        # 遍历每一个步骤
        for step in steps:
            # 如果是点击
            if 'click' == step['action']:
                self.find(step['by'], step['locator']).click()
            # 如果是发送内容
            elif 'send' == step['action']:
                self.find(step['by'], step['locator']).send_keys(step["content"])
