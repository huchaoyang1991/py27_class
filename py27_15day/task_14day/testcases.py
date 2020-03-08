
import unittest

from py27_15day.task_14day.register import register


class RegisterTestCase(unittest.TestCase):

    def test_register(self):
        """正常注册"""
        # 第一步：准备用例的数据
        # 预期结果：
        excepted = {"code": 1, "msg": "注册成功"}
        # 参数：data
        data = ('python1', '123456', '123456')
        # 第二步：调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*data)
        # 第三步：断言（比对预期结果和实际结果）
        self.assertEqual(excepted, res)

    def test_password_dis(self):
        """两次密码不一样"""
        # 预期结果：
        excepted = {"code": 0, "msg": "两次密码不一致"}
        # 参数：data
        data = ('python1', '1234567', '123456')
        # 调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*data)
        self.assertEqual(excepted, res)

    def test_user_register(self):
        """账号已经被注册"""
        # 预期结果：
        excepted = {"code": 0, "msg": "该账户已存在"}
        # 参数：data
        data = ('python18', '1234567', '123456')
        # 调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*data)

        self.assertEqual(excepted, res)

    def test_password_lt6(self):
        """密码长度少于6位"""
        # 预期结果：
        excepted = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 参数：data
        data = ('python1', '12345', '12345')
        # 调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*data)
        self.assertEqual(excepted, res)

    def test_password_gt18(self):
        """密码长度大于18"""
        # 预期结果：
        excepted = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 参数：data
        data = ('python21', '1234561234561234567', '1234561234561234567')
        # 调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*data)
        try:
            self.assertEqual(excepted, res)
        except AssertionError as e:
            print('该用例测试未通过')
            raise e
        else:
            print('该用例测试通过')

    def test_user_lt6(self):
        """账号长度少于6位"""
        # 预期结果：
        excepted = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 参数：data
        data = ('py01', '1234567', '1234567')
        # 调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*data)
        self.assertEqual(excepted, res)

    def test_user_gt18(self):
        """账号长度大于18"""
        # 预期结果：
        excepted = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 参数：data
        data = ('python1234561234567', '1234567', '1234567')
        # 调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*data)
        self.assertEqual(excepted, res)

    def test_user_is_none(self):
        """账号为空"""
        # 预期结果：
        excepted = {'code': 0, 'msg': '所有参数不能为空'}
        # 参数：data
        data = (None, '1234567', '1234567')
        # 调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*data)
        self.assertEqual(excepted, res)

    def test_password_is_none(self):
        """密码为空"""
        # 预期结果：
        excepted = {'code': 0, 'msg': '所有参数不能为空'}
        # 参数：data
        data = ('python678', None, None)
        # 调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*data)
        self.assertEqual(excepted, res)
