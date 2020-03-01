"""
============================
Author:柠檬班-木森
Time:2020/2/29   9:53
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
类定义：
关键字：class
语法：

class  类名：
    # 类里面的代码

类名的命名规范：遵循标识符的命名规范，风格采用大驼峰命名法（每个单词的第一个字母大写）


通过类创建对象：
对象 = 类名()


"""


class Cat:
    pass


class Dog:
    pass


class MyTestClass:
    pass


# 关于对象：有人叫对象，也有人叫实例

# 通过类创建对象(实例化对象)
kitty = Cat()

print(kitty, id(kitty))

coffee = Cat()
print(coffee, id(coffee))
