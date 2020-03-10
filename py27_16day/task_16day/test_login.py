import unittest

from py27_15day.demo1.register import register
from py27_15day.task_15day.login_check import login_check
from py27_16day.demo2.myddt import ddt, data
from py27_16day.task_16day.handle_excel_task import HandleExcelTask


@ddt
class LoginTestCase(unittest.TestCase):
    excel = HandleExcelTask("cases_task.xlsx", "mytest")
    cases = excel.read_data()

    @data(*cases)
    def test(self, case):
        #   1.准备用例数据
        data = eval(case["data"])
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        #   2.调用被测方法
        result = login_check(*data)
        #   3.断言
        try:
            self.assertEqual(expected, result)
        except AssertionError as e:
            self.excel.write_data(row=row, column=5, value="未通过")
            raise e
        else:
            self.excel.write_data(row=row, column=5, value="通过")
