"""
============================
Author:柠檬班-木森
Time:2020/3/7   10:17
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
from py27_15day.demo2.register import register
from py27_15day.demo2.myddt import ddt, data


@ddt
class RegisterTestCase(unittest.TestCase):
    cases = [
        {"title": "注册成功", "excepted": {"code": 1, "msg": "注册成功"}, "data": ['python1', '123456', '123456']},
        {"title": "密码不一致", "excepted": {"code": 0, "msg": "两次密码不一致"}, "data": ['python12', '1234567', '123456']},
        {"title": "账户已存在", "excepted": {"code": 0, "msg": "该账户已存在"}, "data": ['python26', '1234567', '123456']}
    ]

    @data(*cases)
    def test_register(self, case):
        # pass
        # print("用例方法中打印的case:", case)

        # 1、准备用例参数
        expected = case["excepted"]
        data = case["data"]
        # 2：调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*data)
        # 3：断言（比对预期结果和实际结果）
        self.assertEqual(expected, res)


print("------------------")
