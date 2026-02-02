# 弹窗分为警告框（alert）、确认框（confirm）、提示框（prompt）
# 警告框（alert）只有确认按钮
# 确认框（confirm）有确认和取消按钮
# 提示框（prompt）有输入框，确认和取消按钮
import playwright
from playwright.sync_api import  sync_playwright
with sync_playwright()as p:
    browser = p.chromium.launch(headless=False,slow_mo=1000)
    page=browser.new_page()
    page.goto(r'D:\Python_learn\web自动化\test2.html')
    def sb(dialog):    # 设置弹窗监听器
        print(dialog.message)
        page.wait_for_timeout(2000)
        dialog.accept()
    page.on('dialog',sb)   # 调用监听器
    # 或者使用匿名函数设置弹窗监听器
    # page.on('dialog',lambda x:x.accept())
    # page.get_by_role("button",name='触发警告框（Alert）').click()


# 提示框处理
    page.get_by_test_id('btn-prompt').click()
    page.wait_for_timeout(1000)
    page.keyboard.type('shuibian',delay=200)   # 逐字插




    input()
    page.close()
    browser.close()
