names = ["张喻","张小张","李丽","白莲","李飞燕","邝玉龙"]
# 1、打印列表中的姓名
print (' '.join([str(i) for i in names]))
# 2、打印列表中的姓
for name in names:
    print(name[0],end=' ')
# 3、统计列表中有几个姓
# d=set()
# for name in names:
#     d.add(name[0])
# print(f'共有{d}{len(d)}个姓')

# 4、把名字中只有两个字的打印出来
# for i in names:
#     if len(i)==2:
#         print(i,end=' ')
# 5、统计姓李的有几个人
# print([name[0] for name in names].count('李'))
# a=0
# for i in names:
#     if i[0]=='李':
#         a=a+1
# print(a)
# 1、打印10以内的整数
# for i in range(0,11):
#     if i%2 !=0:
#         continue
#     else:
#         print(i)
# 2、打印10以内的奇数
# for i in range(0,11):
#     if i%2 ==0:
#         continue
#     else:
#         print(i)
# 3、打印10以内能被5整除的数
# for i in range(0,11):
#     if i%5 !=0:
#         continue
#     else:
#         print(i)
# 4、打印20以内既能被2整除，又能被3整除的数
# for i in range(0,21):
#     if i%2 ==0 and i%3==0:
#         print(i,end=' ')
# 5、打印s="你好，小白"字符串的字符
s="你好，小白"
for i in s:
    print(i,end='')

# k=[3,2,44,2,11]
# 6、打印列表中的元素
# for i in k:
#     print(i)
# 7、循环打印列表中的偶数
# for i in k:
#     if i%2==0:
#         print(i)
#
# 8、打印列表中能被11整数的数
# for i in k:
#     if i%11==0:
#         print(i)
#
#
k=[3,2,44,2,11,68]
# 9、打印列表中的回文数字
for i in k:
    if str(i)[::-1]==str(i):
        print(i)


# 10、统计列表中奇数的个数
# count=0
# for i in k:
#     if i%2!=0:
#         count += 1
# print(f'奇数个数为：{count}')
# 11、打印下标对应的值，结果如右{0:3,1:2,2:44,3:2,4:11}
# f={}
# for i in range(len(k)):
#     f[i]=k[i]
# print(f)

# 12、把列表转换为字符串，结果如右：3244211
# print(''.join(str(i) for i in k))
# 13、把列表转换为字符串，结果如右：3$2$44$2$11$
# c=''
# for i in k:
#     c =c+str(i)+'$'
# print(c)
# 14、把列表变成字符串，每两个字符之间用$连接，结果为：2$44$2$11
# print('$'.join(str(i) for i in k))
p=[3,2,44,2,11]
#15、计算列表中每个元素所在的下标集合，结果为：{3:[0],2:[1,3],44:[2],11:[4]}# k = {}
# dict={}
# xiabiao=0
# for j in k:
#     if j not in dict:
#         dict[j]=[]
#     dict[j].append(xiabiao)
#     xiabiao+=1
# print(dict)
#
#
s1= "hello every one"
#
# 1、计算字符串的长度
# print(len(s1))
# 2、打印字符串中的第一个字符
# print(s1[0])
# 3、打印字符串中第3个字符
# print(s1[2])
# 4、打印字符串中最后一个字符
# print(s1[-1])
# 5、把every取出来
# print(s1[6:11])
# print(s1.split(' ')[1])
# 6、对字符串进行翻转
# print(s1[::-1])
# 7、对字符串中的e删除
# print(s1.replace('e',''))
# 8、把字符串中的o替换成g
# print(s1.replace('o','g'))
# 9、计算字符串中e的个数
# print(s1.count('e'))
# 10、取出one
# print(s1[-3:])
# 11、y在字符串中吗
# print(s1.index('y'))
# 12、把字符串转大写
# print(s1.upper())
# 13、取出yrev
# print((s1[::-1])[4:8])
# 有字符串
s2="上海自来水来自海上"
# 13、怎么实现打印"来来"
# print(s2[3],s2[5],sep='')
# print(s2[3:6:2])
# 有列表
l1 = [1, 1, 2, 32, 1, 2, 3]
# 15、求列表元素的个数
# print(len(l1))
# 16、求1的个数
# print(l1.count(1))
#
# 17、判断l1个数是否为奇数，如果是就追加一个4进去，否则删除列表中的最后一个元素，最后打印这个列表

# if len(l1)%2 !=0:
#     l1.append(4)
# else:
#     l1.pop(-1)
# print(l1)

# 18、判断列表中的第3个数是偶数吗
# if l1[2]%2==0:
#     print('是偶数')
# else:
#     print('不是偶数')
# 19、5在列表中吗
# if '5' in l1:
#     print('在')
# else:
#     print('不在')
# 20、在列表的第3位插入6
# l1.insert(2,6)
# print(l1)
# 21、实现列表的去重
# print(set(l1))
# 24、删除列表的第4位
# l1.pop(3)
# print(l1)
# 25、求列表的最大值
# print(max(l1))
# 有字典如下：
d1 = {
    "name": "heihei",
    "age": 21,
    "sex": "man",
    "address": "周",
    "hobbies": ["吃", "喝", "玩", "乐"]
}
# 26、打印字典中的元素个数
# count=0
# for i in d1:
#     count+=1
# print('元素个数为：',count)

# print(len(d1))

# 27、求爱好个数
# count=0
# for i in d1['hobbies']:
#     count+=1
# print('爱好个数为：',count)

# print(len(d1['hobbies']))

# 28、打印名字
# print(d1['name'])
# 29、把性别修改成woman
# d1['sex']='woman'
# 30、年龄加1岁，请修改
# d1["age"]=d1["age"]+1
# print(d1)
# 31、把爱好中的吃删除
# d1['hobbies']= d1['hobbies'].pop(0)
# print(d1)
# 33、如果地址是周口，请把它修改成驻马店，否则给他追加一个爱好
if d1['address'] == '周口':
    d1['address']='驻马店'
else:
    d1['hobbies'].append('看电影')
print(d1)
# 34、打印1-100之间的整数
# for i in range(1,101):
#         print(i)
#
# 35、打印3-56之间能被3整除或能被4整除的数
# for i in range(3,57):
#     if i %3 ==0 or i%4==0:
#         print(i)
# 36、计算1-100之间所有整数的平均数
# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum/100)

# list =[]
# for i in range(1,101):
#     list.append(i)
# print(sum(list)/len(list))
# 37、统计10-50之间回文的个数,回文就是正反都一样，比如11呀 22呀
# count=0
# for i in range(10,51):
#     if i%11==0:
#         count+=1
# print(count)
# for i in range(10,51):
#     if str(i)[::-1]==str(i):
#         count+=1
# print(count)
# 38、打印10-100之间哪些数字是以1开头的

# for i in range(10,101):
#     if str(i)[0].startswith('1'):
#         print(i,end=' ')
# 39、打印30-100之间哪些数字是以2结尾的
# for i in range(30,101):
#     if str(i)[0].endswith('2'):
#         xiabiao+=1
#         print(i,end=' ')
# 40、统计30-100之间既是2的倍数又包含3的数的个数
# count = 0
# for i in range(30,101):
#     if i%2==0 and '3' in str(i):
#         count+=1
# print(count)
# # 有列表
l1 = ['我', '在', '哪', '我', '是', '谁']
# 41、列表生成字符串，用for循环实现
# 最后的结果为：我@在@哪@我@是@谁
s=''
for i in l1:
    s=s+str(i)+'@'
print(s[:-1])

# 42、输出每个字的索引列表，用字典表示
# d = {'我':[0,3],'在':[1],'哪':[2],'是':[4],'谁':[5]}
dict={}
xiabiao=0
for i in l1:
    if i not in dict:
        dict[i]=[]
    dict[i].append(xiabiao)
    xiabiao+=1
print(dict)

s='上海自来水来自海上'
for i in s:
    if str(i) ==str(i)[::-1]:
        print(i)
    else:
        print('lfy')