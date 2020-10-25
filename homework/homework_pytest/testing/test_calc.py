#encoding=utf-8
import yaml

from homework.homework_pytest.pytestcode.calc import Calculator
import pytest

class TestCalc:
    def setup(self):
        self.cal =  Calculator() #初始化计算机的一个实例
        # self.data = get_data


    @pytest.mark.parametrize('a,b,result',[
        (0,0,0),
        (0,1,1),
        (2,2,4),
        (-2,-2,-4),
        (0.1,0.1,0.2),
        (-0.1,-0.1,-0.2),
        (3.1111111111111,0,3.1111111111111),
        (111111111111111,0,111111111111111)
    ], ids=['均为0','有非0','正整数','负整数','正小数','负小数','长小数','长整数'])
    def test_add(self,a,b,result):
        """加法的测试用例"""
        assert result == self.cal.add(a,b)


    @pytest.mark.parametrize('a,b,result', [
        (0, 0, 0),
        (1, 0, 1),
        (2, 5, -3),
        (-2, -2, 0),
        (0.1, 0.1, 0),
        (-0.1, -0.5, 0.4),
        (3.1111111111111, 0, 3.1111111111111),
        (111111111111111, 0, 111111111111111)
    ], ids=['均为0', '有非0', '正整数', '负整数', '正小数', '负小数', '长小数', '长整数'])
    def test_sub(self,a,b,result):
        """减法法的测试用例"""
        assert result == self.cal.sub(a, b)
        pass

    @pytest.mark.parametrize('b', yaml.safe_load(open('./data.yaml', encoding='utf-8')),
                    ids = ['正整数','负整数','零','小数','超长整数','字母']
                             )
    @pytest.mark.parametrize('a',yaml.safe_load(open('./data.yaml',encoding='utf-8')),
                    ids = ['正整数', '负整数','零','小数', '超长整数', '字母']
                             )
    def test_mul(self,a,b):
        """乘法的测试用例"""
        a=a['a']
        b=b['b']
        print(self.cal.mul(a,b))

    @pytest.mark.parametrize('b', yaml.safe_load(open('./data.yaml', encoding='utf-8')),
                             ids=['正整数', '负整数', '零', '小数', '超长整数', '字母']
                             )
    @pytest.mark.parametrize('a', yaml.safe_load(open('./data.yaml', encoding='utf-8')),
                             ids=['正整数', '负整数', '零', '小数', '超长整数', '字母']
                             )
    def test_div(self):
        """除法的测试用例"""
        pass

if __name__ == '__main__':
    pytest.main(['-vs','test_calc.py'])