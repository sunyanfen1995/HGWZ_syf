#encoding=utf-8
#pytest-dependency插件

import pytest,time

@pytest.mark.dependency()
@pytest.mark.xfail(reason="deliberate fail")
def test_a():
    time.sleep(1)
    assert False
@pytest.mark.dependency()
def test_b():
    time.sleep(1)
    pass
@pytest.mark.dependency(depends=["test_a"])
def test_c():
    time.sleep(1)
    pass
#被依赖测试用例需要@pytest.mark.dependency装饰；
#被依赖用例测试通过后才能执行当前用例，否则跳过当前用例；
#depends列表里可以依赖多个用例
@pytest.mark.dependency(depends=["test_b"])
def test_d():
    time.sleep(1)
    pass
@pytest.mark.dependency(depends=["test_b", "test_c"])
def test_e():
    time.sleep(1)
    pass

class Test_ini():
    def test_ini01(self):
        print('pytest_ini01')

    def test_ini02(self):
        print('pytest_ini02')

    def test_ini03(self):
        print('pytest_ini03')


if __name__ == '__main__':
    pytest.main()
