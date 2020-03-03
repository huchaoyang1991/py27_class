# 1、上课的手机类继承代码自己敲一遍进行提交，
class PhoneV1:
    def phone(self):
        print("打电话的功能")


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


v3 = PhoneV3()
v3.phone()
v3.music()
v3.send_msg()
v3.pay()
v3.game()


# 2、有一组数据，如下格式：
# {'case_id': 1, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过', 'excepted': '通过'},


# 定义一个如下的类，请通过setattr将上面字典中的键值对，分别设置为类的属性和属性值，键作为属性名，对应的值作为属性值
class CaseData:
    test_case = {'case_id': 1, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过',
                 'excepted': '通过'}


case = CaseData()
for k, v in case.test_case.items():
    setattr(case, k, v)
    print(getattr(case, k))
