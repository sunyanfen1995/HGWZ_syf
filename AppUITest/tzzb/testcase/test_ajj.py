#encoding=utf-8
import pytest

import time
from AppUITest.tzzb.page.app import App
from AppUITest.tzzb.utils import com_utils
from AppUITest.tzzb.page.fund.chicang_page import ChiCangPage


class TestFund:

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()
        self.ajj_data = com_utils.get_data_of_ajj()


    def teardown(self):
        pass

    def test_goto_login_ajj(self):
        """跳转基金tab页并绑定爱基金"""
        fundtabPage = self.main.goto_fundtabpage_by_tab()
        assert '基金' in fundtabPage.get_page_title()
        fundtabPage.goto_addfund().goto_login_ajj().login_ajj_and_detect(acc=self.ajj_data['account'], pwd=self.ajj_data['password'])

    def test_get_chicang_data(self):
        """获取持仓个股数据"""
        time.sleep(2)
        ChiCangPage(self.app.driver).get_chicang_content()



    # def test_yijianfankui(self):
    #     """提交意见反馈成功"""
    #     assert '提交成功' in ChiCangPage.goto_yijianfankui()
    #
    # def test_editprofit_true(self):
    #     """确定修改累计收益"""
    #     assert ChiCangPage.goto_editprofit_true()
    #
    #
    # def test_editfrofit_false(self):
    #     """确定修改累计收益"""
    #     assert ChiCangPage.goto_editprofit_fail()
    #
    #
    # def test_trans_paixu(self):
    #     """遍历排序方式"""
    #     ChiCangPage.goto_paixu()








if __name__ == '__main__':
    pytest.main('test_ajj.py','-vs')
