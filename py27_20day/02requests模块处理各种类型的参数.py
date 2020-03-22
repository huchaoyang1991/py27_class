"""
============================
Author:柠檬班-木森
Time:2020/3/21   9:56
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import requests

#       --------------------------post请求----------------------

url = "http://httpbin.org/post"

data = {"phone":"15567899876","pwd":"lemonban"}

# 发送请求
# 参数类型为："Content-Type": "application/json"，发送请求的时候，使用json来传递参数
# response = requests.post(url=url,json=data)

# 参数类型为：Content-Type": "application/x-www-form-urlencoded，使用data来进行传递
response = requests.post(url=url,data=data)

# 文件上传怎么传递参数：
# 文件上传接口的参数类型为："Content-Type": "multipart/form-data;文件应该使用files这个参数来进行传递
# data = {"phone":"15567899876","pwd":"lemonban"}
# file = {
#     "pic": ("bj01.png", open(r"C:\Users\MuSen\Desktop\page\image\ico.png", "rb"), "image/png")
# }
#
# response = requests.post(url=url, files=file,data=data)

# 获取返回数据
print(response.text)


# ----------------------------get请求-----------------------------------
# get请求的参数：查询字符串参数

# 处理方式一：放到url地址后面
# url = "http://httpbin.org/get?name=musen&age=18"

# 处理方式二：使用params来进行传递
# url1 = "http://httpbin.org/get"
# data = {
#     "name":"musen",
#     "age":18
# }
# response = requests.get(url=url1,params=data)
# print(response.text)