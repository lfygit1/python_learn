# 直接导入
import os
# os.mkdir('a')   # 在当前路径下创建一个名为a的单层目录,已存在的话会报错
# os.makedirs('b\c') #  在当前路径下创建一个多层目录
# os.rmdir('a')   # 删除单层空目录
# os.removedirs('b\c')  # 删除多层目录
import  shutil

dir1=os.getcwd()  # 获取当前所在目录 常用
print(dir1)

ll1=os.listdir(dir1)  # 列出指定路下的目录和文件
print(ll1)

a=os.path.exists(dir1)  # 检查文件或者目录是否存在
print(a)

b=os.path.isfile('D:\Python_learn\g-文件读写\json操作.py')     # 判断是否是文件
print(b)

c=os.path.isdir('D:\Python_learn')  # 判断是否是目录
print(c)

# os.remove('绝对路径.txt')  # 除指定文件

d=os.path.abspath('os模块使用.py')    # 获取文件的绝对路径
print(d)
"""
路径操作   较为常用
"""
path=os.path.join('D:\Python_learn\a-基本定义和数据类型','os模块使用.py')   # 连接路径
print(path)

"""


"""