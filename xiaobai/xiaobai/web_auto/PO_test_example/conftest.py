import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='session')
def page():
    with sync_playwright() as f:
        browser = f.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})  # 创建浏览器上下文管理器，使页面隔离
        page1 = context.new_page()
        page1.goto('http://192.168.110.77:9000/login')

        yield page1
        page1.close()
        context.close()
        browser.close()