"""
============================
Author:柠檬班-木森
Time:2020/3/4   15:13
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

# 作业参考答案

"""
1、完成上课手机类继承的代码


2、有一组数据，如下格式：
{'case_id': 1, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},

定义一个如下的类，请通过setattr将上面字典中的键值对，
分别设置为类的属性和属性值，键作为属性名，对应的值作为属性值

"""


# -----------------------------第一题：------------------------------------------------
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


# -----------------------------第二题：------------------------------------------------

datas = {'case_id': 1, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过', 'excepted': '通过'}


class CaseData:
    pass


for key, value in datas.items():
    setattr(CaseData, key, value)

#
# print(CaseData.case_id)
# print(CaseData.method)
# print(CaseData.url)
# print(CaseData.data)