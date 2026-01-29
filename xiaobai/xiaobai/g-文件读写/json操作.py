# json中只能用双引号"",字典中既可以用双引号，也可以用单引号，这是两者唯一的区别，其他都一样
d="""
{
"password":"123",
 "username":"admin"
}
"""
# print(d)
# print(type(d))
# 输出结果为
# {
# "password":"123",
#  "username":"admin"
# }
# <class 'str'>

# 可以用多行注释的方法把字典/json格式的数据转化为字符串进行输出

# 如果想取出输出结果username对应的值，就需要用到json操作  操作如下：
import json
# k=json.loads(d)   # 把json字符串转为python对象  这里是把字符串d转化为字典格式
# print(type(k))  # 输出为dict，说明json.loads把字符串d转化为了字典格式，这样就可以用字典取值的方式取出 username 对应的值
# print(k['username'])


h={'age':20,'sex':'女'}

g=json.dumps(h,ensure_ascii=False)  # 把Python对象转为json字符串
print(g)
print(type(g))  # 类型为str  字符串格式



# 把json文件转为Python对象
# with open(r'D:\Python_learn\files\a.json','r',encoding='utf-8') as fp:
#     s=json.load(fp)
#     print(s)

# # 把Python对象转存为json文件
# h = {'age': 20, 'sex': '女'}  # python 对象
# with open(r'D:\Python_learn\files\a.json','w',encoding='utf-8') as fp:
#     json.dump(h,fp,ensure_ascii=False)

