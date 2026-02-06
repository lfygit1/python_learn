import allure

from web_auto.PO_test_example.page.index import IndexPage
from web_auto.PO_test_example.page.userinfo import UserInfo

@allure.feature('用户登录')   # 描述被测试的产品需求
@allure.story('用户登录成功')  # 用于描述测试需求
def test_login(page):
    ss = IndexPage(page)
    ss.dingwei1()

@allure.feature('用户查询学生信息')
@allure.story('用户查询成功')
def test_search_us(page):
    ss = UserInfo(page)
    ss.Search_useinfo()