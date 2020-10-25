#encoding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHgwarts():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://home.test.com/")
        self.driver.implicitly_wait(3)

    def test_wait(self):
        time.sleep(3)
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(By.XPATH,'//'))
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_selected(By.XPATH,'//'))
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(By.XPATH,'//'))










