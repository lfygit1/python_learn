from playwright.sync_api import sync_playwright

with sync_playwright() as p:   # 通过上下文管理器启动playwright,确保资源能自动释放
    chrome1=p.chromium.launch(headless=False,slow_mo=500)  # 启动chrome浏览器
    page = chrome1.new_page(viewport={"width":1680,"height":1050})  # 创建一个新页面 并设置窗口大小
    page.goto(r'D:\Python_learn\web自动化\test2.html')

    # 定位下拉框
    xiala1=page.get_by_test_id('province-select')  # 使用 data-testid 的值定位下拉框位置
    # 下标选择
    # xiala1.select_option(index=2)  # 下标传参
    # xiala1.select_option(value='shanghai')   # 使用value值传参
    # xiala1.select_option(label='广东省')  # 使用label标签传参











    input()
    page.close()
    chrome1.close()