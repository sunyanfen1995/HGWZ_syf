#encoding=utf-8
#被测文件
#实现计算机

class Calculator:
    def add(self,a,b):
        try:
            re = a+b
        except Exception as msg:
            return msg
        else:
            return re

    def sub(self,a, b):
        try:
            re = a - b
        except Exception as msg:
            return msg
        else:
            return re


    def div(self,a,b):
        try:
            re = a / b
        except Exception as msg:
            return msg
        else:
            return re

    def mul(self,a, b):
        try:
            re = a * b
        except Exception as msg:
            return msg
        else:
            return re

