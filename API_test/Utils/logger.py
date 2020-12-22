#encoding=utf-8

"""日志模块"""
import logging
from logging import handlers

import os

import time


class Logger(object):
    # # 设置日志级别关系映射
    # level_relations = {
    #     'debug': logging.DEBUG,
    #     'info': logging.INFO,
    #     'warning': logging.WARNING,
    #     'error': logging.ERROR,
    #     'crit': logging.CRITICAL
    # }
    #
    # def __init__(self, filename, level='info', when='D', backCount=3,
    #              fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
    #     self.logger = logging.getLogger(filename)
    #     format_str = logging.Formatter(fmt)  # 设置日志格式
    #     self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
    #     sh = logging.StreamHandler()  # 往屏幕上输出
    #     sh.setFormatter(format_str)  # 设置屏幕上显示的格式
    #     th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,
    #                                            encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
    #     # 实例化TimedRotatingFileHandler
    #     # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
    #     # S 秒
    #     # M 分
    #     # H 小时、
    #     # D 天、
    #     # W 每星期（interval==0时代表星期一）
    #     # midnight 每天凌晨
    #     th.setFormatter(format_str)  # 设置文件里写入的格式
    #     self.logger.addHandler(sh)  # 把对象加到logger里
    #     self.logger.addHandler(th)
    def __init__(self):
        self.logger = logging.getLogger("")
        LEVELS = {
            'NOSET': logging.NOTSET,
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }

        # 创建文件目录
        logs_dir = '../result/logs'
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
            pass
        else:
            os.mkdir(logs_dir)
        # 设置log保存位置
        timestamp = time.strftime("%Y-%m-%d", time.localtime())
        logfilename = '%s.log' % timestamp
        logfilepath = os.path.join(logs_dir, logfilename)
        rotatingFileHandler = logging.handlers.RotatingFileHandler(filename=logfilepath,
                                                                   maxBytes=1024 * 1024 * 50,
                                                                   backupCount=5,
                                                                   encoding='utf-8')
        # 设置输出格式
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        rotatingFileHandler.setFormatter(formatter)
        # 控制台句柄
        console = logging.StreamHandler()
        console.setLevel(logging.NOTSET)
        console.setFormatter(formatter)
        # 添加内容到日志句柄中
        self.logger.addHandler(rotatingFileHandler)
        self.logger.addHandler(console)
        self.logger.setLevel(logging.NOTSET)


    def info(self, message):
        self.logger.info(message)


    def debug(self, message):
        self.logger.debug(message)





