import unittest

from ddt import ddt, data

from py27_15day.demo1.register import register
from py27_15day.task_15day.login_check import login_check


@ddt
class LoginTestCase(unittest.TestCase):
    # {"code": 0, "msg": "登录成功"}
    # {"code": 1, "msg": "账号或密码不正确"}
    # {"code": 1, "msg": "所有的参数不能为空"}
    cases = [
        {"expected": {"code": 0, "msg": "登录成功"}, "data": ['python27', 'lemonban']},
        {"expected": {"code": 1, "msg": "账号或密码不正确"}, "data": ['python12', 'lemonban']},
        {"expected": {"code": 1, "msg": "账号或密码不正确"}, "data": ['python27', '123456']},
        {"expected": {"code": 1, "msg": "所有的参数不能为空"}, "data": [None, 'lemonban']},
        {"expected": {"code": 1, "msg": "所有的参数不能为空"}, "data": ['python27', None]}
    ]

    @data(*cases)
    def test(self, case):
        #   1.准备用例数据
        data = case["data"]
        expected = case["expected"]
        #   2.调用被测方法
        result = login_check(*data)
        #   3.断言
        self.assertEqual(expected, result)
