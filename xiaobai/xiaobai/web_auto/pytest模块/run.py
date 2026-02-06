import pytest
import os

if __name__=='__main__':
    # pytest.main(['-vs'])  #列表内写要运行的py文件名加详细（-v）的调试信息(-s)  如果只运行参数的话会运行这个文件所在目录的所有测试用例
    # pytest.main(['-n=2','test_shibian.py','-vs']) # 多线程运行测试用例，适合用例数量比较多的时候
    # pytest.main(['-vs','--reruns=2','test_1.py'])   # 失败重跑2次
    # pytest.main(['-vs', '-x', 'test_1.py'])   # 失败即停，下面的用例不会运行
    # pytest.main(['-vs', '--maxfail=2', 'test_1.py'])  # 最大失败次数达到2次后停止
    # pytest.main(['-vs','test_1.py','--html=./report/a.html'])  # 生成html的测试报告
    # pytest.main(['-vs', 'test_1.py', '--html=./report/a.html','--self-contained-html', '--capture=sys'])  # 把css合并到报告中
    pytest.main(['-vs','test_shibian.py'])