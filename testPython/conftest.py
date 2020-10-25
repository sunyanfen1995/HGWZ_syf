#encoding=utf-8
import pytest
import yaml


@pytest.fixture(params=['user01','user02','user03'])
# @pytest.fixture()
def login(request):
    print("调用登录方法")
    print(request.param)
    # yield是一个生成器 可以激活fixture teardown方法
    yield ['username','passwd']
    print('end')

#收集上来的测试用例实现定制化功能
def pytest_collection_modifyitems(session, config, items):
    print("当前收集到的测试用例是：",items)
    print('当前收集到用例数量是：',len(items))
    #倒序执行收到到的测试用例
    items.reverse()
    #含有中文的测试用例名称，改写编码格式：
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape') #用例名称：item._nodeid，例如ids传值自定义的名称
        print(item._nodeid)
        #自定义标签
        if 'search' in  item._nodeid:
            item.add_marker(pytest.mark.diy)

    #为命令行增加自定义参数
    #通过 pytest --help可以查看

def pytest_addoption(parser):
        #parser 传入一个解析器
    mygroup = parser.getgroup("hogwarts")  # 设置一个group节点，group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",  # 注册一个命令行选项
                        default='test', #默认 --env=test
                        dest='env',
                        help='set your run env'  # 说明文案
                        )
#解析自定义命令行参数，为什么要解析，不解析会怎么样？
#这个方法名字不用固定
@pytest.fixture(scope='session')
def cmdoption(request):
    # return request.config.getoption("--env", default='test') #语句是固定方式
    #场景：test/dev环境切换
    myenv = request.config.getoption("--env", default='test')
    datapadth =''
    if myenv == 'test':
        datapadth = './data/test.yml'
    if myenv == 'dev':
        datapadth = './data/dev.yml'
    with open(datapadth,encoding="utf-8") as f:
        datas = yaml.safe_load(f)

    return myenv,datas

#动态参数化生成用例，作用是简化参数化
#原理：通过metafunc 方法获取所有fixture名称，如果有一个叫做param则动态生成数据
def pytest_generate_tests(metafunc):
    if 'param' in metafunc.fixturenames:
        metafunc.parametrize(
            'param',metafunc.module.datas,#通过metafunc获取数据，注意datas和myids的命令，后面在定义参数的也要与这边一致
            ids=metafunc.module.myids,
            scope='function'
        )















