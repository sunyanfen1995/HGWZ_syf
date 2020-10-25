#encoding=utf-8
import pytest

#datas 和 myids 的命名要与conftest一致
datas =[ (0, 0),(1, 0)]
myids=['均为0', '有非0']

#param的命名要与conftest一致
def test_case(param):
    print(param)


