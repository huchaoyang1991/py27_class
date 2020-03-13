"""
============================
Author:柠檬班-木森
Time:2020/3/7   10:17
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
from py27_16day.demo2.register import register
from py27_16day.demo2.myddt import ddt, data
from py27_16day.demo2.handle_excel import HandleExcel


@ddt
class RegisterTestCase(unittest.TestCase):
    excel = HandleExcel("cases.xlsx", "register")
    cases = excel.read_data()

    @data(*cases)
    def test_register(self, case):
        # 1、准备用例参数
        expected = eval(case["expected"])
        data = eval(case["data"])
        row = case["case_id"] + 1
        # 2：调用被测试的功能函数，传入参数，获取实际结果：
        # print(data,type(data))
        res = register(*data)
        try:
            # 3：断言（比对预期结果和实际结果）
            self.assertEqual(expected, res)
        except AssertionError as e:
            # 断言不通过，引发断言异常
            # excel写入结果：未通过
            self.excel.write_data(row=row, column=5, value="未通过")
            # 主动抛出异常
            raise e
        else:
            # 断言通过，执行else
            # excel写入结果：通过
            self.excel.write_data(row=row, column=5, value="通过")





