# 1、输入姓名和年龄，格式化输出："我喜欢..,他..岁了"
# a=input('我喜欢：')
# b=input('几岁了：')
# print(f'我喜欢{a}，他{b}岁了')
# 2、定义两个整型变量a=7和b=2,对两个变量进行算术运算
# a=7
# b=2
# print(a+b)
# print(a-b)
# print(a/b)
# print (a%b)
# print(b**3)

# 有字符串
a = 'hi girl hello boy'
# 3、求字符串中有多少字符
# print(len(a))
# 4、求字符串中o出现的次数
# print(a.count('o'))
# 5、把字符串中的hi替换成hello
# print(a.replace('hi','hello'))
# 6、把y取出来
# b = a.index('y')
# print(a[b])
# 7、判断字符串中包含girl吗
print('girl' in a)
# 判断字符串以什么开头
# print(a.startswith('w'))
# 判断字符串以什么结尾
print(a.endswith('y'))
# 判断字符串是否包含
# print('girl' in a)
# print(a.__contains__('girl'))
# 8、把字符串转为大写
# print(a.upper())
# 9、把' girl'从字符串中取出来，赋值给变量b
b=a[2:7]
# print(b)
# 10、把变量b的左边空格去除
# print(b.lstrip())
# 11、从a字符串中取出yob
# b = (a[::-1])
# print(b[0:3])
# 12、对a进行翻转
# print(a[::-1])
# 有列表如下：
l_1 = [3,5,1,8,5]
# 4、求列表的长度
# print(len(l_1))
# 5、求列表的最大值
# l_1.sort(reverse=True)
# print(l_1[0])
# print(max(l_1))
# 6、求列表的最小值
# print(min(l_1))
# 7、求列表的和
# print(sum(l_1))
# 8、求列表的平均数
# print(sum(l_1)/len(l_1))
# 9、求列表中5出现的次数
# print(l_1.count(5))

# 10、对列表升序排序
# l_1.sort()
# print(l_1)

# print(sorted(l_1,reverse=True))
# 11、对列表降序排序
# l_1.sort(reverse = True)
# print(l_1)
# 12、删除列表最后一个元素
# l_1.pop()
# print(l_1)
# 13、移除列表中的3
# l_1.remove(3)
# print(l_1)
# 14、在列表中追加9
# l_1.append(9)
# print(l_1)
# 15、在列表的第2个位置插入1
# l_1.insert(1,1)
# print(l_1)
# 17、利用切片把列表的后3个元素取出
# print(l_1[2:5:1])
# print(l_1[-3:])
# 有列表l_2 = [5,6,3,2]
l_2 = [5,6,3,2]
# 18、把l_2扩展到l_1上

# l_1.extend(l_2)
# print(l_1)
# 19、取l_2列表中的第三个元素
# print(l_2[2])