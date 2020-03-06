"""
============================
Author:柠檬班-木森
Time:2020/3/5   20:22
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
from py27_14day.login import login_check

"""
# 定义测试用例类:用例类必须继承于unittest.TestCase
# 定义测试用例：在测试用例类中，每一个以test开头的方法就是一条用例


unittest中测试用例执行的顺序：根据方法名按ASCII码进行排序的。


unittest中会自动根据用例方法执行的时候，是否出现断言异常，来评判用例执行是否通过。

"""


class LoginTestCase(unittest.TestCase):

    def test_login_pass(self):
        # 第一步：准备用例数据
        # 参数准备
        data = {"username": "python27", "password": "lemonban"}
        # data = ["python27", "lemonban"]
        # user = "python27"
        # pwd = "lemonban"
        # 预期结果准备
        expected = {"code": 0, "msg": "登录成功"}

        # 第二步：获取实际结果（调用功能函数，传入参数，获取实际结果）
        res = login_check(**data)

        # 第三步：断言（比对预期结果和实际结果）
        # assert expected == res
        self.assertEqual(expected, res)

    def test_login_user_error(self):
        # 第一步：准备用例数据
        # 参数准备
        data = {"username": "python8888", "password": "lemonban"}
        expected = {"code": 1, "msg": "账号或密码不正确"}
        # 第二步：获取实际结果（调用功能函数，传入参数，获取实际结果）
        res = login_check(**data)
        # 第三步：断言（比对预期结果和实际结果）
        self.assertEqual(expected, res)

    def test_login_pwd_error(self):
        # 第一步：准备用例数据
        # 参数准备
        data = {"username": "python27", "password": "l1111111"}
        expected = {"code": 1, "msg": "账号或密码不正确"}
        # 第二步：获取实际结果（调用功能函数，传入参数，获取实际结果）
        res = login_check(**data)
        # 第三步：断言（比对预期结果和实际结果）
        self.assertEqual(expected, res)

    def test_login_pwd_is_none(self):
        # 第一步：准备用例数据
        data = {"username": "python27"}
        expected = {"code": 1, "msg": "所有的参数不能为空"}
        # 第二步：获取实际结果（调用功能函数，传入参数，获取实际结果）
        res = login_check(**data)
        # 第三步：断言（比对预期结果和实际结果）
        self.assertEqual(expected, res)

    def test_login_user_is_none(self):
        # 第一步：准备用例数据
        data = {"password": "l1111111"}
        expected = {"code": 1, "msg": "所有的参数不能为空"}
        # 第二步：获取实际结果（调用功能函数，传入参数，获取实际结果）
        res = login_check(**data)
        # 第三步：断言（比对预期结果和实际结果）
        self.assertEqual(expected, res)


if __name__ == '__main__':
    unittest.main()
