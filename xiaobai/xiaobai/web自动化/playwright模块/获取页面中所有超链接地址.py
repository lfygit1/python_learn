# 获取超链接地址（a标签后的链接）
import playwright
from playwright.sync_api import  sync_playwright
with sync_playwright()as p:
    browser = p.chromium.launch(headless=False,slow_mo=1000)
    page=browser.new_page()
    page.goto(r'D:\Python_learn\web自动化\test.html')
    # 定位所有超链接
    # b=page.locator('a').all()   # 定位到所有的a标签，然后再去遍历
    # for i in b:
    #     c=i.get_attribute('href')
    #     print(c)

    # b=page.locator('a').all()   # 定位到所有的input标签，然后再去遍历
    # for i in b:
    #     c=i.get_attribute('title')
    #     print(c)

    d=page.locator('input')
    for i in range(d.count()):  # 统计页面中所有的input标签
        e=d.nth(0)   # 定位到具体想要显示的标签
        c=e.get_attribute('name')   # 获取该标签下的属性
    print(c)



    input()
    page.close()
    browser.close()