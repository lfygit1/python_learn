# iframe操作
# 定位内嵌页iframe标签-->定位内嵌元素-->进行内嵌页元素操作-->返回主页面
# 定位内嵌页iframe标签
# page.frame_locator(selector=)    用xpath定位iframe标签，用于操作iframe内元素
# page.frame(name/url/selectors)    用selector 定位获取iframe标签，适合复杂场景
# 定位内嵌页元素，可以直接用get_by_role/placeholder 等进行定位
# frame_locator.locator(selector=)  在iframe内定位元素（无需显式切换）
# frame.locator(selector)   通过frame对象定位iframe内元素
# 切回主页面（退出所有iframe上下文）
# a=page.main_frame



import playwright
from playwright.sync_api import sync_playwright,expect
with sync_playwright() as f:
    browser = f.chromium.launch(headless=False,slow_mo=200)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})   # 创建浏览器上下文管理器，使页面隔离
    page1 = context.new_page()    # 创建页面1
    # page2=context.new_page()
    # page2.goto('http://192.168.110.77:9000/login')

    page1.goto(r'D:\Python_learn\web自动化\main-page.html')

    a=page1.get_by_test_id('main-username-input')
    a.fill('lfy123')
    expect(a).to_have_value('lfy123')
    page1.get_by_placeholder('请输入密码',exact=True).fill('lfy123..')

    # 带有iframe内嵌页的操作   方法一：
    # frame1=page1.frame_locator('//*[@id="info-iframe"]')   # 用xpath定位iframe标签
    # frame1.get_by_placeholder('请输入11位手机号',exact=True).fill('18530851185')  # 定位iframe内的输入框
    # frame1.get_by_test_id('iframe-email-input').fill('1324654@789.com')

    # 带有iframe内嵌页的操作   方法二：
    frame1=page1.frame('info-frame')  # 括号内写iframe标签信息中的name值
    frame1.get_by_placeholder('请输入11位手机号',exact=True).fill('18530851185')  # 定位iframe内的输入框
    frame1.get_by_test_id('iframe-email-input').fill('1324654@789.com')


    # 切回主页面
    d=page1.main_frame  # 必须有个变量接收，不然报黄
    duanyan1=page1.get_by_test_id('main-submit-btn').click()  # 点击iframe外的按钮，可以直接点击
    input()






