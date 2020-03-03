"""
============================
Author:柠檬班-木森
Time:2020/3/3   21:17
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


class TestData:
    url = "http://www.baidu.com"
    method = "get"


# 在类外面获取类属性
# print(TestData.url)

# getattr:获取类属性
# 参数1：类
# 参数2：属性名
# 参数3: 如果属性不存在，则返回该值
# res = getattr(TestData, "url1", "None")
# print(res)

# 动态获取属性的含义：
# name = input("请输入要获取的属性名:")
# res = getattr(TestData, name, "None")
# print(res)


# 类外面定义类属性
# 方式一：类.属性名= 属性值
# TestData.attr = 100
# print(TestData.attr)


# 方式二：使用setattr
# 动态设置属性：setattr
# 参数一：类
# 参数二：属性名
# 参数三：属性值
# setattr(TestData,"attr2",999)
# print(TestData.attr2)

# 需求：把下面两个列表中的数据设为属性和对应的属性值
title = ["name", "age", "gender"]
data = ["木森", 18, "男"]

# TestData.name = data[0]
# 设置属性
# setattr(TestData, title[0], data[0])
# setattr(TestData, title[1], data[1])
# setattr(TestData, title[2], data[2])


# for i in range(len(title)):
#     setattr(TestData, title[i], data[i])
# print(TestData.name)
# print(TestData.age)
# print(TestData.gender)

# 动态删除属性 delattr
# 参数一：类
# 参数二 ：属性名
# 方式一：关键字：del
del TestData.url
print(TestData.url)

# name = input("请输入你要删除的属性:")
# delattr(TestData,name)
#
# print(TestData.url)


# 扩展：使用del删除变量
# a = 100
# del a
# print(a)


# 判断属性是否存在：存在返回Ture,不存在返回False
res = hasattr(TestData, "url1")
print(res)
