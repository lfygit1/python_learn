"""
格式：
for 变量 in 容器：
    循环体
"""
a = [2,5,3,4,6]
# for i in a:
#     print(i)

# 打印偶数
# for i in a :
#     if i%2==0:
#         print(i)

# 求列表中的最大数
# 方式一：
# print(max(a))
# a.sort()
# 方式二：
# a = [2,5,3,4,6]
# b = 0
# for i in a:  # 从 a 中逐个取值赋值给i
#     if i>b:   # 拿i的值与b的初始值0比较，如果i的值大于b，就执行下一步
#         b=i   # 把i 的值给到b
# print(i)
# 当列表中的数为负数时
# a = [-2,-5,-3,-4,-6]
# b=a[0]  # 设置b的来源为a里的某个数
# for i in a:  # 从 a 中逐个取值赋值给i
#     if i>b:   # 拿i的值与b的初始值比较，如果i的值大于b，就执行下一步
#         b=i
# print(i)

# 列表转化为字符串
# 方式一：
a = [2,5,3,4,6]
# s = ''  # 设置s变量为空值
# for i in a:  # 从列表a里逐个取值赋值给i
#     s = s+str(i)   # s 变量的值等于空值加上转化后的字符串
# print(s)

# 方式二：语法糖之：列表推导式 [str(i) for i in a]
print('-'.join([str(i) for i in a]))

# for 循环根据下标取值
# 打印5次hello
for i in range (1,6):  # 左闭右开，1 不写的话输出012345，说明默认从0开始
    print('hello')



