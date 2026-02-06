"""
page object model   页面模型设计思想
分层思想：
base:       封装playwright相关操作
page层：     封装每个页面的元素集和方法   后期维护主要是这一层，其他两个基本不变
testcase层： 测试用例层
三层之间的关系：  testcase层调用page,page继承base
"""
