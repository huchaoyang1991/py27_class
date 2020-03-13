
import unittest
from py27_16day.task_15day.login import login_check
from py27_16day.task_15day.myddt import ddt, data


@ddt
class LoginTestCase(unittest.TestCase):
    cases = [
        {"title": "登录成功", "excepted": {"code": 0, "msg": "登录成功"}, "data": ['python27', 'lemonban']},
        {"title": "密码错误", "excepted": {"code": 1, "msg": "账号或密码不正确"}, "data": ['python27', 'asdasa67']},

    ]

    @data(*cases)
    def test_login(self, case):

        # 1、准备用例参数
        expected = case["excepted"]
        data = case["data"]
        # 2：调用被测试的功能函数，传入参数，获取实际结果：
        res = login_check(*data)
        # 3：断言（比对预期结果和实际结果）
        self.assertEqual(expected, res)


