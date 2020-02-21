"""
============================
Author:柠檬班-木森
Time:2020/2/20   20:20
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
函数中的返回值：
函数中的返回值是由return来决定的


函数中可不可返回两个值？
可以

函数中没有return就没有返回值，调用函数得到的结果就是None
函数中返回多个值，直接写在return后面用逗号隔开就可以的


当函数执行到return的之后，那么会直接跳出函数，返回结果


"""


def func(a, b):
    c = a + b
    d = a - b
    return c, d
    # return之后不要写没有意义的代码，不会执行的
    # print("7890------")
    # print("-----7890")


# aa, bb = func(11, 22)
# print(aa)


# 定义一个打印三角形的函数，不需要返回值
def func2(n):
    # 功能：打印三级形
    for i in range(n):
        for j in range(i + 1):
            print("* ", end="")
        print()


# func2(5)

# 定义一个函数，用来计算给定一个数的2次方,调用完函数之后，获取这个数的2次方，去加上100


def func3(n):
    # print(n**2)
    return n ** 2


res = func3(8)

print("调用完函数之后得到的结果：", res)

# print(res+100)
