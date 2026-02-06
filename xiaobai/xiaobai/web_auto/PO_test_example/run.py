import pytest
import os
if __name__ =='__main__':
    pytest.main(['--alluredir', 'report/result', 'testcase'])  # 生成json类型的测试结果
    split = 'allure ' + 'generate ' + './report/result ' + '-o ' + './report/html ' + '--clean'  # 将测试结果转为html格式报告
    os.system(split)  # system函数可以将字符串转化成命令在服务器上运行