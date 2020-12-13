#encoding=utf-8
import json
import pytest
from mitmproxy.genera_testcase import json_travel


def test_json_travel():
    with open("demo.json", encoding='utf-8') as f:
        datas = json.load(f)
        print(datas)
        # 格式化输出json
        print(json.dumps(json_travel(data= datas, array=3),indent=2, ensure_ascii=False))
        print(json.dumps(json_travel(data= datas, text=4),indent=2, ensure_ascii=False))
        print(json.dumps(json_travel(data= datas, num=6),indent=2, ensure_ascii=False))



if __name__ == '__main__':
    pytest.main(['-v','-s','test_travel.py'])

