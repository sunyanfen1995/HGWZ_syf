#encoding=utf-8
import pytest

from frame_project.实战2.main_page import MainPage


# class TestMian:
#     def test_mian(self):
#         MainPage().goto_marketpage().goto_search()

#直接增强
def a():
    print('before')
    print('a')
    print('after')

#间接增强
def enhance(func):
    print('before')
    func()
    print('after')

def tmp(func): #func只需要加强的函数
    def wrapper(*args,**kwargs): #接收多个参数
        print('before')
        func(*args,**kwargs) #执行func
        print('after')
    return wrapper #wrapper()函数的调用  wrapper名字调用

@tmp
def a():
    print('a')




def test_a():
    a()
def test_a2():
    enumerate(a)

if __name__ == '__main__':
    pytest.main(['test_main.py','-s','-v'])