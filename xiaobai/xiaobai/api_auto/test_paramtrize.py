# parametrize  参数化实例    把要变的参数写在yaml文件中 ，读取之前写的读yaml文件的函数 用例中的参数调用yaml中的数据
import requests
import pytest

from g_文件读写.yaml文件操作 import read_yaml


@pytest.mark.parametrize('a',read_yaml(r'D:\Python_learn\api_auto\lg.yaml'))
def test_login(a):
    res = requests.post(url=a['url'],
                  json={"username": a['username'], "password": a['password']},
                  headers={"content-type": "application/json;charset=UTF-8"}
                  )
    b = res.json()
    print(b)
    # assert a['code'] ==b['code']