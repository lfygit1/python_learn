# 单元测试框架实在自动化测试或者白盒测试中对软件中的最小单元（函数、方法）进行测试的框架
# 单元测试框架主要做什么：发现测试用例、执行测试用例、判断测试结果、生成测试报告
# 常用的插件：pytest-html（生产HTML测试报告）、pytest-xdist(多线程运行插件)、pytest-ordering(改变用例执行顺序插件)、pytest-rerunfailures（失败重跑插件）、alluer-pytest(allure报告插件)
# 插件安装：pip install -r requirements.txt -i 清华源   把需要的插件一次性写入txt文件中，使用这个命令一次性下载
# pip install - r C:\Users\XIAOBAI\Desktop\a.txt - i https: // pypi.tuna.tsinghua.edu.cn / simple
import pytest
# py文件必须以test_开头或者_tast结尾，文件中的函数名也必须是这样 文件中的类名必须以Test开头

# 在dos窗口(cmd窗口)中运行py文件或者test用例文件
# python + py文件的绝对路径/  pytest + test文件的绝对路径 -v -s

# 命令行窗口运行文件中某个用例 pytest test_1.py::test_sum3 -v -s


# 可以用把要执行的测试用例文件名写入到其他py文件中执行，文件内容参考   run.py