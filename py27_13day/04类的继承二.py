"""
============================
Author:柠檬班-木森
Time:2020/3/3   20:31
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
object:python中所有类的基类(祖宗类)


关于继承：
子类通过继承父类，能够获取父类中定义的所有属性和方法（私有属性除外）

注意：父类不能使用子类的属性和方法。




"""


# -------------------------------使用继承实现的需求代码-----------------------------
# 需求一：V1：大哥大
class PhoneV1(object):
    def phone(self):
        print("打电话的功能")


# 需求二：V2:功能机
class PhoneV2(PhoneV1):

    def music(self):
        print("听音乐的功能")

    def send_msg(self):
        print("发送信息的功能")


class PhoneV3(PhoneV2):

    def pay(self):
        print("支付功能")

    def game(self):
        print("玩游戏的功能")


#
v1 = PhoneV1()
v2 = PhoneV2()
v3 = PhoneV3()

# v1对应的类，
# v1.phone()

# v2对应的类
# v2.phone()
# v2.music()
# v2.send_msg()

# v3对应的类
# v3.phone()
# v3.music()
# v3.send_msg()
# v3.pay()
# v3.game()