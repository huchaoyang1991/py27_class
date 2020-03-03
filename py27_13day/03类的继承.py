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




"""

# -------------------------------不使用继承实现的需求代码-----------------------------
# 需求一：V1：大哥大
class PhoneV1(object):

    def phone(self):
        print("打电话的功能")


# 需求二：V2:功能机
class PhoneV2(object):

    def phone(self):
        print("打电话的功能")

    def music(self):
        print("听音乐的功能")

    def send_msg(self):
        print("发送信息的功能")


class PhoneV3(object):
    def phone(self):
        print("打电话的功能")

    def music(self):
        print("听音乐的功能")

    def send_msg(self):
        print("发送信息的功能")

    def pay(self):
        print("支付功能")

    def game(self):
        print("玩游戏的功能")
