# while 循环
name = ['张三','李四','李五','赵六','六十七']
# 1.遍历列表中的姓名
# a=0
# while a <=3:
#     print(name[a])
#     a+=1

# 2.遍历列表中姓李的姓名
# a = 0  # 索引
# while a <=3:  # 循环次数
#     if name[a][0] == '李':  # 如果a的第一个字符是'李'
#         print(name[a])  # 输出a的值
#     a+=1 # 索引加1

# 3.列表中姓名只有两个字的
# a = 0
# while a <=3:  # 循环次数
#     if len(name[a]) == 2:  # 如果a的长度是2
#         print(name[a])  # 输出a的值
#     a+=1 # 索引加1

# 打印下标对应的姓名，结果是一个字典  while循环方法：
# s={}  # 定义一个空字典
# i=0 # 索引
# while i<len(name): # 循环次数  len(name) 指的是列表的长度
#     s[i]=name[i] # 索引对应的值
#     i+=1
# print(s)


# for 循环方法：
# s={}
# for i in range(len(name)):
#     s[i]=name[i]
# print(s)

#############################################################################################################
# for 循环
# 1.遍历列表中的数字
# a=[1,2,3,4,5,6,7,8,9,10]
# for i in a:  # 循环变量
#     print(i)

print('----------------------------------------------------------------------------------------------------')
# 2.打印列表中的偶数
# for i in a:
#     if i%2==0:
#         print(i)

print('----------------------------------------------------------------------------------------------------')

# 3.取出列表中的最大数
# 方式一：
# print(max(a))

# 方式二：
# b=a[0]  # 定义变量b，并赋值为列表a的第一个元素
# for i in a:  # 从列表 a中逐个取出元素，赋值给变量i
#     if i>b:  # 判断i是否大于b
#         b=i  # 如果i大于b，则将i的值赋给b
# print(i)

# 列表转化为字符串
# 方式一：
a=[1,2,3,4,5,6,7,8,9,10]
# s='' # 定义变量s，并赋值为空字符串
# for i in a:
#     s+=str(i) # 将i的值转化为字符串，并拼接到s中
# print(s)

# 方式二： 语法糖之列表推导式
# print(''.join([str(i) for i in a]))
# # 等价于
# s=''.join(map(str,a))
# print(s)

# for 循环根据下标取值
# 打印5次hello
# for i in range(5):
#     print('hello')
# # 等价于
# for i in range(1,6):
#     print('hello')


# 练习
# 1.有字符串如下
text='仍需@的JF@ @K的J K多@少积分@觉得  的时间 '
# 去除字符串中的空格
res=text.replace(' ','')
print(res)

# 2.有列表如下：
# 把列表中的姓名变成字典，且要求每个姓下有对应的人，如{'张':['张三','张四'],'王':['王五','王六'],'周':['周七']}
list=['张三','张四','王五','王六','周七']
s = {}
for name in list:  # 循环变量
    first_name = name[0]  # 取出姓名的第一个字符
    if first_name not in s: # 判断姓名是否在字典中
        s[first_name] = []  # 如果不在，则添加
    s[first_name].append(name)  # 添加姓名
print(s)

# 3.有列表如下：
k=[3,22,44,11,55]
# 循环打印上面列表中的元素
for i in k:  # 循环变量
    print(i)
print('----------------------------------------------------------------------------------------------------')
# 4.循环打印列表中的偶数
for i in k:  # 循环变量
    if i%2==0:  # 判断i是否是偶数
        print(i)
# 5.把列表转化为字符串，效果如下：3$22$44$11$55
print('$'.join(str(i) for i in k))

# 6.打印列表中的质数
for i in k:  # 循环变量
    for j in range(2,i):  # 从2开始到i-1的数字，
        if i%j==0:  # 判断i是否能被j整除
            break
    else:  # 如果i是质数
        print(i)
print('----------------------------------------------------------------------------------------------------')
# 7.打印10-100之间的质数
for i in range(10,101):
    for j in range (2,i):
        if i%j==0:
            break
    else:
        print(i)

print('----------------------------------------------------------------------------------------------------')


# 8.有列表如下：
g=[22,33,11,22,11,11]
# 统计每个元素的下标集合，结果如下：{22:[0,3],33:[1],11:[2,4,5]}
result = {}          # 1. 先准备一个空字典
i = 0                # 2. 下标从 0 开始
for value in g:      # 3. 依次取出列表中的每个值
    if value not in result:
        result[value] = []   # 4. 第一次出现，先给它一个空列表
    result[value].append(i)  # 5. 把当前下标放进去
    i += 1                   # 6. 下标 +1

print(result)

# 9.统计列表中每个元素出现的次数
count = {}              # 1. 空字典，用来存次数
for value in g:         # 2. 遍历列表里的每个元素
    if value not in count:
        count[value] = 1   # 3. 第一次出现，次数设为 1
    else:
        count[value] += 1  # 4. 不是第一次，次数 +1

print(count)


# 10.对列表进行去重
new_list = []           # 用来存去重后的结果

for value in g:
    if value not in new_list:   # 不在新列表里，才添加
        new_list.append(value)  # 添加

print(new_list)

# 使用for循环打印列表中的最小值
min_value = g[0]          # 1. 先假设第一个是最小值

for value in g:           # 2. 遍历列表
    if value < min_value: # 3. 如果发现更小的
        min_value = value # 4. 就更新最小值

print(min_value)
