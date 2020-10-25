#encoding=utf-8
from time import sleep, ctime

import logging

import _thread

logging.basicConfig(level=logging.INFO)

#@如何守护：引入锁
loops  = [2,4]
def loop(nloop, nsec, lock):
    logging.info('start loop' +str(nloop)+ ' at'+ctime())
    sleep(nsec)
    logging.info('end loop' +str(nloop)+ ' at'+ ctime())
    lock.release() #锁释放

def main():
    logging.info("start all at " + ctime())
    locks =[]
    nloops = range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock() #实例化一个锁
        lock.acquire() #这是什么意思？
        locks.append(lock)


""""
def loop0():
    logging.info('start loop0 at'+ctime())
    sleep(4)
    logging.info('end loop0 at' + ctime())

def loop1():
    logging.info('start loop1 at'+ctime())
    sleep(4)
    logging.info('end loop1 at' + ctime())

def main():
    logging.info("start all at "+ ctime())
    #两个线程同时进行
    _thread.start_new_thread(loop0, ())#传函数，不用加（）
    _thread.start_new_thread(loop1, ())
    sleep(6) #为什么要加？因为主线程退出时子线程也被杀掉了。所以增加主线程的时间确保子线程完成

    #顺序执行
    # loop0()
    # loop1()
    logging.info("end all at " + ctime())
"""
if __name__ == '__main__':
    main()

