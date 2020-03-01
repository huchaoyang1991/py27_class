"""
============================
Author:柠檬班-木森
Time:2020/2/29   10:56
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
特征  +  行为

特性:属性(类属性，和实例属性)
行为:方法(类方法，实例方法)，方法的本质就是类里面的函数



实例方法：第一个参数是self，self代表的是对象本身，那个对象调用该方法，self就代表那个对象
实例方法：只能通过对象去调用

类方法：@classmethod进行装饰（标识）
第一个参数是cls,cls代表的是类本身



静态方法：@statictmethod进行装饰（标识）



"""


class Cat:
    leg = "四条腿"
    tail = "长尾巴"

    def __init__(self, name, age, gender):
        """初始化对象属性"""
        self.name = name
        self.age = age
        self.gender = gender

    def skill1(self, skill_name):
        print("{}施展了抓老鼠的技能：{}".format(self.name, skill_name))

    def skill2(self):
        print("施展了爬树的技能")

    @classmethod
    def func(cls):
        print(cls)
        print("这个是类方法")

    @staticmethod
    def func2():
        print("这个是静态方法")


kitty = Cat("凯蒂猫", 2, "母猫")
# coffee = Cat("加菲猫", 1, "公猫")
# print(kitty.name)
# print(coffee.name)

# kitty.skill1("往前扑")
# coffee.skill1("从天而降")

# li = [11, 22, 33, 44]
# li.sort()

# s = '1111'
# s.replace()


#  关于方法的调用：
# 实例方法：只能通过对象去调用
# Cat.skill2()
# 类方法：可以通过类和对象去调用
# Cat.func()
# kitty.func()
# 静态方法：可以通过类和对象去调用
# Cat.func2()
# kitty.func2()


# 属性的访问：
# 类属性：可以通过类和对象去访问
# 对象（实例）属性：只有对象自己能用
