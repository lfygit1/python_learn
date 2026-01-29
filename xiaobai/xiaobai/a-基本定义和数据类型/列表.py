# 列表：容器的一种，用[]表示，列表里的元素有序可重复
# a = []
# print(type(a))
# 1、查看列表长度
# print(len(a))

b = [4,2,5,6,3,2]
# 2、统计元素出现次数
# print(b.count(3))

# 3、根据下标取值
# print(b[0])
# print(b[-1])

# 4、某个元素的下标
# print(b.index(5))

# 5、追加：列表.append(元素)
# b.append(7)
# print(b)
# 6、插入：列表.insert(下标,值)
b.insert(6,7)
print(b)
# 7、更新
# b[0]=8
# print(b)
# 8、删除，根据下标删：列表.pop(下标)
# b.pop()
# print(b)

# 9、删除，根据值删：列表.remove(值)
# b.remove(5)
# print(b)


c = [4,2,5,6,3,2]
# 10、排序：列表.sort()
# 升序
# c.sort()
# print(c)
# 降序
# c.sort(reverse=True)
# print(c)
# 11、清空
# b.clear()
# print(b)
# # 12、扩展：extend()
# d = ['a','b']
# c.extend(d)
# print(c)
#
# k = ['你','好',[3,4]]
# # 1、打印列表长度  输出结果为3 代表k这个列表中有3个元素
# print(len(k))
# # 2、打印列表最后一个元素
# print(k[-1])
# # 3、查看列表最后一个元素的类型
# print(type(k[-1]))
# # 4、列表追加9
# k.insert(3,0)
# print(k)
# # 5、在好后面插入吗
# k.insert(2,'吗？')
# print(k)
# # 6、删除下标为1的元素
# k.pop(0)
# print(k)
# # 7、把好删除
# k.pop(0)
# print(k)