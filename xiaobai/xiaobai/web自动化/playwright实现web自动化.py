# 使用playwright进行web自动化，无需配置驱动器路径，只需要执行下面两个命令，下载好playwright依赖和浏览器驱动即可
# playwright 会自动等待，无需编写sleep 或者waitfor ,从根源上解决了元素找不到的问题
# 每个测试用例可使用独立的browsercontext，与其他用例完全隔离，避免状态污染
import time

# 同步异步的概念：
# 同步：顺序执行
# 异步：并行执行，适合高并发场景

# 前端包括：
# html:页面
# css:样式表
# js:动作

# get_by_text()  # 通过元素文本定位
# get_by_role()  # 通过ARAI角色定位
# get_by_test_id()  # 通过测试表示定位（最稳定）
# 下载playwright依赖
# pip install playwright==1.56.0 -i https://pypi.tuna.tsinghua.edu.cn/simple/
#
# 下载浏览器驱动
# [chrome firefox webkit]
# playwright install

import playwright

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:   # 通过上下文管理器启动playwright,确保资源能自动释放
    chrome1=p.chromium.launch(headless=False,slow_mo=500)  # 启动chrome浏览器
    page = chrome1.new_page()  # 创建一个新页面
    page.goto('http://192.168.110.77:9000/home')   # 打开指定网址

    # input1=page.get_by_test_id('username-input')  # 根据test_id进行定位  前提是必须要有 data-testid 这个属性
    # input1.fill('xioabai')  # 输入内容
    # input2=page.get_by_role("textbox",name="密码").fill('45345454') #

    page.get_by_placeholder('请输入账号').fill('admin')  # 用 get_by_placeholder 方式定位用户名输入框
    input3=page.get_by_placeholder('请输入密码').fill('123')   # 用 get_by_placeholder 方式定位密码输入框
    page.get_by_role("textbox",name='请输入验证码').fill('1111')  # 用 get_by_role 方式定位 可用于定位输入框、密码框搜索框等 参数值可以在F12页面中的Accessibility中找到
    page.get_by_role('button',name='登 录').click()   # 用CSS定位登录按钮
    page.locator('//*[@id="app"]/div/section/aside/ul/li[2]/div').click()   # 用 Xpath 定位信息管理按钮
    # page.get_by_role('generic',name='').click()
    page.get_by_role('menuitem',name='用户信息').click()  # 用 get_by_role 方式定位用户信息按钮
    page.locator('//*[@id="app"]/div/section/section/main/div/div[3]/div[2]/table/thead/tr/th[1]/div/label/span/span').click()  # 用xpath定位页面中全选复选框
    page.get_by_text('学生管理',exact=True).click()  # 用 get_by_text 定位   点击学生管理按钮  精确定位
    # page.get_by_text('成绩', exact=False).click()   # 用  get_by_text 定位 点击学生成绩按钮   模糊定位
    # page.on('dialog',lambda x:x.accept())
    page.get_by_role('menuitem',name='学生信息').click()
    page.get_by_role('button',name="新增").click()   # 用 get_by_role 定位，点击上传按钮
    page.locator('//*[@id="app"]/div/section/section/main/div/div[5]/div/div[2]/form/div[1]/div/div/input').fill('刘飞宇')  # xpath定位新增窗口的姓名栏位

    page.locator('//*[@id="app"]/div/section/section/main/div/div[5]/div/div[2]/form/div[2]/div/div/input').fill('2025-12-25') # xpath定位新增窗口的日期栏位
    page.locator('//*[@id="app"]/div/section/section/main/div/div[5]/div/div[2]/form/div[3]/div/div/input').fill('男')
    page.locator('//*[@id="app"]/div/section/section/main/div/div[5]/div/div[2]/form/div[4]/div/div/input').fill('25')
    page.locator('//*[@id="app"]/div/section/section/main/div/div[5]/div/div[2]/form/div[5]/div/div/input').fill('周口')
    page.locator('//*[@id="app"]/div/section/section/main/div/div[5]/div/div[2]/form/div[6]/div/div/input').fill('2512')
    page.get_by_role('button',name='确 定').click()
    # expect(input3).to_have_value('41684')   # 断言，失败会报错
    # page.get_by_label("用户",exact=False).fill('dsfsdfds')  # 用label进行定位  需要满足1.label标签，2.for属性和id属性一致  exact同样控制精确/模糊查询
    # page.get_by_title("用户",exact=False).fill('zcxvbvc')  # 用title属性定位  前提是必须有title属性


    input()
    page.close()
    chrome1.close()










    # # 定位下拉框
    # xiala1=page.get_by_test_id('province-select')  # 使用 data-testid 的值定位下拉框位置
    # # 下标选择
    # # xiala1.select_option(index=2)  # 下标传参
    # # xiala1.select_option(value='shanghai')   # 使用value值传参
    # xiala1.select_option(label='广东省')  # 使用label标签传参




