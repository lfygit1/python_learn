# s='上海自来水来自海上'
# # 如果s为回文，就打印它，否则打印自己的名字
# if s==s[::-1]:
#     print(s)
# else:
#     print('xiaobai')
# # 打印s中每个字符
# for i in s:
#     print(i)

l=[1,2,3,4,5]
# # 打印列表中的奇数
# for i in l:
#     if i%2!=0:
#         print(i)
# # 判断4是否在列表中，如果不在，把它追加进去，如果在，打印列表第一个元素
# if 4 not in l:
#     l.append(4)
# else:
#     print(l[0])
# # 把 s中的自来水换成白开水
# s=s.replace('自来水','白开水')
# # 统计 列表中 比3 大的元素个数
count=0
for i in l:
    if i>3:
        count+=1
print(count)
# 求列表中的最大值
print(max(l))
print('11'+33)