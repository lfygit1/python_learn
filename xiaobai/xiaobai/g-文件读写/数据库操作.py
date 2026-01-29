# 下载第三库 pymysql   pip install pymysql==1.0.2 -i https://pypi.tuna.tsinghua.edu.cn/simple/
import pymysql

from  yaml文件操作 import read_yaml

# 192.168.110.77   root   xiaobai123
# 导入yaml文件读取函数
s = read_yaml(r'D:\Python_learn\files\mysql.yaml')

# 连接数据库，获取链接
con=pymysql.connect(host=s['host'],user=s['user'],password=s['password'],database=s['database'],port=s['port'])
# 获取游标（暂存SQL执行后的结果数据）只有查询才需要从游标里获取结果，
cur=con.cursor()
# 执行SQL
cur.execute('select username from user limit 3')
res=cur.fetchall()  # 获取查询结果
print(res)
# 提交commit  增删改都需要在SQL执行后进行提交  commit
con.commit()
# 关闭游标
cur.close()
# 关闭连接
con.close()