"""
传参方式：
1.默认值传参
"""
# def p1(name='xiaobai'):
#     print(f'hello {name}')
# p1()
# 以上代码没有使用return返回值，调用时也没有传入实参
# 执行结果为 hello xiaobai 说明使用了默认传参

# 2.位置传参
# def sum1(a,b):
#     c=a+b
#     return c
# print(sum1(1,3))

# 3.关键字传参
def sum1(a,b):
    c=a+b
    return c
print(sum1(a=2,b=3))

# 4.混合传参（既有关键字，又有位置）
# 使用混合传参时，位置传参要在关键字传参之前
# def sum1(a,b):
#     c=a+b
#     return c
# print(sum1(2,b=3))