#encoding=utf-8

#yield生成器，
def func():
    for i in range(3):
        print(f'i={i}')
        # yield类似return 同时相同于暂停并且己住 上一次执行的位置；
        yield
        print('end')
f= func()
next(f) #next()方法获取生成器的下一个值
next(f)
next(f)

