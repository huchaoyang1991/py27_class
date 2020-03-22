"""
============================
Author:柠檬班-木森
Time:2020/3/21   11:01
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import requests

# res = requests.get(url="http://www.lemonban.com/")
# 自动识别内容的编码方式，有可能识别不准确出现乱码
# print(res.text)

# 手动自动编码方式，对页面内容进行解码
# print(res.content.decode("utf-8"))


# 文件下载
res = requests.get(url="http://www.lemonban.com/images/upload/image/20190219/1550554131699.jpg")

print(res.content)

with open("lemon.png","wb") as f:
    f.write(res.content)