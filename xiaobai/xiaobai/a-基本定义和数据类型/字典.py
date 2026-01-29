# 字典：用{}表示，里面的元素是键值对，键是唯一的，键的类型一般是字符串
# 1、创建一个空字典
s = {}
a = dict()

k = {"name":"xiaobai","age":18,"ah":['吃','喝','玩']}

# 查： k[键]
print(k['name'])
print(len(k['ah']))
# 增： k[键]=值
k['dz'] = '淮北'
print(k)
# 修改：k[键]=值
k['name']='xiaohei'
print(k)
# 删除: del k[键]
del k['ah']
print(k)