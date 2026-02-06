# 装饰器：在不改变代码（方法、单元、测试用例）的情况下给函数添加额外的功能
# 怎么用：在函数上添加@装饰器
# 在不同py文件中使用同一个前后置，需要使用conftest文件进行配置

import pytest

from g_文件读写.yaml文件操作 import read_yaml


@pytest.fixture(scope='class')  # 夹具 实现用例的前后置
def connect_db():
    con = '数据库连接信息'
    print('连接数据库')
    yield con    # 相当于return   yield 之前的是前置，后面的是后置
    print('关闭数据库')
def test_1(connect_db):
    print('123')
    print(connect_db)
@pytest.mark.skipif(1 == 1, reason='no reason')  # 有条件跳过
def test_2():
    print('456')
@pytest.mark.parametrize("aa", read_yaml(r"/files/c.yaml"))# 实现参数化  a指的是列表中的元素，列表中有几个元素，这个用例就执行几遍
def test_3(aa):
    print(aa)
@pytest.mark.run(order=1)  # 排序，让这个用例先跑
def test_4():
    print('jqk')
@pytest.mark.skip('备注：没有原因，就是不想执行这个')  # 无条件跳过
def test_5():
    print('QKA')
