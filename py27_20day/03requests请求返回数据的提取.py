"""
============================
Author:柠檬班-木森
Time:2020/3/21   10:45
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import requests

# 第一步:准备请求的相关数据
# 接口地址
url = "http://api.lemonban.com/futureloan/member/login"

# 请求的参数
data = {
    "mobile_phone": "18189098765",
    "pwd": "lemonban"
}
# 请求头
headers = {
    "X-Lemonban-Media-Type": "lemonban.v1"
}
# 发送请求
response = requests.post(url=url, json=data, headers=headers)

# 打印返回内容
# text属性：
# res1 = response.text
# print(res1,type(res1))
# # 错误示范
# res2 = eval(res1)
# print(res2,type(res2))

# json方法：将字符串中的json类型数据转换为对应的python值
# 使用json方法的前提：返回数据必须是json格式的
# res3 = response.json()
# print(res3, type(res3))


# content属性
# res5 = response.content.decode("utf8")
# print(res5, type(res5))
