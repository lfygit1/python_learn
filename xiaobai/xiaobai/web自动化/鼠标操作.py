from playwright.sync_api import  sync_playwright
with sync_playwright()as p:
    browser = p.chromium.launch(headless=False,slow_mo=1000)
    page=browser.new_page()
    page.goto(r'D:\Python_learn\web自动化\test2.html')

    # 悬停
    page.get_by_test_id('btn-hover').hover()
    page.wait_for_timeout(1000)
# 双击
    page.get_by_test_id('box-dblclick').dblclick()

# 右键单击
    page.get_by_test_id('box-rightclick').click(button='right')


# 拖拽  drag_to(目标位置)
    page.get_by_test_id('drag-1').drag_to(page.get_by_test_id('drop-container'))

# 按住/释放  page.mouse.down() /page.mouse.up()
#     page.get_by_test_id()
#     page.mouse.down()

    input()
    page.close()