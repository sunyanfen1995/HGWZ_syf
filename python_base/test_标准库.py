#encoding=utf-8
import os,time


#2020/08/24
import math
import pytest


def test_biaozhun():
    """os模块
    """
    os.mkdir("testdir") #创建目录
    # print(os.listdir("./"))  # 当前目录下存在哪些文件,生成list
    os.removedirs("testdir") # 删除文件
    print(os.getcwd()) #获取当前目录的完整地址
    print(os.path())


    #练习题
    # print(os.path.exists("b")) #判断是否存在
    # if not os.path.exists("b"):
    #     os.mkdir("b")
    # if not os.path.exists("b/test.txt"):
    #     f = open("b/text.txt", "w")
    #     f.write("hello, os using")
    #     f.close()

    """time模块
    """
    # print(time.asctime()) #国外的时间格式
    # print(time.time()) #时间戳（从1974年来时计算的秒数，唯一）
    # print(time.localtime()) #时间戳转化为时间元组,默认当期秒数，可传值
    # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) #将当期时间戳转化为带格式的时间
    #
    # #练习题：获取两天前的时间
    # now_timestamp = time.time()
    # two_day_before = now_timestamp - 60*60*24*2
    # time_tuple = time.localtime(two_day_before)
    # print("两天前时间：",time.strftime("%Y-%m-%d %H:%M:%S", time_tuple))
    #
    # #练习题：获取三天后的时间
    # three_day_after = now_timestamp + 60*60*24*3
    # time_tuple2 = time.localtime(three_day_after)
    # print("三天后时间：", time.strftime("%Y-%m-%d %H:%M:%S", time_tuple2))


    """urlllib2:现在用的少了
    """
    # import urllib.request
    # response = urllib.request.urlopen("http://www.baidu.com")
    # print(response.status)
    # print(response.header)

    """math:
    """
    # print(math.ceil(5.4)) #返回大于等于X的最小整数,上限
    # print(math.floor(5.5)) #返回小于等于X的最大整数 下限制
    # print(math.sqrt(36)) #返回平方根


if __name__ == '__main__':
    pytest.main(['-vs test_biaozhun'])





