#encoding=utf-8
#测试用例通过传入fixture方法，获取测试/开发数据
def test_case01(cmdoption):
    print('测试环境')
    env,datas =cmdoption
    print(f'环境：{env},数据：{datas}')
    ip = datas['env']['ip']
    port = datas['env']['port']
    url = 'http://'+ip+":"+ port
    print(url)



