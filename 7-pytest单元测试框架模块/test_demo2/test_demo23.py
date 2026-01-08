# pytest-xdist分布式执行用例
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
import time

@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_experimental_option("detach", True) # 设置浏览器不自动关闭

    service = Service(r"D:\software\Chrome\Application\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
# def teardown(driver):
#     driver.quit()
def test_bing01(driver):
    driver.get("https://cn.bing.com/")
    time.sleep(5)
    search_box = driver.find_element(By.ID,"sb_form_q")
    search_box.click()
    search_box.send_keys("python")
    driver.find_element(By.ID,"search_icon").click()



    




