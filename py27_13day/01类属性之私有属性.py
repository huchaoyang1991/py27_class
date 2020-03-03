"""
============================
Author:柠檬班-木森
Time:2020/3/3   20:14
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
类属性：

公有属性：既可以在类的内部使用，又可以在类外部使用。

私有属性：私有属性，使用双下划线开头。私有属性，只能在类的内部使用，在类外面无法使用。



"""


class MyClass:
    # 公有属性
    attr = 100
    # 私有属性
    __attr = 999

    def print_attr(self):
        print("属性attr:", self.attr)
        print("属性__attr", self.__attr)


# 私有属性，在类外部无法获取（访问）
# print(MyClass.__attr)
m = MyClass()
# print(m.__attr)

m.print_attr()
