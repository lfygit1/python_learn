import pytest
import requests

@pytest.fixture(scope='session')
def test_login():
    res = requests.post(url='http://192.168.110.77:7010/xbschool/login',
                  json={"code": "1111", "username": "admin", "password": "123"},
                  headers={"content-type": "application/json;charset=UTF-8"}
                  )
    b = res.json()
    yield b
