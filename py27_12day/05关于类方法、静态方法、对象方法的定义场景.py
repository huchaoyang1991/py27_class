"""
============================
Author:柠檬班-木森
Time:2020/2/29   11:24
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


class Cat:
    leg = "四条腿"
    tail = "长尾巴"

    def __init__(self, name, age, gender):
        """初始化对象属性"""
        self.name = name
        self.age = age
        self.gender = gender

    def move(self):
        print("快速移动")

    def skill2(self):
        """在方法内部，会使用到对象相关的属性，或方法，那么适合定义为对象方法"""
        print("{}施展了抓老鼠的技能".format(self.name))
        self.move()

    @classmethod
    def func(cls):
        """在方法内部只会使用到类属性"""
        print("这个是猫类共同特征:", cls.leg, cls.tail)

    @staticmethod
    def func2():
        """方法内部，既不会使用类相关的属性和方法，也不会使用对象相关的属性和方法"""
        print("这个是静态方法")

    @staticmethod
    def func11():
        print("这是一个普通的函数")


kitty = Cat("凯蒂猫", 2, "母猫")
