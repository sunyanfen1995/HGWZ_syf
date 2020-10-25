#encoding=utf-8
import pytest


#login是一个方法，对方法进行参数化
@pytest.mark.parametrize('login',[
    ('username1','passwd1'),
    ('username2', 'passwd2'),
], indirect=True) #设置这个参数为True，接收参数至方法名中
def test_ser01(login):
    print("search01")

def test_ser02(login):
    print("search02")
if __name__ == '__main__':
    pytest.main()
