"""
requests模块模拟发送post请求
"""
import requests
res1=requests.post('https://httpbin.org/post', data={'key': 'value'})
print(res1.json())