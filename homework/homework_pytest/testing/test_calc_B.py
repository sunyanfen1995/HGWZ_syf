#encoding=utf-8
import yaml

from homework.homework_pytest.pytestcode.calc import Calculator
import pytest




class TestCalc:
    cal = Calculator()  # 初始化计算机的一个实例
    with open("./dataB.yaml") as f:
        datas = yaml.safe_load(f)
        addmyids = datas['add'].keys()
        addmydatas = datas['add'].values()

        mulmyids = datas['mul'].keys()
        mulmydatas = datas['mul'].values()
        submyids = datas['sub'].keys()
        submydatas = datas['sub'].values()

        divmyids = datas['div'].keys()
        divmydatas = datas['div'].values()

    @pytest.mark.run(order =1)
    @pytest.mark.depency()
    @pytest.mark.parametrize('a,b,result',addmydatas,ids=addmyids)
    def test_add(self, a,b,result):
        """加法的测试用例"""
        assert result == self.cal.add(a,b)

    @pytest.mark.run(order = 2)
    @pytest.mark.dependency(depends=test_add)
    @pytest.mark.parametrize('a,b,result', submydatas, ids=submyids)
    def test_sub(self,a,b,result):
        """减法法的测试用例"""
        assert result == self.cal.sub(a, b)
        pass

    @pytest.mark.run(order=3)
    @pytest.mark.depency()
    @pytest.mark.parametrize('a,b,result', mulmydatas, ids=mulmyids)
    def test_mul(self,a,b,result):
        """乘法"""
        assert result == self.cal.mul()

    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=test_mul)
    @pytest.mark.parametrize('a,b,result', divmydatas, ids=divmyids)
    def test_div(self,a,b):
        """除法的测试用例"""
        pass

if __name__ == '__main__':
    pytest.main(['-vs','test_calc_B.py'])