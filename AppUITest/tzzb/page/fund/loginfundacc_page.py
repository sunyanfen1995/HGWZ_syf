#encoding=utf-8
from appium.webdriver.common.mobileby import MobileBy

import time

from AppUITest.tzzb.page.base_page import BasePage

#基金绑定页
from AppUITest.tzzb.page.fund.chicang_page import ChiCangPage
from AppUITest.tzzb.utils import com_utils

ajj_acc = com_utils.get_data_of_ajj()['account']
ajj_pwd = com_utils.get_data_of_ajj()['password']

class LoginFundAccPage(BasePage):
    curr_page_title = (MobileBy.ID, 'com.hexin.zhanghu:id/navi_title')
    curr_fund_name = (MobileBy.ID, 'com.hexin.zhanghu:id/login_qs_qsname_tv')



    def get_page_title(self):
        return self.find(*self.curr_page_title).text

    def get_fund_name(self):
        """获取并返回当前基金名称"""
        return self.find(*self.curr_fund_name).text

    def login_ajj(self, acc, pwd):
        """绑定爱基金"""
        self.find_and_sendkeys(MobileBy.ID,'com.hexin.zhanghu:id/login_qs_account_edit',ajj_acc)
        self.find_and_sendkeys(MobileBy.ID, 'com.hexin.zhanghu:id/login_qs_account_pwd_edit', ajj_pwd)
        self.find_and_click(MobileBy.ID, 'com.hexin.zhanghu:id/login_qs_submit_bt')

    def login_ajj_success(self):
        """绑定成功，跳转持仓页"""
        return ChiCangPage

    def login_ajj_fail(self):
        """绑定失败：获取弹窗内容并关闭弹窗"""
        # 获取文本内容，关闭弹窗并重新执行登录
        md_content = self.find(MobileBy.ID, 'com.hexin.zhanghu:id/md_content').text
        print(f'当前提示信息是：{md_content}')
        assert '绑定失败' in md_content
        self.find_and_click(MobileBy.ID, 'com.hexin.zhanghu:id/md_buttonDefaultPositive')


    def login_ajj_and_detect(self,acc, pwd):
        """绑定爱基金新并异常处理"""
        self.login_ajj(acc, pwd)
        time.sleep(5)
        # 如果不存在报错提示框，跳转持仓
        if not self.find(MobileBy.ID, 'com.hexin.zhanghu:id/md_title'):
            return self.login_ajj_success()
        # 如果存在报错，处理掉弹窗重新登录
        else:
            self.login_ajj_fail()
            return self.login_ajj_and_detect(acc, pwd)










