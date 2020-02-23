"""
============================
Author:柠檬班-木森
Time:2020/2/22   11:29
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
with 语句

语法格式：
with open(文件名，打开模式) as 接收文件句柄的变量:
    # 文件的读写操作


使用with操作文件的优点：不用自己关闭文件，文件会自动关闭


"""
# f1 = open("reademe.txt","r",encoding="utf8")

with open("reademe.txt", "r", encoding="utf8") as f:
    print(f.read())
