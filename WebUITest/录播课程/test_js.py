#encoding=utf-8
import pytest

import time

from WebUITest.录播课程.base import Base


class TestJS(Base):
    @pytest.mark.skip
    def test_JS_scroll(self):
        """通过js来滑动"""
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element_by_id('kw').send_keys('selenium面试')
        #定位元素并返回结果( 返回js结果需要加上return)
        ele = self.driver.execute_script("return document.getElementById('su')")
        ele.click()
        #执行滑动
        self.driver.execute_script('document.documentElement.scrollTop=100000')#
        time.sleep(2)
        # 获取页面title， 页面性能数据
        # for code in [
        #     'return document.title', 'return JSON.stringify(performance.timing)'
        # ]:
        #     print(self.driver.execute_script(code))
        #也可以在合并执行，但只返回了第一个rerutn值：因为return只
        print(self.driver.execute_script("return document.title; return JSON.stringify(performance.timing)"))

    def test_datatime(self):
        """对事件控件的处理"""
        self.driver.get('https://www.12306.cn/index/')
        #定位时间输入框并移除readonly属性.重新赋值
        self.driver.execute_script('a=document.getElementById("train_date");a.removeAttribute("readonly");a.value="2020-11-22"')
        time.sleep(2)
        #打印当前时间
        print(self.driver.execute_script('return document.getElementById("train_date").value'))






if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_js.py'])