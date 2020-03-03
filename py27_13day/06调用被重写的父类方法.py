"""
============================
Author:柠檬班-木森
Time:2020/3/3   20:52
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


# 需求一：V1：大哥大
class PhoneV1(object):
    def phone(self):
        print("打语音电话的功能")


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

    def phone(self):
        print("智能机打视频电话的功能")
        print("。。。。五分钟过去，，，接下来想打语音电话")
        # 如何在这里调用父类里面的phone
        # 方式一：父类名.方法名（self）
        # PhoneV1.phone(self)
        # 方式二：super().方法名（）
        super().phone()

# 需求：

# 在子类中定义和父类同名的方法（重写父类方法）

v3 = PhoneV3()

v3.phone()
