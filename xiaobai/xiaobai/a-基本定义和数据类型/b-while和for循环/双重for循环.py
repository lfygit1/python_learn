# 打印1-5之间的整数

# for i in range(1,6):
#     print(i)
# 输出结果为
# 1
# 2
# 3
# 4
# 5   默认换行
# 实现不换行输出
# for i in range(1, 6):
#     print(i,end='')
# 输出结果为 12345 不在换行

# 双重for循环
# 如果想打印多次,可以使用双重for循环
# for i in range(3):
#     for i in range(1, 6): # 相当于把这行及以下的代码替换掉了下方写法的print
#         print(i,end='')
#     print()
#
# # 等价于
# for i in range (3):
#     print('12345')

# 打印
# ***
# ***
# ***
# for i in range(3):
#     for i in '***':   # in 后面跟的是容器，字符串也是容器
#         print(i,end='')
#     print()
print('---------------------------------------')
# 等价于
# for j in range(3):
#     for i in range(3):
#         print('*',end='')
#     print()

# 打印效果如下:
# *
# **
# ***

# for j in range(3):
#     for i in range(j+1):
#         print('*',end='')
#     print()

# 打印效果如下:
# ***
# **
# *

# for j in range(3):
#     for i in range(3-j):
#         print('*',end='')
#     print()
# 内层循环控制列，外层循环控制行

# 打印99乘法表
# for j in range(1,10):
#     for i in range(1,j+1):
#         print(f'{i}*{j}={i*j}',end = ' ')
#     print()

# 打印倒着的99乘法表
# for j in range(9,0,-1):  # -1为步长，意思是倒着数，每次减一
#     for i in range(j,0,-1):
#         print(f'{i}*{j}={i*j}',end = ' ')
#     print()



# a=2
# b=3
# 交换a和b的值
# c=a
# a=b
# b=c
# print(a,b)
# 或者使用元组解包的方法：
# a,b =b,a
# print(a,b)

k=[5,2,9,1,6]
# k.sort()  # 升序排序
# print(k)

# 冒泡排序
for i in range(len(k)-1):
    for j in range(len(k)-1-i):  # -i 可以优化运算步骤，不减i也是一样的运算结果
        if k[j]>k[j+1]:
            k[j],k[j+1] =k[j+1],k[j]
    print(k)

# 冒泡排序使用双重for循环实现
# 内层循环控制列表中的元素两两比较
# 如果前一个数大于后一个数，就交换位置
#
# 外层循环控制内层循环的轮数
