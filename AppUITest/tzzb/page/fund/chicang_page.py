#encoding=utf-8
from appium.webdriver.common.mobileby import MobileBy

from AppUITest.tzzb.page.base_page import BasePage
import shelve

from AppUITest.tzzb.page.fund.huoJi_page import HuoJixiangqingPage
from AppUITest.tzzb.utils import com_utils


class ChiCangPage(BasePage):
    _curr_page_title = (MobileBy.ID, 'com.hexin.zhanghu:id/my_new_fund_navi_title') #爱基金
    _huoji_btn = (MobileBy.ID, 'com.hexin.zhanghu:id/moneyFundAssetsImg')
    _sandian_btn = (MobileBy.ID, 'com.hexin.zhanghu:id/my_new_fund_navi_right_img')
    _yijianfankui_btn = (MobileBy.ID, 'com.hexin.zhanghu:id/feedbackTv')
    _profitedit_input = (MobileBy.ID, 'com.hexin.zhanghu:id/allProfitEdt')
    _queding_btn = (MobileBy.ID, 'com.hexin.zhanghu:id/okBt')
    _quxiao_btn =(MobileBy.ID, 'com.hexin.zhanghu:id/cancelBt')
    _chiyoushouyi_btn = (MobileBy.ID, 'com.hexin.zhanghu:id/titleHoldProfitTv')
    _zuixinrishouyi_btn = (MobileBy.ID, 'com.hexin.zhanghu:id/titleDayProfitTv')
    _zichan_btn = (MobileBy.ID, 'com.hexin.zhanghu:id/titleAssetsTv')

    def get_page_title(self):
        return self.find(*self._curr_page_title).text

    def get_chicang_data(self):
        """获取持仓头部数据并并存储到db中"""
        zrsy = self.find(MobileBy.ID, 'com.hexin.zhanghu:id/frag_my_new_fund_top_yesterday_profit_value').text
        zrsyl = self.find(MobileBy.ID, 'com.hexin.zhanghu:id/frag_my_new_fund_top_yesterday_profit_percent').text
        ssygsy = self.find(MobileBy.ID, 'com.hexin.zhanghu:id/real_time_profit_tv').text
        ssygsyl = self.find(MobileBy.ID, 'com.hexin.zhanghu:id/real_time_profit_percent_tv').text
        zhzzc = self.find(MobileBy.ID, 'com.hexin.zhanghu:id/zzc_value').text
        zccb = self.find(MobileBy.ID, 'com.hexin.zhanghu:id/chicangCBvalue').text
        hjzc = self.find(MobileBy.ID, 'com.hexin.zhanghu:id/moneyFundAssetsValTv').text
        ljsy = self.find(MobileBy.ID, 'com.hexin.zhanghu:id/totalProfitValTv').text

        db_path = com_utils.get_os_path('data')+'\\fund_data'
        # path = 'D:/python_learn/HGWZ_ceshikaifa/AppUITest/tzzb/data/fund_data'   #写死路径
        with shelve.open(db_path) as db:
            db['ajj_zrsy'] = zrsy
            db['ajj_zrsyl'] = zrsyl
            db['ajj_ssygsy'] = ssygsy
            db['ajj_ssygsyl'] = ssygsyl
            db['ajj_zhzzc'] = zhzzc
            db['ajj_zccb'] = zccb
            db['ajj_hjzc'] = hjzc
            db['ajj_ljsy'] = ljsy

    def close_yindao(self):
        """如果存在知道了引导，则关闭"""
        yindao_btn = (MobileBy.XPATH, '//*[@text=["知道了]]')
        if self.find(*yindao_btn):
            self.find_and_click(*yindao_btn)

    def goto_huojigpage(self):
        """点击跳转，货基详情页"""
        self.find_and_click(*self._huoji_btn)
        return HuoJixiangqingPage(self.driver)


    def goto_yijianfankui(self):
        """进行意见反馈,成功后返回持仓页"""
        self.find_and_click(*self._sandian_btn)
        self.find_and_click(*self._yijianfankui_btn)
        if self.find(MobileBy.ID, 'com.hexin.zhanghu:id/navi_title').text is '意见反馈':
            print('输入意见反馈内容')
            self.find_and_click(MobileBy.ACCESSIBILITY_ID, '数据问题')
            self.find_and_sendkeys(MobileBy.XPATH, '//*[contains(@text, "文字描述")]', '输入意见反馈内容')
            self.find_and_sendkeys(MobileBy.XPATH, '//*[@resource-id="phone_num"]', 'test_wx')
            self.find_and_click(MobileBy.ACCESSIBILITY_ID, '提交')
            return self.get_toast_text()

    def goto_editprofit_true(self):
        """修改累计收益"""
        ljsy = self.find(MobileBy.ID, 'com.hexin.zhanghu:id/totalProfitValTv').text
        self.find_and_click(*self._sandian_btn)
        self.find(*self._profitedit_input).send_keys('2021')
        self.find_and_click(*self._queding_btn)
        new_ljsy = self.find(MobileBy.ID, 'com.hexin.zhanghu:id/totalProfitValTv').text
        assert new_ljsy != ljsy


    def goto_editprofit_fail(self):
        """修改累计收益：取消"""
        ljsy = self.find(MobileBy.ID, 'com.hexin.zhanghu:id/totalProfitValTv').text
        self.find_and_click(*self._sandian_btn)
        self.find(*self._profitedit_input).send_keys('2021')
        self.find_and_click(*self._quxiao_btn)
        new_ljsy = self.find(MobileBy.ID, 'com.hexin.zhanghu:id/totalProfitValTv').text
        assert new_ljsy == ljsy


    def chichang_is_null(self):
        """获取持仓是否为空"""
        elems = self.find(MobileBy.XPATH,'//*[@resource-id="com.hexin.zhanghu:id/content"]')
        if len(elems) != 0:
            print('持仓非空')
            return True
        else:
            print("持仓为空")
            return False

    def get_chicang_content(self):
        """获取持仓信息"""
        elems = self.find(MobileBy.XPATH, '//*[@resource-id="com.hexin.zhanghu:id/content"]')
        if len(elems) != 0:
            """ 滑动一次，确保持仓数据全部渲染出来"""
            self.swipe_up(1)
            for elem in elems:
                self.find(elem)
                fund_name = self.find(MobileBy.XPATH,'//*[@resource-id= "com.hexin.zhanghu:id/fund_name"]').text
                print(fund_name)




    def goto_paixu(self):
        """遍历排序"""
        for i in [self._zichan_btn, self._chiyoushouyi_btn, self._zuixinrishouyi_btn]:
            self.find_and_click(*i)
            if self.find(MobileBy.XPATH,'//*[@text="取消"]'):
                self.find_by_scroll('收益率升序')
                self.find(MobileBy.XPATH, '//*[@text="确定"]')





















