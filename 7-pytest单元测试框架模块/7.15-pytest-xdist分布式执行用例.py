"""
pytest-xdist分布式执行用例
当测试用例数量很多时，一条条执行的速度会很慢，这时可以使用pytest-xdist插件进行分布式执行
一、分布式执行用例的设计原则
1.用例之间是独立的，用例与用例之间没有依赖关系，用例可以完全独立运行
2.用例执行没有顺序要求，随机顺序都能正常执行
3.每个用例都可以重复运行，运行结果不会影响其他用例的执行

二、pytest-xdist插件安装
pip install pytest-xdist

三 、pytest-xdist插件使用
原理：xdist会产生一个或者多个workers，workers通过master来控制；每个workers负责执行完整的用例集，
然后按照master的要求运行测试，而master不执行测试任务
常用命令： pytest -n auto （自动检测你的电脑有几个 CPU 核心，就启动几个“工人”帮你跑测试）。

案例参考：test_demo2文件夹下的test_demo23.py
"""