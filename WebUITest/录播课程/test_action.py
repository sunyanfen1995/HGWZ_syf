#encoding=utf-8
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
import pytest,time
from selenium.webdriver.common.keys import Keys

#
# class TestActionChains():
#     """ActionChains的使用"""
#     def setup(self):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(5)
#         self.driver.maximize_window()
#     def teardown(self):
#         self.driver.quit()
#
#     @pytest.mark.skip
#     def test_case_click(self):
#         """鼠标点击事件"""
#         self.driver.get('http://sahitest.com/demo/clicks.htm')
#         element_click = self.driver.find_element_by_xpath("//input[@value='click me']")
#         element_doubleclick= self.driver.find_element_by_xpath("//input[@value='dbl click me']")
#         element_rightclick= self.driver.find_element_by_xpath("//input[@value='right click me']")
#         #实例化一个action，传driver
#         action = ActionChains(self.driver)
#         #添加事件
#         action.click(element_click) #单击
#         action.context_click(element_rightclick) #右击
#         action.double_click(element_doubleclick) #双击
#         #执行事件
#         action.perform()
#
#     @pytest.mark.skip
#     def test_movetoelement(self):
#         """将光标移动到某一个元素上"""
#         self.driver.get("http://www.baidu.com")
#         ele = self.driver.find_element_by_link_text("更多")
#         action = ActionChains(self.driver)
#         action.move_to_element(ele)  #光标移动到某一个元素上
#         action.perform()
#         time.sleep(3)
#     @pytest.mark.skip
#     def test_dragdrop(self):
#         """拖拽效果"""
#         self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
#         drag_elem = self.driver.find_element_by_id("dragger")
#         drop_elem = self.driver.find_element_by_xpath("/html/body/div[2]")
#         action = ActionChains(self.driver)
#         #拖拽效果，三种写法都可以
#         action.drag_and_drop(drag_elem, drop_elem).perform()
#         # action.click_and_hold(drag_elem).release(drop_elem).perform()
#         action.click_and_hold(drag_elem).move_to_element(drop_elem).release().perform()
#         time.sleep(3)
#
#     @pytest.mark.skip
#     def test_keys(self):
#         """模拟键盘输入"""
#         self.driver.get("http://sahitest.com/demo/label.htm")
#         ele = self.driver.find_element_by_xpath('/html/body/label[1]/input')
#         ele.click()
#         action = ActionChains(self.driver)
#         action.send_keys("username").pause(1)  #输入文本并暂停一秒
#         action.send_keys(Keys.SPACE) #模拟按键盘上的space键
#         action.send_keys('tom').pause(1)
#         action.send_keys(Keys.BACK_SPACE).perform()   #删除键 ，执行action动作
#         time.sleep(3)
#         #还有其他操作：复制、粘贴等



class TestTouchAction():
    """touchAction的使用"""
    def setup(self):
        option = webdriver.ChromeOptions() #selenium启支持浏览器启动时设置参数
        option.add_experimental_option('w3c',False) #添加实验选项,
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_scroll(self):
        """模拟滚动"""
        self.driver.get('https://www.baidu.com/')
        ele_input = self.driver.find_element_by_id('kw')
        ele_search = self.driver.find_element_by_id('su')
        ele_input.send_keys('selenium学校')
        #实例化一个action
        action = TouchActions(self.driver)
        action.tap(ele_search) #点击
        action.perform()
        action.scroll_from_element(ele_input,0,1000).perform() #指定元素偏移量 x,y
        time.sleep(2)










if __name__ == '__main__':
    pytest.main(['-v','-s','test_action.py'])
