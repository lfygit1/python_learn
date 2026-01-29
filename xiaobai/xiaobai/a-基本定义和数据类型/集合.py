# 集合：用{}表示，里面的元素无序且唯一
# 1、创建空集合
# a =set()
# print(type(a))

b = {5,2,4,2}

# 添加元素
# b.add(7)
# print(b)

# 删除
# b.remove(3)
# b.discard(3)
# print(b)

# 并集 |
# 交集 &
# 差集 -

h = {1,2,3}
g = {3,4,5}
print(h | g)
print(h & g)
print(g - h)