#encoding=utf-8
#pytest-order插件
import pytest
@pytest.mark.run(order=-1) #倒数第二个
def test_foo():
    assert True

@pytest.mark.run(order=1) #指定第一个
def test_bar():
    assert True

@pytest.mark.last #指定最后一个
def test_foo1():
    assert True

@pytest.mark.third #指定第三个
def test_bar1():
    assert True

if __name__ == '__main__':
    pytest.main()
