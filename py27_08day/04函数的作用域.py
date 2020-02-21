"""
============================
Author:柠檬班-木森
Time:2020/2/20   21:29
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
全局变量：直接定义在文件中的变量叫全局变量，在该文件的任何地方都可以访问。

局部变量：定义在函数内部的变量，叫局部变量,只能在定义该变量的函数内部使用。


"""

# 直接定义在文件中的变量叫全局变量
# a = 100
#
#
# def func():
#     # 定义在函数内部的变量，叫局部变量
#     c = 50
#     print(a)
#
# func()

# print(c)


# -------------------------函数的作用域----------------------------------------
# 局部变量的作用域：函数内部
# 函数参数的作用域：函数内部

# def func2(a, b):
#     c = 100
#     print(a)
#     print(b)
#
# func2(11, 22)

# 问题：如何在函数内部定义全局变量？
# 使用global进行声明

# print()
# # def func3():
# #     global c
# #     c = 1000
# #     b = 10
# #     f = 20
# # func3()
# # print(c)


# ----------------------------------
# 函数内部变量和全局变量同名时，在函数内部访问该变量，会优先使用局部变量
# a = 100
#
# def func():
#     a = 10
#     print("打印a的值：", a)
#
# func()


# -------------------错误示范------------------------
# a = 100
# def func():
#     print(a)
#     a = 1000
# func()

# a = 1000
# def func():
#     a = a + 1
#     print(a)
# func()

# ---------------------------------------------

a = 100

def func():
    global a
    a = 100000
    print("函数内部打印", a)

func()
print("函数外部打印", a)



# b = 10
#
# b = 100000
# print(b)
