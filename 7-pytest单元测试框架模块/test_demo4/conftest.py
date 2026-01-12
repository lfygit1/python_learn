# conftest.py

import platform
import pytest

def pytest_html_report_title(report):
    report.title = "自定义测试报告标题"


def pytest_metadata(metadata):
    """直接通过 metadata 字典添加环境信息"""
    metadata.update({ 
        "测试项目": "zzy_exercise",
        "测试环境": "STAGING",
        "执行节点": "Jenkins Slave-02"
    })

# def pytest_configure(config):
#     if not hasattr(config, '_metadata'):
#         config._metadata = {}
    
#     config._metadata.update({
#         'Test Project': 'ceshixiangmu',  # 或者把中文值改为英文
#         'Test Module': 'module1',
#         'QA name': 'LFY'
#     })



