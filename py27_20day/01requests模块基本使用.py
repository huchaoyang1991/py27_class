"""
============================
Author:柠檬班-木森
Time:2020/3/21   9:36
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import requests

# 第一步:准备请求的相关数据
# 接口地址
url = "http://api.lemonban.com/futureloan/member/register"

# 请求的参数
data = {
    "mobile_phone": "18189098765",
    "pwd": "lemonban"
}
# 请求头
headers = {
    "X-Lemonban-Media-Type":"lemonban.v1"
}

# 发送请求
response = requests.post(url=url, json=data,headers=headers)
# 打印返回内容
print(response.text)
# 打印请求头内容
print(response.request.headers)

"""
# 默认的请求头
{'User-Agent': 'python-requests/2.21.0',
 'Accept-Encoding': 'gzip, deflate',
 'Accept': '*/*',
 'Connection': 'keep-alive', 
 'Content-Length': '50',
 'Content-Type': 'application/json'}
 
 # 自己添加过X-Lemonban-Media-Type字段的请求头
 {'User-Agent': 'python-requests/2.21.0', 
 'Accept-Encoding': 'gzip, deflate', 
 'Accept': '*/*', 
 'Connection': 'keep-alive',
 'X-Lemonban-Media-Type': 'lemonban.v1',
 'Content-Length': '50', 
 'Content-Type': 'application/json'}
 
"""
