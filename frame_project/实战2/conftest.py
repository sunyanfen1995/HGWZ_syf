#encoding=utf-8

import pytest
import signal
import subprocess
import os


@pytest.fixture(scope='module', autouse=True)
def record_vedio():
    """录屏功能"""
    command="scrcpy --record tmp.mp4"
    #subprocess.Popen：执行shell命令并输出结果，可以封装成独立的一个方法
    p = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    print(p)  #打印执行内容
    yield
    # 杀死刚开启的进程
    os.kill(p.pid, signal.CTRL_C_EVENT)  #signal是进程间通信与异步处理的一种手段，当遇到并发性编程或者系统级的控制时，就需要我们能够控制程序的信号处理进程，完成一些额外的工作。 signal.CTRL_C_EVENT这是按下Ctrl-c时候发出的
