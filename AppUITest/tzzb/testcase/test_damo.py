#encoding=utf-8
import os


def test_os():
    curr = os.path.dirname(__file__)

    print(os.path.join(curr.split('tzzb', 1)[0], 'tzzb')+ '\\test.py')


