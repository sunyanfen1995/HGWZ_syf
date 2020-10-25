#encoding=utf-8
#class11：对allure的使用

import allure
@allure.feature("登录模块") #功能点描述
class TestLogin():
    @allure.story("登录成功")  # 用户故事
    @allure.title("登录-登录成功") #用例标题
    @allure.severity(allure.severity_level.TRIVIAL) #用例等级 依次降低：blocker，critical，normal，minor，trivial
    @allure.testcase('https://testhomer.com','测试用例地址')
    def test_login_success(self):
        with allure.step("步骤1：打开应用"):  #操作步骤
            print("打开应用")
        with allure.step("步骤2：输入账密登录"):
            print("开始登录")
        print("这是登录：测试用例，登录成功")
        pass
    @allure.title("登录-登录失败")
    @allure.story("登录失败")
    def test_login_fail(self):
        print("这是登录：测试用例，登录失败")
        pass

    @allure.story("账号错误")
    def test_account_false(self):
        print("这是登录：测试用例，账号错误")
        pass
@allure.feature("搜索模块")
class TestSearch():
    @allure.story('case01')
    def test_case1(self):
        print("testcase01")

    @allure.story('case02')
    def test_case2(self):
        print("case02")

#关于allure添加附件的功能
@allure.feature('allure附件使用')
class TestAttach():
    def test_attach_text(self):
        allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)
        print('添加附件的格式：text')

    def test_attach_html(self):
        allure.attach("<b>这是一段htmlbody块</body>",name="html测试块", attachment_type=allure.attachment_type.HTML)
        print('添加附件的格式：html')

    def test_attach_photo(self):
        allure.attach("C:\\Users\\毛线\\Desktop\\照片\\DSC02901.JPG", name="图片测试", attachment_type=allure.attachment_type.JPG)
        print('添加附件的格式：JPG')

    def test_attach_video(self):
        allure.attach("C:\\Users\\毛线\\Desktop\\照片\\DSC02901.JPG", name="视频测试", attachment_type=allure.attachment_type.MP4)
        print('添加附件的格式：MP4')




