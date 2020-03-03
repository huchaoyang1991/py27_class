"""
============================
Author:柠檬班-木森
Time:2020/3/3   21:46
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


class MyCalss:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def number(self):
        print("a+b的结果：", self.a + self.b)


class MyClassV2(MyCalss):

    def number(self):
        super().number()
        # 在原方法的基础上扩展的新功能
        print("a-b的结果：", self.a - self.b)
        print("a/b的结果：", self.a / self.b)



m = MyClassV2(11,22)
m.number()