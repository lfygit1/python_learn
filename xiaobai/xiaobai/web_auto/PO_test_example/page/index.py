import allure

from web_auto.PO_test_example.base.base1 import BaseCeng


class IndexPage(BaseCeng):
    # 元素集
    user = '//*[@id="app"]/div/div/div[2]/form/div[2]/div/div[1]/input'
    pwd = '//*[@id="app"]/div/div/div[2]/form/div[3]/div/div[1]/input'
    degnlu='//*[@id="app"]/div/div/div[2]/form/div[5]/div/button'
    # 方法
    def dingwei1(self):
        # 输入用户名
        with allure.step('输入用户名'):
            self.zhanghao(self.user,'admin')
            # 输入密码
        with allure.step('输入密码'):
            self.zhanghao(self.pwd,'123')
            # 点击登录
        with allure.step('点击登录'):
            self.denglu(self.degnlu)

