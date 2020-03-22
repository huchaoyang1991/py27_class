"""
============================
Author:柠檬班-木森
Time:2020/3/17   20:33
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
from configparser import ConfigParser

# # 第一步：创建一个配置文件解析器对象
conf = ConfigParser()
#
# # 第二步：将配置文件读取搭配配置文件解析器对象中
conf.read("lemon01.ini", encoding="utf-8")

# 第三步：配置文件内容写入
conf.set("mysql", "musen", "木森")

conf.write(fp=open("lemon01.ini", "w", encoding="utf-8"))
