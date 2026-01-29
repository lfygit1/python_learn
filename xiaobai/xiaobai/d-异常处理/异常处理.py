"""
异常处理机制：
try:
    可能发生异常的代码
except 异常类：
    捕获异常后执行的代码
finally：
    不管是否发生异常，都会执行的代码
"""
# 下面的代码会在14行发生异常，执行后会报错，然后14行以后的代码都不会再执行
# a=3
# b=2
# b=3-b-1
# c=a/b
# a+=2
# print(c)
# print(a)
# 加上异常处理机制后代码如下：
a=3
b=2
b=3-b-1
c=None
try:
    c=a/b
except ZeroDivisionError as e:
    print(e)
finally:
    a+=2
    print(c)
    print(a)