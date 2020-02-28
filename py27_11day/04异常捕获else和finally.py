"""
============================
Author:柠檬班-木森
Time:2020/2/27   21:35
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

# a = 1
#
# try:
#     print("--------------1-------------")
#     print(name)
#     print("--------------2-------------")
# except NameError as e:
#     print(e)
#
# print("--------------3-------------")

"""
else的应用场景

"""

# import os
#
# def copy_file(path):
#     try:
#         # 第一步：获取目标路径中所有的文件和目录
#         file_list = os.listdir(path)
#     except FileNotFoundError as e:
#         print("你传入的路径不对，出现了错误，错误提示:{}".format(e))
#     else:
#         # 第二步：遍历文件，
#         for item in file_list:
#             # 获取该文件的路径
#             file_path = os.path.join(path, item)
#
#             # 第三步：判断是文件还是目录，是文件的话就进行copy
#             if os.path.isfile(file_path):
#                 # 打开文件，读取内容
#                 with open(file_path, 'r', encoding='utf8') as f:
#                     contnet = f.read()
#
#                 # 在当前目录创建副本文件，写入内容
#                 new_file = 'cp' + item
#                 with open(new_file, 'w', encoding='utf8') as f:
#                     f.write(contnet)
#
# copy_file("python")


"""
finally的应用

"""

import random

# try:
#     # 对于有可能会出错的代码，我们可以对这行代码进行异常捕获
#     price = float(input("请输入橘子价格："))
# except NameError:
#     # try里面的代码，出现了异常执行except中的代码
#     print("输入价格的代码出错了")
# else:
#     # try里面的代码没有出现异常的时候执行else的代码
#     n = random.randint(1, 100)
#     sum_price = price * n
#     print("您购买的橘子为{:.2f}斤，每斤{:.2f}元，应支付金额为{:.2f}".format(n, price, sum_price))
# finally:
#     # 不管try的代码是否出现异常，都会执行
#     print("这个是finally中的代码")
#
# print("这个是finally之外的的代码")


# 通过finally来关闭文件

f = open("text.txt", "w",encoding="utf8")
try:
    n = int(input("请输入数字"))
except NameError:
    f.write("代码错误了")
else:
    f.write("代码没有错误了")
finally:
    print("finally执行了")
    f.close()