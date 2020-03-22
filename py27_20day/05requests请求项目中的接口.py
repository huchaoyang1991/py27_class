"""
============================
Author:柠檬班-木森
Time:2020/3/21   11:09
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import requests
import jsonpath

# 请求头
headers = {
    "X-Lemonban-Media-Type": "lemonban.v2"
}

# 请求登录的接口
# 接口地址
url = "http://api.lemonban.com/futureloan/member/login"
# 请求的参数
data = {
    "mobile_phone": "18189098765",
    "pwd": "lemonban"
}
# 发送请求
response = requests.post(url=url, json=data, headers=headers)
res = response.json()

# 提取用户id和token值
member_id = jsonpath.jsonpath(res,"$..id")[0]
token = jsonpath.jsonpath(res,"$..token")[0]

"""
{'code': 0,
 'msg': 'OK', 
'data': 
    {'id': 7800007, 
    'leave_amount': 0.0,
     'mobile_phone':'18189098765', 
     'reg_name': '小柠檬', 
     'reg_time': '2020-03-21 09:49:27.0', 
     'type': 1, 
     'token_info': {
        'token_type': 'Bearer', 
        'expires_in': '2020-03-21 11:16:59', 
        'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjc4MDAwMDcsImV4cCI6MTU4NDc2MDYxOX0.-zjbWEbXF9qdfvW1Wn0640HZnv3Xkdrx0nDedRTcsgk_URgU185yA-e2SjQUvVfsjA-FpJSKSOF4jjB-Jyv47A'}
     },
  
  'copyright': 'Copyright 柠檬班 © 2017-2019 湖南省零檬信息技术有限公司 All Rights Reserved'}
"""

# 请求需求鉴权的接口
re_url = "http://api.lemonban.com/futureloan/member/recharge"
re_data = {
    "member_id":member_id,
    "amount":2000
}

headers = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "Authorization":"Bearer"+" "+ token
}
response2 = requests.post(url=re_url,json=re_data,headers=headers)

print(response2.text)

