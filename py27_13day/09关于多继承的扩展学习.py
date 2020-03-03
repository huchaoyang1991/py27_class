"""
============================
Author:柠檬班-木森
Time:2020/3/3   21:54
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
多继承



"""


class BaseA(object):
    attr_a = 100

    def func_a(self):
        print("func_a---------aaa")

    def func(self):
        print("func---------aaa")


class BaseB(object):
    attr_b = 999

    def func_b(self):
        print("func_b---------bbbb")

    def func(self):
        print("func---------bbb")


class MyTest(BaseA, BaseB):

    def func(self):
        print("func---------mytest")


m = MyTest()
# m.func_b()
# # m.func_a()
# # print(m.attr_a)
# # print(m.attr_b)

m.func()
