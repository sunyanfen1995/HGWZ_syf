#encoding=utf-8
from PO_wework_api.api.wework import Wework


class TestWework:

    def test_create(self):
        print(Wework().test_create(userid="syf1", name='sunyanfen', mobile="13362110922"))
