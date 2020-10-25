#encoding=utf-8
import pytest
import time
from selenium.webdriver import ActionChains

from WebUITest.录播课程.base import Base


class TestAlert(Base):
    def test_alert(self):
        """对alert的处理"""
        self.driver.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        # 切换至frame
        self.driver.switch_to.frame('iframeResult')
        action = ActionChains(self.driver)
        drag_elem = self.driver.find_element_by_id("dragger")
        drop_elem = self.driver.find_element_by_id("droppable")
        #执行拖拽效果
        action.drag_and_drop(drag_elem,drop_elem).perform()
        time.sleep(3)
        #切换至alert并点击确定
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.alert.dismiss() #点击取消
        self.driver.switch_to.alert.send_keys() #输出文本
        # 切换至默认frame
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id('submitBTN').click()
        time.sleep(3)

if __name__ == '__main__':
    pytest.main(['test_alert.py','-v','-s'])


