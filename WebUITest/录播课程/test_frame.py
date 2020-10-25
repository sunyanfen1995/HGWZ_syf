#encoding=utf-8
import pytest
from selenium import webdriver

import time

from WebUITest.录播课程.base import Base


class TestFrame(Base):
    # def setup(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.implicitly_wait(5)
    #     self.driver.maximize_window()
    #
    # def teardown(self):
    #     self.driver.quit()

    def test_frame(self):
        """frame的处理"""
        self.driver.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        #切换至frame
        self.driver.switch_to.frame('iframeResult')
        print(self.driver.find_element_by_id('draggable').text)
        # self.driver.switch_to.parent_frame() #切回父frame
        self.driver.switch_to.default_content() #切回默认frame,两种方法都可以
        self.driver.find_element_by_id('submitBTN').click()







if __name__ == '__main__':
    pytest.main(['-v','-s','test_frame.py'])