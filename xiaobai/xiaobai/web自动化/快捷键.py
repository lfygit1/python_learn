from playwright.sync_api import sync_playwright

with sync_playwright() as p:   # 通过上下文管理器启动playwright,确保资源能自动释放
    chrome1=p.chromium.launch(headless=False,slow_mo=500)  # 启动chrome浏览器
    page = chrome1.new_page(viewport={"width":1680,"height":1050})  # 创建一个新页面 并设置窗口大小
    page.goto(r'D:\Python_learn\web自动化\test.html')  # 打开网页
    user=page.get_by_test_id('username-input')  # 定位到用户名输入框
    user.fill('shuibian')  # 输入内容
    # user.focus()
    # 复制粘贴操作
    page.keyboard.press('Control+A')
    page.keyboard.press('Control+c')
    page.keyboard.press('Control+v')

    pwd=page.get_by_test_id('fullname-input').click()   # 定位到需要填入的位置
    page.keyboard.press('Control+v')   # 粘贴
# 长按实现复制粘贴
#     user.focus()
#     page.keyboard.down('Control')
#     page.keyboard.press('a')
#     page.keyboard.up('Control')


    input()
    page.close()
    chrome1.close()