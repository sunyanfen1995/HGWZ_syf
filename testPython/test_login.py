#encoding=utf-8
import pytest


# @pytest.fixture()
# def login():
#     print("登录方法")
#     # yield是一个生成器 可以激活fixture teardown方法
#     yield ['username','passwd']
#     print('end')

def test_01(login):
    print(f'获取返回结果：login={login}')
    print("需要执行登录方法")

def test_02():
    print("不需要执行登录方法")

@pytest.mark.flaky(reruns=2, reruns_delay=2)
def test_example():
    import random
    # assert random.choice([True, False])
    assert 3==1

def test_assume():
    pytest.assume(1==2)
    pytest.assume(2==2)

from pytest import assume
@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
def test_simple_assume(x, y):
    with pytest.assume:
        assert x == y
        assert True
        assert False
    # with assume: assert x == y
    # with assume: assert True
    # with assume: assert False

if __name__ == '__main__':
    pytest.main()
