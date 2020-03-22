"""
============================
Author:柠檬班-木森
Time:2020/3/17   21:15
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
from configparser import ConfigParser


class HandleConfig(ConfigParser):
    """配置文件解析器类的封装"""

    def __init__(self, filename):
        super().__init__()
        self.read(filename, encoding="utf8")


conf = HandleConfig("lemon01.ini")

res = conf.get("mysql", "port")
print(res)
