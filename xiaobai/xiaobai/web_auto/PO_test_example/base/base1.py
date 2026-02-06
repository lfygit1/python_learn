from playwright.sync_api import sync_playwright


class BaseCeng():
    def __init__(self,page):   # 初始化属性
        self.page1=page
    # 定位
    def dingwei(self,a):
        b=self.page1.locator(a) # b 就是账号输入框这个元素
        return b
    # 输入
    def zhanghao(self,a,c):
        self.dingwei(a).fill(c)


    # 点击
    def denglu(self,a):
        v=self.dingwei(a).click()
        return v
    # 悬停
    def hove(self,a):
        a=self.dingwei(a).hover()

