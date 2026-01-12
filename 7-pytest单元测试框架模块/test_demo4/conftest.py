# conftest.py

import platform
import pytest

def pytest_html_report_title(report):
    report.title = "自定义测试报告标题"

def pytest_configure(config):
    if not hasattr(config, '_metadata'):
        config._metadata = {}
    
    config._metadata.update({
        'Test Project': 'ceshixiangmu',  # 或者把中文值改为英文
        'Test Module': 'module1',
        'QA name': 'LFY'
    })

