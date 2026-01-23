str1='12' 
str2='上海自来水来自海上'
#1、把str1转换为整数类型，并打印它的类型
# print(int(str1),type(str1))

#2、把str1倒置(反转)，并打印
# print(str1[::-1])

#3、输出str2中每个"来”的位置
# for i in range(len(str2)):
#     if str2[i] == '来':
#         print(i)

#4、输出str2中每个字对应的个数
# for i in range(len(str2)):
#     print(str2[i],str2.count(str2[i]))  # 字符串的count()方法

#5、求str2中哪些字是重复的
# for i in range(len(str2)):
#     if str2.count(str2[i])>1:
#         print(str2[i])

#6、遍历3-100之间的整数
# for i in range(3,101):
#     print(i)

#7、遍历3-100之间所有能被3整除的数
#8、找出3-100之间能被3整除的个数
# count=0
# for i in range(3,101):
#     if i%3==0:
#         count+=1
# print(count)

#9、遍历3-100之间数，当遍历到5、8、55、65的时候不打印，其余打印
# for i in range(3,101):
#     if i in(5,8,55,65):
#         continue
#     print(i)

l_2=[4,2,7,9,45,23,34,12,23,9] 
l_3=[7, 9, 45, 9] 
#10、向l_2的最后一位插入1 
# a=(l_2).append(1)
# print(l_2)
#11、打印l_2列表中所有能被9整除的数
# for i in l_2:
#     if i%9==0:
#         print(i)

#12、计算l_2列表中所有数的和
# print(sum(l_2))

#14、对l_2进行去重
# print(set(l_2))

#有字典
d2={
'name':['张三','张三丰','张无忌','李现','李四'],
'age':[21,23,21,23,34],
'address':['豫','浙','冀','晋','皖','鲁','陕','湘']
}
#16、对字典d_2进行遍历
for i in d2:
    print(i,d2[i])

#17、打印字典d_2中的key对应value的长度
# for i in d2:  # 遍历字典的key
#     print(len(d2[i]))
#18、打印字典d_2中姓张的名字
for i in d2['name']:
    if i.startswith('张'):  # 判断i是否以张开头
        print(i)
#19、遍历字典，如果key对应的value的长度为奇数，那么请在value中插入一个值
for i in d2:
    if len(d2[i])%2==1:
        d2[i].append('1')
        print(d2[i])
#20,请在address中添加江苏省的简称
d2[i].append('苏')
print(d2)

#21、矩阵转置
#将二维列表的列，变成行，形成个新列表
#第一列变成第一行
#第二列变成第二行
#第三列变成第三行
#第四列变成第四行
list04=[[1,2, 3,4],[5,6, 7,8],[9,10,11,12]]
#[[1,5,9],[2,6,10],[3,7,11],[4,8 12] 
# 方法一：使用嵌套循环
a = []
for i in range(len(list04[0])):  # 外层循环：原矩阵的列数（这里是4列）
    b = []
    for j in range(len(list04)):  # 内层循环：原矩阵的行数（这里是3行）
        b.append(list04[j][i])  # 将原矩阵的第j行第i列元素加入临时列表
    a.append(b)  # 将临时列表作为新矩阵的一行


for row in a:
    print(row)



#1、两数之和
#编写个函数add numbersa,b),接受两个参数并返回它们的和。 
def add(a,b):
    return a+b
print(add(1,2))

#2、默认参数函数
# 编写函数greet(name="Guest"),如果没有传入参数，默认返回'Hello,Guest',否则返回'Hello,[name]': 
# 有默认值参数的函数

def greet(name="Guest"):
    print(f'Hello,{name}')
greet('')