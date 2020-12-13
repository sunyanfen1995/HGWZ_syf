#encoding=utf-8
def sigleton(func):
    """单例模式"""
    _instance={}
    def wrapper(*args,**kwargs):
        if func not in _instance:
            _instance[func] = func(*args,**kwargs)
    return wrapper

#装饰器:不修改代码的前提中实现新功能





