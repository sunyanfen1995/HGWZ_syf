#encoding=utf-8
import pytest
import time
from selenium.webdriver import ActionChains

from WebUITest.录播课程.base import Base


class TestFile(Base):
    @pytest.mark.skip
    def test_file(self):
        """文件上传"""
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element_by_xpath('//*[@id="form"]/span[1]/span[1]').click()
        self.driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[2]/input').send_keys('C:\\Users\\毛线\\Desktop\\照片\\DSC02901.JPG')
        time.sleep(6)

if __name__ == '__main__':
    pytest.main(['test_file.py','-v','-s'])


