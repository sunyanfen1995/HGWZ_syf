#encoding=utf-8

import pytest

class TestCaseDemo(TestBase):
    context = Context()
    context.load(str(__name__).split('.')[-1]+'.yaml')

    @pytest.mark.parametrize(
        "testcase",
        context.store.testcase.vakues(),
        ids = context.store.testcase.keys()
    )
    def test_param(self, testcase):
        self.context.run_steps_by_testcase(testcase)



