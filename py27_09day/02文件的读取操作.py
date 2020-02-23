"""
============================
Author:柠檬班-木森
Time:2020/2/22   10:52
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
open函数：打开文件的
open(参数1，参数2,encoding="utf8")
参数1: 文件名/文件路径
参数2：文件打开的模式


文件夹打开的模式：
r:读取文件
a:写入
w:写入

#文件读取的方法
read():读取文件中所有的内容
readline():读取一行内容
readlines():按行读取所有的内容，返回一个列表


#关闭文件：
close:关闭文件

"""

# -------------------基本的读取操作--------------------
# 打开文件
# f = open(file="reademe.txt", mode="r",encoding="utf8")

# f = open("reademe.txt", "r", encoding="utf8")
# # 文件读取
# # 读取所有的内容
# # content = f.read()
#
# # 读取一行内容
# # content = f.readline()
#
# # 按行读取所有的内容，返回一个列表
# content = f.readlines()
#
# print(content)
#
# # 关闭文件
# f.close()

# --------------------指定路径读取-------------------------
# 注意事项：为了防止文件路径中的\t,\n等字符串转义字符被转义，建议加个r,关闭字符串转义

f = open(r"C:\project\py27_class\py27_01day\test_demo1.py","r",encoding="utf8")

print(f.read())

f.close()