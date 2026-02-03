# 多窗口操作核心是先捕获新窗口的page对象，在通过该对象定位并点击新窗口内的元素
# 1.监听新窗口   with context.expect_page() as p2_info:
# 2.获取新窗口信息     page1.locator('body>a.link-with-title').click()
# 3.或许新窗口        page2=p2_info.value
# 4.等待窗口内容加载完成  page2.wait_for_load_state('load')
# 5.对新窗口的元素进行操作  跟普通元素操作一致
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as f:
    browser=f.chromium.launch(headless=False,slow_mo=200)
    context=browser.new_context(viewport={"width":1920,"height":1080})   # 创建浏览器上下文管理器，使页面隔离
    # context.set_default_timeout(5000) # 修改为本地文件路径
  # 设置超时时间为5秒
    page1=context.new_page()    # 创建页面1
    page1.goto('file:///D:/python_learn/xiaobai/xiaobai/web自动化/playwright模块/test.html')   # 打开指定网址

    # # 监听新窗口
    with context.expect_page() as p2_info:
        page1.locator('body>a.link-with-title').click() # 点击页面1中的跳转超链接   用的是Css定位，复制selector
    page2=p2_info.value  # 获取新窗口
    page2.wait_for_load_state('load')   # 等待新窗口加载完成
    page2.locator('body>div.fixed-suspension-layer>div>div').click()   # 新窗口中点击弹窗的关闭按钮
    page2.get_by_placeholder('请输入您要搜索的商品关键字',exact=True).fill('手机')
    page2.get_by_role('button',name='搜索').click()
    page2.locator('//*[@id="main-nav-holder"]/div[1]/div/ul/li[2]/div/div[2]/div[2]/em').click()

    # 超链接到商品详情页
    try:
        with context.expect_page() as p3_info:   # 商品详情页
            page2.locator('#main-nav-holder>div:nth-child(2)>div>ul>li:nth-child(2)>div>div.goods-info>div.goods-name>a').click()
            page3=p3_info.value
            page3.wait_for_load_state('load')
            page3.get_by_role('link',name="").click()   # 点击+号添加一个商品
            page3.get_by_role('link',name="添加购物车").click()  # 点击添加购物车，会弹出提示框
            page3.on('dialog', lambda x: x.accept())
            page3.locator('body > div.w1200 > div.dss-detail.clearfix > div.dss-goods-summary > div.dss-buy > div.dss-btn > div > dl > dd.btns > a:nth-child(2)').click()
            page3.get_by_role('link',name='立即购买').click()
    except:
        page3.screenshot(path=r'C:\Users\XIAOBAI\Desktop\d.png', full_page=True, omit_background=False)


    input()