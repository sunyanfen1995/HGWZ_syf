#encoding=utf-8
import configparser
import os


def test_congif():
    config = configparser.ConfigParser()
    print(os.environ['PATH'])
    config.read(os.path.join(os.environ['PATH'], 'iselenium.ini'))