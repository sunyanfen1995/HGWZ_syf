#encoding=utf-8
from AppUITest.tzzb.page.app import App
from AppUITest.tzzb.page.fund.fundtab_page import FundTabPage
from AppUITest.tzzb.utils import com_utils


class TestFund:

    def setup(self):
        self.app = App()
        # self.main = self.app.start().goto_main()
        self.ajj_data = com_utils.get_data_of_ajj()
        self.fundtabpage = FundTabPage()

    def teardown(self):
        pass

    def test_goto_fundtab(self):
        """切换至基金tab"""
        fundtabPage = self.app.start().goto_main().goto_fundtabpage_by_tab()
        assert '基金' in fundtabPage.get_page_title()

    def test_goto_login_ajj(self):
        """绑定爱基金"""
        self.fundtabpage.goto_addfund().goto_login_ajj().login_ajj_and_detect(acc=self.ajj_data['account'], pwd=self.ajj_data['password'])

