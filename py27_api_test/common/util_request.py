"""
尝试对request模块进行二次封装（）
"""
import json
from configparser import ConfigParser

import requests

from py27_api_test.common.handle_config import conf


def request(server_url, path, method="POST", data=None):
    # url = "http://httpbin.org/post"
    # data = {"username": "chris", "pwd": "123456", "remarks": None}

    url = conf.get("api", server_url) + path
    print(url)
    if method == "POST":
        response = requests.post(url=url, json=data)
    elif method == "GET":
        response = requests.get(url=url, params=data)
    else:
        raise Exception("请求方法（method）只能是“POST”or“GET”")
    return response.json()


# 下载文件
def __filff(self):
    res = requests.get(url="http://www.lemonban.com/images/upload/image/20190219/1550554131699.jpg")
    with open("lll.jpg", "wb") as f:
        f.write(res.content)


data = {"name": 1, "grade": 100}
res = request(server_url="40008", path="post", data=data)
print(res)
