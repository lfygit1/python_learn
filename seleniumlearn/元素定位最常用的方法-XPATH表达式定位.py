"""
xpath 定位方法：
1.xpath 结合基本属性定位元素
2.xpath结合文本定位
3.xpath层级定位
4.xpath索引定位
5.xpath模糊匹配定位
"""

from selenium import webdriver  # 导入selenium模块
from selenium.webdriver.chrome.service import Service  # 导入Service模块
# from webdriver_manager.chrome import ChromeDriverManager  # 导入ChromeDriverManager模块
import time  # 导入time模块
from selenium.webdriver.common.by import By  # 必须导入 By 类
service = Service(executable_path=r"D:\software\Chrome\Google\Chrome\Application\chromedriver.exe") # 创建Service对象并指定驱动程序路径

option = webdriver.ChromeOptions()  # 创建ChromeOptions对象
option.add_experimental_option("detach", True)    # 设置浏览器不自动关闭  detach 在这里的意思是：分离/脱离：让浏览器进程与自动化脚本进程分离，即使脚本执行结束或异常退出，浏览器也不会被自动关闭
option.binary_location = r"D:\software\Chrome\Google\Chrome\Application\chrome.exe"   # 指定浏览器路径
# service = Service(ChromeDriverManager().install())  # 创建Service对象

driver = webdriver.Chrome(service=service,options=option)  # 创建浏览器对象
time.sleep(2)   # 等待两秒
driver.maximize_window()       # 最大化浏览器窗口
driver.get('https://www.baidu.com')  # 打开百度首页

# 1.xpath 结合基本属性定位元素
el1= driver.find_element(By.XPATH,".//li[@class='hotsearch-item even']")  # 通过xpath结合属性定位元素
print('el1:',el1.text)

# #  通过文本内容定位
# el2 = driver.find_element(By.XPATH, "//span[contains(text(), '围观')]")
# print('el2:',el2.text)

# 定位第一个热搜项
# el3 = driver.find_element(By.XPATH, "//li[1]//span[@class='title-content-title']")
# print(el3.text)

# # 通过父元素定位
# el4 = driver.find_element(By.XPATH, "//div[@id='hotsearch-content-wrapper']//li[2]//span[@class='title-content-title']")
# print(el2.text)