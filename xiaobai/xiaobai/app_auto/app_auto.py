import time

import uiautomator2 as d

# app 自动化前置配置
# set PYTHONUTF8=1  # 设置字符编码
# pip install weditor ==0.7.3 -i https://pypi.tuna.tsinghua.edu.cn/simple/   # 使用定位工具定位app中的元素
# pip install uiautomator2 ==2.16.14 -i https://pypi.tuna.tsinghua.edu.cn/simple/  #  和app交互用的
# 检查：
# 打开模拟器，使用 adb devices 命令查看设备有没有连接 原则上会自动连接。
# 没有自动连接的需要手动连接：adb connect 127.0.0.1:60221（60221是夜神模拟器的端口号，模拟器不同，端口号不同）
# 连接好后cmd窗口运行：python -m weditor  此时会启动weiditor的页面，cmd窗口中开始下载 atx 软件，并安装至模拟器中
# 下载完成后点击 weiditor页面 中的 dump hierarchy ,点击完成后 weiditor页面中会出现模拟器中的页面，点击weiditor页面中的元素，对应信息会出现在右侧窗口中

# 连接设备
e=d.connect()
print(e.info)


e.app_start('app包名')  # 运行app
a=e(resourceId='com.ensoft.eudic:id/text_serch')  # 定位搜索框
a.send_keys('hello')  # 输入要搜索的内容
time.sleep(2)

# 1.屏幕操作
e.screen_on()  # 点亮屏幕
time.sleep(2) # 防止操作太快看不清屏幕，休息2秒再执行下一个
e.screen_off()  # 熄灭屏幕
print(e.info.get('screenOn'))  # 判断屏幕是否点亮


# 2.模拟物理按键
e.press('home')  # 按下home键
e.press('back')  # 按下返回键
e.press('volume_up')  # 按下音量+
e.press('volume_down')  # 按下音量-
# 3. 截图并保存（实战排错必备）
e.screenshot("screen.png")  # 保存到当前目录，命名为screen.png

# 4. 获取屏幕分辨率
print(e.window_size())  # 输出：(1080, 2400) （宽，高）

# 5.应用管理
e.app_start('app的包名')  # 可以连接wedictor后点击模拟器中的app，然后刷新wedictor，在右面信息中心查看
e.app_stop('app的包名')   # 关闭指定app
e.app_stop_all()  # 关闭所有app后台应用

# 6.卸载
e.app_uninstall('app的包名')   # 卸载指定应用
# 7. 安装
e.app_install('安装包的路径')

# 8. 查看app是否安装成功
print(e.app_info('安装包名'))
# 获取屏幕分辨率
width,height=e.window_size()
# 9.滑动屏幕
# 通用写法：起点在屏幕下方80%位置，终点在屏幕上方30%位置
#     start_x = width * 0.5  # 横坐标居中（避免滑到边缘）
#     start_y = height * 0.8  # 起点：屏幕下方80%
#     end_x = width * 0.5  # 横坐标不变
#     end_y = height * 0.3  # 终点：屏幕上方30%

# 执行滑动（持续0.5秒，速度适中）
# d.swipe(start_x, start_y, end_x, end_y, duration=0.5)


# app自动化测试怎么做？

# 使用uiautomator2+pytest+POM模型+jekins持续集成完成app自动化测试
# 使用weditor模拟用户对app进行操作，比如定位，点击，滑动等
# 使用pytest发现测试用例、执行测试用例、判断测试结果、生成测试报告
# 使用PO模型思想对我们的代码进行分层设计，分为3层，方便我们后期维护
# base:封装uiautomator2相关的操作
# page:封装每个页面的元素集和方法
# testcase:写测试用例

# 使用jenkins对代码进行持续集成，做到无人值守
