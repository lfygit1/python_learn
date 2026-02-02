# while 条件:
#     循环体

# a = 0
# while a<5:
#     print('hello')
#     a+=1

# 打印1-5之间的整数
# a = 1
# while a<=5:
#     print(a)
#     a+=1

# 打印1-5之间的偶数
# a = 1
# while a<=5:
#     if a %2 ==0:
#         print(a)
#     a+=1

# 统计1-5之间偶数的个数
# k = 0
# a = 1
# while a<=5:
#     if a %2 ==0:
#         k+=1
#     a+=1
# print(k)

# 打印列表中的偶数
# a = [2,3,5,4]
# b = 0
# while b<len(a):
#     print(a[b])
#     b+=1



# 1、遍历（循环）列表中的姓名
names = ['张三','李四','张无忌','李四光']
# a = 0
# while a < len(names):
#     print(names[a])
#     a +=1
# 2、遍历列表中姓李的姓名
# names = ['张三','李四','张无忌','李四光']
# i = 0
# while i < len(names):
#     a=names[i]
#     if names[a].startswith('李'):
#         print(names[a])
#     a +=1

# 3、列表中姓名只有两个字的有几个
# i =0
# k =0
# while i <len(names):
#     a =names[i]
#     if len(a) ==2:
#         k+1
#     i+=1
# print(k)


# 4、打印下标对应的姓名，结果是一个字典，如右：{0:'张三',1:'李四',2:'张无忌',3:'李四光'}
s={}
i=0
while i<len(names):
    s[i] = names[i]
    i+=1
print(s)


# 用下标的方式打印
# names = ['张三','李四','张无忌','李四光','wangwu']
print({names[i] for i in range(len(names))}) # len(names) 统计列表中的长度，即列表中元素的个数
#     print(names[i])

