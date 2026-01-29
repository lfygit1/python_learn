# 不确定参数的个数时可以使用可变长函数
def sum2(*a):  # *a表示不确定有多少个参数，此时的a相当于一个容器
    c=0
    for i in a:
        c+=i
    return c
k=[2,3,4]
print(sum2(*k))   # 如果参数当容器使用时，需要再调用时，在实参位置加上*  位置传参

# print(sum2(1, 2))
# print(sum2(1, 2,3))
# print(sum2(1, 2,3,4))

def sum3(**a):   # 如果形参中有两个*时，a可以看做字典  关键字传参
    for k,v in a.items():
        print(k)
sum3(name='zs',age=18)  # 输出内容为name和age

h={'a':2,'b':4}
sum3(**h)   # 调用时也需要在实参中加上**

# 定义一个函数，取任意个数的最大数
k=[15,41651,6546,587,874,864,4654654654]
def max1(*a):
    c=max(k)
    return c
print(max1(*k))


