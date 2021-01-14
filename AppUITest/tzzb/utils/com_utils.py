#encoding=utf-8
import yaml


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


