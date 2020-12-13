#encoding=utf-8
import allure
#方法2：使用装饰器的方式处理黑名单
def handle_black(func):
    def wrapper(*args,**kwargs):
        from frame_project.实战2.base_page import BasePage  #循环导入
        instance:BasePage = args[0] #作用等价于self
        try:
            result = func(*args,**kwargs)
            instance.error_num = 0
            return result
        except Exception as e:
            #截图，并存放到allure中
            instance.driver.save_screenshot('tmp.png')
            with open("tmp.png", 'rb') as  f:
                content = f.read()
            allure.attach(content,attachment_type=allure.attachment_type.PNG)
            # 设置计数器，判断是否超过最大错误次数
            if instance.error_num > instance.max_num:
                raise e
            instance.error_num += 1
            # 从黑名单中进行遍历元素
            for black_ele in instance.black_list:
                ele = instance.driver.find_elements(*black_ele)
                if len(ele) > 0:
                    ele[0].click()
                    #处理完黑名单后再查找原来的元素
                    return wrapper(*args,**kwargs)
            raise e  # 不存在黑名单元素就最直接抛出异常
    return wrapper



