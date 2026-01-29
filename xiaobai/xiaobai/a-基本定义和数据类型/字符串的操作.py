# 容器：字符串、元组、列表、集合、字典
name = "xiaobai"

# 1、统计长度：len(字符串) 代表字符串中有几个字符
# print(len(name))

# 2、根据位置/下标取值，位置从0开始：字符串[位置]
# 第一个字符
# print(name[0])
# 最后一个字符
# print(name[len(name)-1])
# print(name[-1])

# 3、查找某个元素的下标：字符串.index(元素)
# 前闭后开，[3,7],[3,7)
# print(name.index('i',2,7))

# 4、统计次数：字符串.count(元素)
# print(name.count('x'))

# 5、替换：字符串.replace(old,new)
# print(name.replace('i','q'))

# 6、分割：字符串.split(字符)
# d = name.split('a')
# print(d)
# print(type(d))

# 7、小写转大写：字符串.upper()
# e = name.upper()
# print(e)

# 8、大写转小写：字符串.lower()
# f = e.lower()
# print(f)


k = ' xia  oh  '
# 9、去除左右两边的空格：字符串.strip()
# print(k.strip())  # 去除两边的空格
# print(k.lstrip())  # 去除左边的空格
# print(k.rstrip())  # 去除右边的空格、
# print(k.replace(' ',''))  # 去除所有空格

# 10、切片：字符串[start:end:step]
#     start:开始位置
#     end:结束位置
#     step:步长，默认1
print(name[1:5:1])  # 输出结果为 iaob  从下标为1的字母i开始，挨个往后数，到第五个字母b（下标为4）结束
print(name[1:5:2])  #  从下标为1的字母i开始，隔一个数一个，不包含第五个字符，所以输出结果为 io
print(name[:4])    # 输出结果为xiao 从头开始到第四个字符
print(name[4:])    # 输出结果为bai 从第四个字符开始到最后  不包括第四个字符
# 字符串的复制
print(name[:])
# 字符串的翻转
print(name[::-1])
# 11、拼接:+
print(name + str(12))  # 把12这个数字转为字符串，再拼接上name的值  输出结果为xiaobai12

a = '12'
b = '13'
print(a+b)   # 字符串相加，输出结果为1213
print(int(a)+int(b))  # 字符串转为数字再相加  结果为25



students = "任良;黄文庆;任贤齐;西门庆;方亿;方中山;贾彬;贾西贝 "
# 1、统计字符串的长度
# print(len(students))
# 2、统计方出现的次数
# print(students.count('方'))
# 3、打印庆的下标
# print(students.index('庆'))
print(students.index('庆',6,28))
# 4、打印字符串的第1个字符
# print(students[0])
# 5、打印字符串的最后一个字符
# print(students[-1])
# 6、打印字符串倒数第3个字符
# print(students[-3])
# 7、去除字符串右边的空格
# print(students.rstrip())
# 8、把中替换为文
# print(students.replace('中','文'))
# 9、把字符串安装;号分割
a=students.split(';')
print(a)
# 10、把任良取出
print(students[0:2:1])
# 11、把字符串翻转
print(students[::-1])
# 12、打印字符串最后一个字符的下标
print(len(students)-1)