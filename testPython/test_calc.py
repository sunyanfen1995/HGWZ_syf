#encoding=utf-8
#测试文件：计算器的case
#pytes实战01
import pytest
import sys
print(sys.path.append('..'))   #解决pythoncode不在当前路径下
from pythoncode.calc import Calculator

class TestCal:
    def setup(self):
        self.cal = Calculator()
        print("初始化一个计算机对象")
    def teardown(self):
        print("结束")


    @pytest.mark.add
    @pytest.mark.parametrize('a,b,result',[
        (1,1,2),
        (0.2,0.2,0.4)
    ],ids=['int','float'])#给用例命名
    def test_add01(self,a,b,result):
        # cal = Calculator()
        assert result == self.cal.add(a,b)

    @pytest.mark.add
    def test_add02(self):
        # cal = Calculator()
        assert 4 == self.cal.add(2, 2)

    @pytest.mark.div
    def test_div(self):
        # cal = Calculator()
        assert 1 == self.cal.div(2, 2)





