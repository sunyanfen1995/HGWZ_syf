#encoding=utf-8
import pytest
#参数化

#01@pytest.mark.parametrize（）
import yaml


class TestData:
    #string
    @pytest.mark.parametrize("a,b",[(10,20),(20,30)])
    def test_data01(self,a,b):
        print(f"a+b:{a+b}")

    #tuple
    @pytest.mark.parametrize(("c,d"), [(10, 20), (20, 30)])
    def test_data02(self, c, d):
        print(f"a+b:{c+d}")

    #list
    @pytest.mark.parametrize(["A","B"], [(10, 20), (20, 30)])
    def test_data03(self, A, B):
        print(f"a+b:{A+B}")

#02 yaml:导入yaml包，加载文件
    @pytest.mark.parametrize(("a,b"), yaml.safe_load(open("./data.yl")))
    def test_data04(self, a, b):
        print(f"a+b={a+b}")


if __name__ == '__main__':
    pytest.main(['-s -v','test_data.py'])


