#encoding=utf-8
""""企业微信客户标签管理"""
import json
import jsonpath
import requests

#todo:底层具体的实现框架代码耦合严重，无法适用变化，比如公司切换了协议，如pb、dubbo
#todo:代码冗余，需要封装
#todo：无法清晰的描述业务
#todo：使用jasonpath表达更灵活的递归过滤
import time


def test_tag_list():
    """获取token"""
    corpid='ww3ad1d98f7b75e8c6'
    corpsecret= 'T5IMG_1NzwXl4H3ALsE4OoUZOVuPXVstWT3UeDF49V0'
    r = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        params={'corpid':corpid,'corpsecret':corpsecret}
        )
    token = r.json()['access_token']

    """查询全部标签"""
    r= requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        params ={
            'access_token':token
        },
        json={
            'tag_id':[]   #结构化数据，把json对象自动转化成字符串类型的内容
        }
    )
    # assert r.status_code == 200
    print(json.dumps(r.json(), indent=2)) #json格式的标准化输出

    """编辑标签"""
    tag_name = 'tag1_new'+ str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
        params= {
            'access_token': token
        },
        json={
            'id':'et_N2IEQAAcCOHbiU0fku2VJis3Xfdgw',   #tag id
            'name':tag_name                          #tag_name
        }
    )
    """
    不能直接判断200，因为可能存在缓存或者服务器欺骗行为，实际未更新成功
    所以此处需要再查询标签列表，判断新的标签名是否存在
    """
    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        params={
            'access_token': token
        },
        json={
            'tag_id': []  # 结构化数据，把json对象自动转化成字符串类型的内容
        }
    )
    print(json.dumps(r.json(), indent=2))  # json格式的标准化输出

    #这种方法太复杂，不建议
    # for group in r.json()['tag_group']:
    #     if group['group_name']=='python':
    #         for tag in group['tag']:
    #             if tag['name'] =='tag1_new':
    #                 print('ok')

    #采用列表表达式，如果有遍历到的，则tags列表长度不为0
    tags =[
        tag
        for group in r.json()['tag_group'] if group['group_name']=='python'
        for tag in group['tag'] if tag['name'] == tag_name
    ]
    assert tags != []

    #采用jsonpath 编写  对于jsonpath的使用还需要再掌握下
    #assert jsonpath(f"$..[?@.name='{tag_name}']")


def test_tag_add():
    """添加标签"""
    """获取token"""
    corpid = 'ww3ad1d98f7b75e8c6'
    corpsecret = 'T5IMG_1NzwXl4H3ALsE4OoUZOVuPXVstWT3UeDF49V0'
    r = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        params={'corpid': corpid, 'corpsecret': corpsecret}
    )
    token = r.json()['access_token']

    r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
                      params={
                          'access_token': token
                      },
                      json={
                            "group_name": "python_add",
                            "order": 1,
                            "tag": [{
                                    "name": "TAG_NAME_1",
                                    "order": 1
                                },
                                {
                                    "name": "TAG_NAME_2",
                                    "order": 2
                                }
                            ]
                        }
                      )
    print(r.json())
    print(jsonpath.jsonpath(r.json(), "$..name"))

def test_add_delect():
    """删除标签或者组"""
    corpid = 'ww3ad1d98f7b75e8c6'
    corpsecret = 'T5IMG_1NzwXl4H3ALsE4OoUZOVuPXVstWT3UeDF49V0'
    r = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        params={'corpid': corpid, 'corpsecret': corpsecret}
    )
    token = r.json()['access_token']

    r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
                      params={
                          'access_token': token
                      },
                      json={
                          "tag_name": [
                              'tag_add_@@@'
                          ],
                          "group_id": [
                          ]
                      }
                      )
    print(r.json())








