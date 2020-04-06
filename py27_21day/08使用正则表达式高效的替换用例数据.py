"""
============================
Author:柠檬班-木森
Time:2020/4/2   20:37
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import re

user = "python"
pwd = "lemonban"
name = "musen"
age = 18


# 使用字符串的方法进行替换（缺点，每次只能替换一个数据，效率太低）
# data = '{"user":#user#,"pwd":#pwd#,"name":"#name#","age":"#age#"}'
# data = data.replace("#user#", user)
# data = data.replace("#pwd#", pwd)
# data = data.replace("#name#", name)
# data = data.replace("#age#", str(age))
# print(data)

# 通过正则表达式来进行数据替换
# data = '{"user":#user#,"pwd":#pwd#,"name":"#name#","age":"#age#"}'
#
# re.findall("#(.*?)#",data)

"""
search: 匹配一个符合规范的数据，
第一个参数：匹配规则
第二个参数：被查找的字符串
返回值：匹配对象

"""
from common.handle_config import conf

data = '{"user":#user#,"pwd":#pwd#,"name":"#name#","age":"#age#"}'
res = re.search("#(.*?)#",data)
# 返回的式一个匹配对象
# print(res)
# 获取匹配到的数据
key = res.group()
print(key)
# 获取匹配规则中括号里面的内容
item = res.group(1)
print(item)
value = conf.get("musen",item)

data = data.replace(key,value)

print(data)