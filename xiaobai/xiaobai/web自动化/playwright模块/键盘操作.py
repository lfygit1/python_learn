# 键盘操作主要是通过page.keyboard实现
from playwright.sync_api import  sync_playwright
with sync_playwright()as p:
    browser = p.chromium.launch(headless=False,slow_mo=1000)
    page=browser.new_page()
    page.goto(r'http://shop.xiaobaisoftware.com/index.php/home')
    page.get_by_test_id('username-input').focus()
    # page.keyboard.type('shuibian',delay=200)   # 逐字插入   delay 延迟200毫秒后输入下一个文字
    # page.keyboard.insert_text('shuibian')   # 快速插入

    input()
    page.close()
    browser.close()