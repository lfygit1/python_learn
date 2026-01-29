# 打开文件
# f=open(r'D:\Python_learn\files\read.txt','r',encoding='utf-8')  # 绝对路径前要加r进行转译
# # 读取内容
# print(f.read())

# 追加内容
# f=open(r'D:\Python_learn\files\read.txt','a',encoding='utf-8')  # 追加内容用 a 参数
# print(f.write('654653541'))   # 在文件中最后追加字符串

# 追加后再用 r 参数读取
# f=open(r'D:\Python_learn\files\read.txt','r',encoding='utf-8')
# print(f.read())

# 手动关闭文件
# f.close()

# 自动关闭文件
# with open(r'D:\Python_learn\files\read.txt','r',encoding='utf-8') as f:
    # 读取内容
    # print(f.read())
    # g=f.readlines()
    # print(g[1])   # 读取多行，输出结果为列表格式


    # while True:
    #     h=f.readline()     # 读取单行  输出结果为文件中的第一行
    #     if h:
    #         print(h)
    #     else:
    #         break
# 把文件读取操作定义成函数，方便调用
# def read_txt(file_path):
#     with open(file_path,'r',encoding='utf-8') as f:
#         return f.readlines()
# s =read_txt('D:\Python_learn\while和for循环\continue和break的区别.py')
# for i in s:
#     if 'continue' in i:  # 输出指定文件中 continue 所在行
#         print(i)

# 写文件
# def wright_txt(file_path,b,c):  # file_path 指的是文件路径   b 指的是读或者写 c 指的是写入内容
#     with open(file_path,b,encoding='utf-8') as f:
#         f.writelines(c)
# wright_txt(r'D:\Python_learn\files\wright.txt','a',['hello\n','hi\n','goodbye\n','hahahaha'])
# 指定路径下文件不存在会自动创建  绝对路径前要加r进行转译  模式为w意为覆盖，多次写入会覆盖上一次的写入内容
