# CSS定位方式  #id.class  使用方式：定位到元素，F12中右键，选择copy--selector  粘贴到locator后面的参数里即可

import playwright
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:   # 通过上下文管理器启动playwright,确保资源能自动释放
    chrome1=p.chromium.launch(headless=False,slow_mo=500)  # 启动chrome浏览器
    page = chrome1.new_page()  # 创建一个新页面
    page.goto(r'D:\Python_learn\web自动化\test.html')   # 打开指定网址
    # page .locator('#username').fill('liufeiyu')
    # page.locator('#password').fill('aidsfdsfd')


# XPATH定位  定位到元素，F12中右键，选择copy--xpath
    page.locator('//*[@id="username"]').fill('liufeiyu')



    input()
    page.close()
    chrome1.close()