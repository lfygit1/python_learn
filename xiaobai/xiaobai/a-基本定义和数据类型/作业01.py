# 需求1：输入一个字符串，完成以下操作：
# 输出字符串的长度；
# 判断字符串是否以 "py" 开头；
# 提取字符串的最后 3 个字符；
# 将字符串反转并输出。
# a=input('输入一个字符串:')
# print(len(a))
# print(a.startswith('py'))
# print(a[-3:])
# print(a[::-1])
# 需求2：输入一段包含空格、标点的文本（例如："Hello, Python! I love coding in python."），完成：
# 去除文本两端的空格；
# 将所有字母转为小写；
# 统计文本中 "python" 出现的次数；
# 将文本中的逗号、感叹号替换为空格。


a = input('请输入一段包含空格、标点的文本: ')
# print(a.strip())
print(a.lower())
# print(a.count('python'))
print(a.replace(',',' ').replace('!',' '))
# 需求3：给定初始列表 nums = [5, 2, 9, 1, 5, 6]，完成以下操作：
# 在列表末尾添加数字 8；
# nums.append(8)
# print(nums)
# 删除列表中第一个值为 5 的元素；
# nums.remove(5)
# print(nums)
# 将列表中下标为 2 的元素改为 10；
# nums[2]=10
# print(nums)
# 对列表进行升序排序（原地排序）；
# nums.sort()
# print(nums)
# 找出列表中的最大值和最小值。
# print(max(nums),min(nums))
#
# 需求4：给定字典 student = {"name": "李四", "age": 20, "score": 88}，完成：
# 添加键值对 "gender": "男"；
# student = {"name": "李四", "age": 20, "score": 88}
# a=student
# a["gender"]='男'
# print(a)
# # 将 age 修改为 21；
# a["age"]=21
# print(a)
# 删除键 "score"；
# del a["score"]
# print(a)
# #
# 需求5：给定两个集合 s1 = {1, 2, 3, 4, 5} 和 s2 = {4, 5, 6, 7, 8}，完成：
# 求两个集合的交集（都存在的元素）；
# 求两个集合的并集（所有元素，去重）；
# 求 s1 相对于 s2 的差集（s1 有但 s2 没有的元素）；
# 判断 s1 是否包含元素 6；
# 向 s1 中添加元素 9，移除元素 3。
# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}
# print(s1 & s2)
# print(s1 | s2)
# print(s1 - s2)
# print(6 in s1)
# s1.add(9),s1.discard(3)
# print(s1)



# 题目 6：判断数字正负
# 需求：输入一个整数，判断它是正数、负数还是零，并输出对应的提示信息。
# 思路提示：使用 if-elif-else 结构，依次判断 num > 0、num < 0，剩余情况就是 0。
#
# num=input('输入一个整数')
# num=int(num)
# if num>0:
#     print('是正数')
# elif num<0:
#     print('是负数')
# else:
#     print('0')




# 题目 7：判断闰年
# 需求：输入一个年份，判断该年份是否为闰年。
# 闰年判断规则：
# 能被 4 整除但不能被 100 整除；
# 能被 400 整除。
# 满足任一条件即为闰年。
# 思路提示：使用 and/or 组合逻辑条件，核心公式：(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)。
#
# year = input('输入一个年份: ')
# year = int(year)
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print('闰年')
# else:
#     print('不是闰年')



# 题目 8：超市打折计算
# 需求：超市促销规则如下：
# 购物金额 < 100 元：无折扣，原价付款；
# 100 ≤ 金额 < 200 元：9 折优惠；
# 200 ≤ 金额 < 500 元：8 折优惠；
# 金额 ≥ 500 元：会员：6折优惠；
#               非会员：7折优惠；
# 输入购物金额，计算最终付款金额。
j=input('请输入购物金额：')
j=float(j)
h = 1
if j<100:
    print('原价付款')
    print(j)
elif j>=100 and  j<200:
    print('9折优惠')
    print(0.9*j)
elif j>=200 and j<500:
    print('8折优惠')
    print(0.8*j)
elif j>=500:
    if h == 1:
        print('6折优惠')
        print(0.6 * j)
    else:
        print('7折优惠')
        print(0.7*j)