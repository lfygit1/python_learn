# 模拟键盘操作  1.输入文本   2.模拟按键操作

from selenium.webdriver.common.action_chains import ActionChains

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
time.sleep(0.2)   # 等待0.5秒
driver.maximize_window()       # 最大化浏览器窗口
driver.get('http://www.baidu.com')  # 打开鼠标点击测试网站

# 1.输入文本  当鼠标光标在输入框内时，可以使用 send_keys() 方法输入文本
ActionChains(driver).send_keys("hello world").perform()



# 2.当 鼠标光标在输入框外时，可以使用 ActionChains 类的 send_keys_to_element() 方法输入文本
# driver.get(r'D:\python_learn\seleniumlearn\鼠标-键盘操作测试.html')  # 打开鼠标点击测试网站
# el2= driver.find_element(By.XPATH,"//input[@id='textInput']")  # 通过xpath定位输入框
# ActionChains(driver).send_keys_to_element(el2,"hello world").perform()


# 3.模拟按键操作   按键的按下与松开
ActionChains(driver).send_keys(Keys.CONTROL+'a').perform() # 按下 CTRL+a