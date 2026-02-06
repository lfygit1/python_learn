import requests
import pytest
import allure

def test_stu_message(test_login):
    res2 = requests.get(url='http://192.168.110.77:7010/xbstudent/numSex',
                        params={'token': test_login['data']['token']})
    d = res2.json()
    assert d['code'] == 200 and d['message'] == '成功'


def test_edit_stu(test_login):
    res3=requests.post(url='http://192.168.110.77:7010/xbstudent/update'
                      ,headers={"content-type":"application/json",'token':test_login['data']['token']},
                       json={"id":6298,"name":"刘飞宇","inDate":"2028","sex":"女","age":30,"address":"周口","qiNum":"2512","aa":'null',"bb":'null'})
    f=res3.json()
    print(f)

def test_select_stu_info(test_login):
    res4=requests.get(url='http://192.168.110.77:7010/xbstudent/stuByPage?page=1&pageSize=10&username=&inDate=&qiNum=',
                      headers={"content-type":"application/json",'token':test_login['data']['token']})
    g=res4.json()
    print(g)

