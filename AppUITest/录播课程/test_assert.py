#encoding=utf-8
from hamcrest import *
import pytest

def test_hamcrest():
    assert_that(10, equal_to(10), reason='当前数不符合预期') #
    assert_that(8, close_to(10,3))   #上下浮动


if __name__ == '__main__':
    pytest.main(['test_assert','-s', '-v'])
