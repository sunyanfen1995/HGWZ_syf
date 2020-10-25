#encoding=utf-8
import random


#08/14 标准库




"""
#08/14 异常+面向对象编程
def div(a,b):
    return a/b
try:
    print(div(1,1))
    list = [1,3,4]
    # print(list[3])
    # print(div(1,0))
except Exception as e: #基本类异常
    print(e)
except ZeroDivisionError as e: #具体的异常类型
    print(e)
else:
    print('没有异常的时候才会执行')
finally:#无论有无异常，最终都会执行
    print('最终都会被执行')
#自定义异常
class MyException(Exception):
    def __init__(self, msg):
        print(f"这是一个异常：{msg}")
def set_age(num):
    if num <=10 or num >200:
        raise MyException(f'值错误：{num}')
    else:
        print(f'年龄设置为：{num}')
set_age(-10)









#08/13 class python的输入与输出
#form
name = 'Tom'
age = 20
list = [1,3,4]
dict1 = {'name':'tom', 'gender':'male'}

print('my list is {}, dict is {}'.format(list, dict1))
print('my name is {},my age is {}'.format(name, age))

name_list = ['lili', 'tom', 'jerry']
dict2 = {'names':'tom', 'gender':'male'}
#list进行解包：*
print('we are :{}、{} and {}'.format(*name_list))
#dict进行解包：**
print('my name is {names}, my gender is {gender}'.format(**dict2))
#f stirng 推荐 f{变量名}:
# 不需要解包；
# 大括号内不支持\主义；
# 大括号内可以放表达式和函数；
print(f'my name is {name},age is {age} my list is {name_list},my dict is {dict2}')
print(f"my name is {name},age is {age} my list is {name_list[1]},my dict is { dict2['names']}")
print(f"my name is {name.upper()}") #函数
print(f"result is {(lambda x:x+1)(3)}") #表达式内有：需要用（）

#文件读取
f = open('data.txt')
print(f) #输出IO流
print(f.readable()) #判断文件死否可读
print(f.readline()) #输出一行
print(f.readlines()) #输出所有行
f.close() #及时关闭文件，避免死锁

#with语句块，可以将文件打开之后，操作完毕，自动关闭这个文件
with open('data.txt') as f :
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break


#08/12 class06 python模块
import sys
print(dir(sys))


#08/12 clss05 常用数据结构
#数据类型
#元组的不可变性
a = [5,5,5]
tuple_hogwatz = (1,2,a)
print(type(tuple_hogwatz))
#打印出内存地址
print(id(tuple_hogwatz[2]))
tuple_hogwatz[2][0] = 'a'
print(id(tuple_hogwatz[2]))
print(tuple_hogwatz)

#元组内置函数
a = (1,3,4,'a','a')
print('a的数量：',a.count('a'))
print('求数字3的索引：',a.index(3))
print(a.index('a')) #重复数字打印第一个索引

#集合的定义
set_a = {1}
set_b = set()
c = {} #是字典
print(type(set_a))
print(type(set_b))
print(type(c))


#集合的内置函数
a = {1,2,3}
b = {2,3,5}
print('a与b的并集：',a.union(b))
print('a与b的交集：',a.intersection(b))
print('a与b的差集：',a.difference(b))
a.add('bb')  #集合的添加
print(a)
c = 'adasdsdfsfesdf'
print(set(c)) #去重

#字典的定义
hogwarts_dict1 = {'a':1, 'b':2}
hogwarts_dict2 = dict(a=1,b=2)
print(type(hogwarts_dict1))
print(type(hogwarts_dict2))

#字典的内置函数
print('key值：',hogwarts_dict1.keys())
print('value值：',hogwarts_dict1.values())
print('删除指定的键值对，并返回被删除的键值对的values值：',hogwarts_dict1.pop('a'))
print(hogwarts_dict1)

print('随机删除一个键值对，并返回删除后剩余的键值对：',hogwarts_dict1.popitem())
a = {}
b = a.fromkeys((1,2,3),'a') #创建指定的key value值
print(b)
#推导式
print({i: i*2 for i in range(1,10)})


# str_a = "1234567"
# print(str_a[0:5])
# if str_a:
#     print('ceshi')
# else:
#     print('eee')
#
# #1-100de 求和
# result = 0
# for i in range(101,2):
#     # if i%2 ==0:
#     result+=i
# print(result)
#
# for i in range(1,10):
#     if i ==5:
#         continue
#     print(i)

# person_num = 0
# computer_num = random.randint(1,100)
# while True:
#     person_num = int(input('请输入：'))
#     if person_num > computer_num:
#         print('小一点')
#     elif person_num < computer_num:
#         print('大一点')
#     else:
#         print('猜对了')
#         break

# func = lambda x:x+1
# print('lambda:',func(2))

"""