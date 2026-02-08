import requests
import pytest
import allure

from g_文件读写.yaml文件操作 import read_yaml


@allure.feature('获取学生信息')
@allure.story('查询成功')
@pytest.mark.parametrize("aa", read_yaml(r"D:\Python_learn\api_auto\cxxsxx.yaml"))
def test_stu_message(test_login,aa):
    with allure.step('访问接口'):
        res2 = requests.get(url=aa['url'],
                            params={'token': test_login['data']['token']})
    with allure.step('获取结果'):
            d = res2.json()
    with allure.step('断言'):
            assert d['code'] == 200 and d['message'] == '成功'

@allure.feature('编辑学生信息')
@allure.story('提交成功')
@pytest.mark.parametrize("aa", read_yaml(r"D:\Python_learn\api_auto\bjxsxx.yaml"))
def test_edit_stu(test_login,aa):
    with allure.step('访问接口'):
        res3=requests.post(url=aa['url']
                          ,headers={"content-type":"application/json",'token':test_login['data']['token']},
                           json={"id":6298,"name":"刘飞宇","inDate":"2028","sex":"女","age":30,"address":"周口","qiNum":"2512","aa":'null',"bb":'null'})
    with allure.step('获取结果'):
        f=res3.json()
        print(f)
@allure.feature('查看编辑过的学生信息')
@allure.story('修改信息成功')
@pytest.mark.parametrize("aa", read_yaml(r"D:\Python_learn\api_auto\xgxsxx.yaml"))
def test_select_stu_info(test_login,aa):
    res4=requests.get(url=aa['url'],
                      headers={"content-type":"application/json",'token':test_login['data']['token']})
    g=res4.json()
    print(g)

