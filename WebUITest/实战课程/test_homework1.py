#encoding=utf-8
import pytest
import shelve
import time

from WebUITest.实战课程.Base import Base

class TestWework(Base):
    """作业：使用cookies登录企业微信，完成联系人导入，并断言
    只是简单写了下两个用例
    """

    def test_addPerson_Fail(self):
        """导入失败"""
        db = shelve.open('cookies')
        cookies = db['cookie']
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')  # 打开首页
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh() #重新刷新页面后便是登录状态
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@class="index_service_cnt js_service_list"]/a[2]').click()
        self.driver.find_element_by_xpath(
            '//*[@class="qui_btn ww_btn ww_fileImporter_fileContainer_upload"]/input').send_keys(
            'D:/python_learn/HGWZ_15/WebUITest/Data/mydata.xlsx')
        text = self.driver.find_element_by_xpath('//*[@class="ww_fileImporter_fileContainer_fileNames"]').text
        assert 'mydata' in text
        time.sleep(3)
        # 点击导入按钮
        self.driver.find_element_by_xpath('//*[@class="ww_fileImporter_body"]/div[3]/a').click()
        # 导入错误
        error_text = self.driver.find_element_by_xpath('//*[@class="ww_fileImporter"]/div[2]/div/div[2]').text
        if '批量导入模板错误' in error_text:
            # 点击重新导入按钮
            self.driver.find_element_by_xpath('//*[@class="ww_fileImporter_errorContainer"]/a').click()
    @pytest.mark.skip
    def test_addPerson_Success(self):
        """导入成功"""
        db = shelve.open('cookies')
        cookies = db['cookie']
        print(cookies)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')  # 打开首页
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@class="index_service_cnt js_service_list"]/a[2]').click()
        self.driver.find_element_by_xpath(
            '//*[@class="qui_btn ww_btn ww_fileImporter_fileContainer_upload"]/input').send_keys(
            'D:/python_learn/HGWZ_15/WebUITest/Data/data.xlsx')
        text = self.driver.find_element_by_xpath('//*[@class="ww_fileImporter_fileContainer_fileNames"]').text
        assert 'data' in text
        time.sleep(3)
        # 点击导入按钮
        self.driver.find_element_by_xpath('//*[@class="ww_fileImporter_body"]/div[3]/a').click()
        # 导入成功
        success_text = self.driver.find_element_by_xpath('//*[@class="ww_fileImporter_body"]/div[1]').text
        if '导入成功' in success_text:
            # 点击重新导入按钮
            self.driver.find_element_by_xpath('//*[@class="ww_fileImporter_successBtnWrap"]/a').click()


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_homework1.py'])
