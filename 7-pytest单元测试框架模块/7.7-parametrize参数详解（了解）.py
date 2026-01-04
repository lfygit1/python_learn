"""
parametrize参数详解（了解）

1.argnames 和 argvalues 参数的具体用法
2.inderict 参数用法
3.ids参数用法
4.scope参数用法
5.与其他mark一起使用
"""

# 1.argnames 和 argvalues 参数的具体用法
# 单参数 单值的情况

# 单参数 多值的情况
# arg values 可以传入多样的python数据类型：列表，嵌套了元组的列表 ，字典，字符串等 
# 传入多个值时，用例会被执行多次，每次取一个值去执行

# parametrize参数叠加使用


# 实例参考test_demo10.py