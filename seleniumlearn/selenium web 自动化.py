"""
selenium 模块介绍：
selenium 是一个自动化测试工具，用于测试浏览器，可以模拟用户操作，如点击、输入、选择等。
元素定位方式：
1. id：通过元素的id属性定位，id属性的值必须唯一，且不能重复。
2. name：通过元素的name属性定位，name属性的值必须唯一，且不能重复。
3. class name：通过元素的class属性定位，class属性的值可以重复。
4. tag name：通过元素的标签名定位，如div、span、input等。
5. link text：通过元素的链接文本定位，如a标签的文本内容。
6. partial link text：通过元素的部分链接文本定位，如a标签的文本内容。
7. xpath：通过元素的xpath路径定位，xpath路径是一个字符串，
8. css selector：通过元素的css选择器定位，css选择器是一个字符串，
9. index：通过元素的索引定位，索引从0开始，如div标签的第1个元素。
"""
# 模拟浏览器相关操作
# 1.创建浏览器对象
from selenium import webdriver  # 导入selenium模块
from selenium.webdriver.chrome.service import Service  # 导入Service模块
from webdriver_manager.chrome import ChromeDriverManager  # 导入ChromeDriverManager模块
import time  # 导入time模块

option = webdriver.ChromeOptions()  # 创建ChromeOptions对象
option.binary_location = r"D:\software\Google\Chrome\Application\chrome.exe"   # 指定浏览器路径
driver = webdriver.Chrome(options=option)  # 创建浏览器对象

driver.get('https://www.baidu.com')  # 打开百度首页
driver.maximize_window()            # 最大化浏览器窗口
driver.set_window_size(800,400)  # 设置浏览器窗口大小
p = driver.get_window_position()  # 获取浏览器窗口位置
print(p, 666666666666666666)  # 打印浏览器窗口位置
driver.set_window_position(100,100)

time.sleep(2)  # 暂停2秒
driver.quit()  # 关闭浏览器
