from web_auto.PO_test_example.base.base1 import BaseCeng


class UserInfo(BaseCeng):
    xxgl = '#app > div > section > aside > ul > li:nth-child(2) > div > span'
    yhxi = '//*[@id="app"]/div/section/aside/ul/li[2]/ul/li[1]'
    cxyum='//*[@id="app"]/div/section/section/main/div/div[1]/div[1]/input'
    cxan='//*[@id="app"]/div/section/section/main/div/div[1]/button[1]/span'
    xuanting='//*[@id="app"]/div/section/section/header/div[2]/div/div/span'

    def Search_useinfo(self):
        self.denglu(self.xxgl)
        self.denglu(self.yhxi)
        self.zhanghao(self.cxyum,'大黑')
        self.denglu(self.cxan)
        self.hove(self.xuanting)


