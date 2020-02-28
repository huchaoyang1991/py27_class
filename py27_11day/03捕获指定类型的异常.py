"""
============================
Author:柠檬班-木森
Time:2020/2/27   21:15
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

# n = int(input("请输入一个数值："))


# print(n1)

# 捕获一个指定类型的异常
# try:
#     n = int(input("请输入一个数值："))
#     print(n1)
# except NameError as e:
#     print("代码出错啦")
#     print("当前出错的原因：",e)


# 捕获多个异常类型，
# 方式一：使用多个except(不同的异常类型，做不同的处理)
# try:
#     n = int(input("请输入一个数值："))
#     print(n1)
# except NameError as e:
#     print("代出现了namerror")
#     print("当前出错的原因：", e)
# except ValueError as e:
#     print("代出现了valueerror")
#     print("当前出错的原因：", e)


# 方式二：一个except(不同的异常类型，做相同的处理)
# try:
#     n = int(input("请输入一个数值："))
#     print(n1)
# except (NameError,ValueError,KeyError) as e:
#     print("代码出错")
#     print("当前出错的原因：", e)


# 捕获不确定的异常类型，可以直接捕获常见异常类型的父类
# try:
#     import requests
#     requests.get(url="www.baidu.com")
# except Exception as e:
#     print(e)