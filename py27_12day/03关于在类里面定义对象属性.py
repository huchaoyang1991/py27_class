"""
============================
Author:柠檬班-木森
Time:2020/2/29   10:27
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
定义在类里面的函数叫做方法：

__init__方法：初始化方法，在创建对象的时候，会自动调用执行里面的代码

关于方法中的第一个参数self:self代表的是对象，不用手动传，调用用改方法的时候会自动传


"""


# class Cat:
#     leg = "四条腿"
#     tail = "长尾巴"
#
#     def __init__(self):
#         """初始化方法"""
#         print("这里时打印self,",id(self),self)
#         print("这个时init方法在调用")
#
# kitty = Cat()
# print("这里打印的时kitty",id(kitty),kitty)
#
# print("--------------------------------------------------------")
# coffee = Cat()
# print("这里打印的时coffee",id(coffee),coffee)


# init方法的作用
class Cat:
    leg = "四条腿"
    tail = "长尾巴"

    def __init__(self, name, age, gender):
        """初始化对象属性"""
        self.name = name
        self.age = age
        self.gender = gender


kitty = Cat("凯蒂猫", 2, "母猫")
print(kitty.name)



coffee = Cat("加菲猫", 1, "公猫")
print(coffee.name)


#  定义一个学生类

class Students:
    attr1 = "学生"

    def __init__(self, name, age, class_):
        self.name = name
        self.age = age
        self.class_ = class_
