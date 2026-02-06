# yaml 文件读取
import yaml
# pip show pyyaml   查看yaml的版本信息
# # 报红说明包为第三方包，需要下载
# 下载命令：pip install yaml==版本号 -i 清华源
# pip install pyyaml==6.0 -i https://pypi.tuna.tsinghua.edu.cn/simple/
#
# pip list 查看所有已安装的依赖
# pip show 依赖名   查看指定依赖的详细信息

# yaml.load()   # 读取yaml文件，转为Python对象
"""
server:
  port: 7010
  max-http-header-size: 10MB
#  设置项目名称
#  servlet:
#    context-path: /haha
#在服务器运行要改成服务器的IP
ip: 192.168.110.83
"""
# with open(r'D:\Python_learn\files\a.yml','r',encoding='utf-8') as f :
#     s =yaml.load(f,Loader=yaml.FullLoader)
#     print(s)
#     print(type(s))  # yaml文件中的内容为上面的格式时，返回字典格式


"""
- 喜欢
- 不喜欢
- 讨厌
格式时，返回列表格式
"""
# with open(r'D:\Python_learn\files\b.yaml','r',encoding='utf-8') as f :
#     s =yaml.load(f,Loader=yaml.FullLoader)
#     print(s)
#     print(type(s))  # yaml 文件中的内容为上面的格式时，返回列表格式



"""
- name:张三
  age：18

- name:李四
  age：19

- name:赵四
  age：20
"""
# with open(r'D:\Python_learn\files\c.yaml','r',encoding='utf-8') as f :
#     s =yaml.load(f,Loader=yaml.FullLoader)
#     print(s)
#     print(type(s))  # yaml 文件中的内容为上面的格式时，返回列表格式,列表中的值为字典格式
#
# 封装为yaml文件读取操作的函数
def read_yaml(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        s=yaml.load(f,Loader=yaml.FullLoader)
        return s
# read_yaml(r'D:\Python_learn\files\b.yaml')

# 封装为yaml文件写入操作的函数   yaml.dump()  #把Python对象写入到yaml文件里
#
# s = {'姓名':'张三','年龄':25,'性别':'男','爱好':'chi'}
# def wright_yaml(file_name):
#     with open(file_name,'w',encoding='utf-8') as f:
#         yaml.dump(s,f,allow_unicode=True)
# wright_yaml(r'D:\Python_learn\files\e.yaml')

