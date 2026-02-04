import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='session')  # 夹具 实现用例的前后置
def connect_db():
    con = '数据库连接信息'
    print('连接数据库')
    yield con    # 相当于return   yield 之前的是前置，后面的是后置
    print('关闭数据库')

