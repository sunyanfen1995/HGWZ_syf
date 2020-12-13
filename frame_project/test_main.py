#encoding=utf-8
import importlib
import pytest
from frame_project.hello import A
import re

@pytest.mark.skip
def test_a():
    a= importlib.import_module("re")  #动态导入
    print(a.search(".*","xxxx"))

    get = importlib.import_module('hello')  #动态导入
    getattr(get, 'a')()  #反射：getattr(get, 'a')代表地址；再加一个()才能调用函数

@pytest.mark.skip
def test():
    globals()['a'] = 101  #全局变量:将变量存入其中，需要用的时候再取出来，本身就存了很多属性值在的，包括内置函数，如print等
    print(globals()['a'])
    print(globals()['__name__'])
    print(hasattr(re, 'a'))  #从re中找是否有a函数：输出为True 则有指定方法，否则就没有（用于区分package还是module）
    print(hasattr(A(), 'c'))
    print(hasattr(A, 'd'))  #指定d是静态方法的话是不需要实例化A的

def test_string_print():
    a='10'
    print(eval('a'))#将string当作python命令调用，即:eval() 函数用来执行一个字符串表达式，并返回表达式的值。
    print(type(eval('a')))
    print(a)
    print(type(a))


if __name__ == '__main__':
    pytest.main(['test_main.py', '-s', '-v'])



