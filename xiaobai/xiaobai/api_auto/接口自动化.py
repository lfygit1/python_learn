# 导入requests 库
import requests as re
res=re.post(url='http://192.168.110.77:7010/xbschool/login',
        json={"code":"1111","username":"admin","password":"123"},
        headers={"content-type":"application/json;charset=UTF-8"}
        )
b=res.json()
# print(b)
# assert b['code'] == 200 and b['message'] =='成功'


# res1=re.get(url='http://192.168.110.77:7010/xbstudent/stuByPage?page=1&pageSize=10&username=&inDate=&qiNum=',
#             headers={"token":b['data']['token']})
# print(res1.json())

res2=re.get(url='http://192.168.110.77:7010/xbstudent/numSex',params={'token':b['data']['token']})
d=res2.json()
print(d)
assert d['code'] ==200 and d['message'] =='成功'

# 接口自动化怎么做？
# 使用requests+pytest+allure+jekins持续集成完成接口自动化
# 使用requests请求接口（post/get/delete/put等，其底层都是访问的request方法）
# 使用global 变量值或者conftest文件中配置作用域，让下游接口可以访问上游接口，实现多接口调用
# 使用pytest发现，执行测试用例，输出测试报告（html，allure等）

