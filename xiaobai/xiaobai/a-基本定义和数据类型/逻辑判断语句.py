# 格式：
'''
if 条件:
    条件成立，要执行的代码
else:
    条件不成立，要执行的代码
'''
# age = 15
# if age>18:
#     print('自由飞翔')
# else:
#     print('去学习')


# 键盘输入一个数，判断这个数是否是偶数，如果是打印**是偶数
# 否则打印这个数和3的和

# a = input('请输入一个数：')
#
# if int(a)%2==0:
#     print(f'{a}是偶数')
# else:
#     print(int(a)+3)

names = ['张三','李四','张无忌','李四光']
# 判断列表里第三个姓名是否姓张，
# 如果是，打印这个人的名字，
# 否则打印最后一个人的姓名
a = names[2]
if a[0]=='张':
    print(a)
else:
    print(names[-1])

# 90-100   优秀
# 70-90   良好
# 60-70   一般
# 0-60   不及格

s = input('给我一个分数呗：')
s = float(s)
if s>=90 and s<=100:
    print('优秀')
elif s>=70 and s<90:
     print('良好')
elif s>=60 and s<70:
    print('一般')
elif s<60:
    print('不及格')
else:
    print('你咋不上天，跟太阳肩并肩')