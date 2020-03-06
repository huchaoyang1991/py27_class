import unittest

from py27_14day import login_test


class LoginTestCases(unittest.TestCase):
    def test_login_pass(self):
        # 1.准备测试数据
        # 参数
        data = {"username": "python30", "password1": "123456", "password2": "123456"}
        # 预期结果
        expected = {"code": 1, "msg": "注册成功"}
        # 2.获取实际结果
        res = login_test.register(**data)
        # 3.断言
        self.assertEqual(expected, res)

    def test_login_user_is_none(self):
        # 1.准备测试数据
        # 参数
        data = {"username": None, "password1": "123456", "password2": "123456"}
        # 预期结果
        expected = {"code": 0, "msg": "所有参数不能为空"}
        # 2.获取实际结果
        res = login_test.register(**data)
        # 3.断言
        self.assertEqual(expected, res)

    def test_login_pwd1_is_none(self):
        # 1.准备测试数据
        # 参数
        data = {"username": "python28", "password1": None, "password2": "123456"}
        # 预期结果
        expected = {"code": 0, "msg": "所有参数不能为空"}
        # 2.获取实际结果
        res = login_test.register(**data)
        # 3.断言
        self.assertEqual(expected, res)

    def test_login_pwd2_is_none(self):
        # 1.准备测试数据
        # 参数
        data = {"username": "python28", "password1": "123456", "password2": None}
        # 预期结果
        expected = {"code": 0, "msg": "所有参数不能为空"}
        # 2.获取实际结果
        res = login_test.register(**data)
        # 3.断言
        self.assertEqual(expected, res)

    def test_login_pwd2_error(self):
        # 1.准备测试数据
        # 参数
        data = {"username": "python28", "password1": "123456", "password2": "123457"}
        # 预期结果
        expected = {"code": 0, "msg": "两次密码不一致"}
        # 2.获取实际结果
        res = login_test.register(**data)
        # 3.断言
        self.assertEqual(expected, res)

    def test_login_user_is_exist(self):
        # 1.准备测试数据
        # 参数
        data = {"username": "python26", "password1": "123456", "password2": "123456"}
        # 预期结果
        expected = {"code": 0, "msg": "该账户已存在"}
        # 2.获取实际结果
        res = login_test.register(**data)
        # 3.断言
        self.assertEqual(expected, res)

    def test_login_pwd_error1(self):
        # 1.准备测试数据
        # 参数
        data = {"username": "python28", "password1": "12346", "password2": "12346"}
        # 预期结果
        expected = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 2.获取实际结果
        res = login_test.register(**data)
        # 3.断言
        self.assertEqual(expected, res)

    def test_login_pwd_error2(self):
        # 1.准备测试数据
        # 参数
        data = {"username": "python28", "password1": "1234567890123456789", "password2": "1234567890123456789"}
        # 预期结果
        expected = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 2.获取实际结果
        res = login_test.register(**data)
        # 3.断言
        self.assertEqual(expected, res)

    def test_login_user_error1(self):
        # 1.准备测试数据
        # 参数
        data = {"username": "pyth", "password1": "123456", "password2": "123456"}
        # 预期结果
        expected = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 2.获取实际结果
        res = login_test.register(**data)
        # 3.断言
        self.assertEqual(expected, res)

    def test_login_user_error2(self):
        # 1.准备测试数据
        # 参数
        data = {"username": "python007python007python007", "password1": "123456", "password2": "123456"}
        # 预期结果
        expected = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 2.获取实际结果
        res = login_test.register(**data)
        # 3.断言
        self.assertEqual(expected, res)


if __name__ == '__main__':
    unittest.main()
