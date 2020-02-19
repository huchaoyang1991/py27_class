"""
============================
Author:柠檬班-木森
Time:2020/2/18   21:17
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
需求：通过for循环打印如下图案：

*
* *
* * *
* * * *
* * * * *

"""

# for i in range(5):
#     print("这是第{}行：".format(i+1))
#     for j in range(i+1):
#         print("*")
#

for i in range(5):
    print("这是第{}行：".format(i+1))
    for j in range(i+1):
        print("*",end="")

# 最终实现的代码
# for i in range(5):
#     for j in range(i+1):
#          # 加上end="",下一个print打印的时候不会换行
#         print("* ",end="")
#     # 这个print是为了让下一个print打印的时候换行
#     print() # print(end="\n")