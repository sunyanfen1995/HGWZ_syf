#encoding=utf-8
import yaml

import os


def get_data_from_yaml():
    """从yaml中读取数据"""
    with open('../data/accounts.yml') as f:
        accounts = yaml.safe_load(f)
        return accounts

def get_data_of_ajj():
    auto_fund = get_data_from_yaml()['Auto_Fund']
    return auto_fund['ajj']

def get_data_of_yfd():
    auto_fund = get_data_from_yaml()['Auto_Fund']
    return auto_fund['yfd']

def get_os_path(dirname):
    """获取指定目录下的绝对路径"""
    curr_file = os.path.dirname(__file__)
    tzzb_dir = os.path.join(curr_file.split('tzzb', 1)[0], 'tzzb')
    return os.path.join(tzzb_dir,dirname)


