import os
import unittest

import requests

from py27_api_test.common.handle_excel import HandleExcel
from py27_api_test.lib.myddt import ddt, data
from py27_api_test.utils.my_config import conf
from py27_api_test.utils.my_log import log
from py27_api_test.utils.my_path import DATA_DIR

filename = os.path.join(DATA_DIR, "apicases.xlsx")  # TODO excel路径


@ddt
class LemonTestCase(unittest.TestCase):
    excel_login = HandleExcel(filename, "login")
    cases_login = excel_login.read_data()
    excel_register = HandleExcel(filename, "register")
    cases_register = excel_register.read_data()

    @data(*cases_login)
    def test_login(self, case):
        headers = eval(conf.get("env", "headers"))
        url = case["url"]
        data = eval(case["data"])
        expected = eval(case["expected"])
        row = case["case_id"] + 1

        response = requests.post(url=url, json=data, headers=headers)
        response = response.json()
        print("预期结果:", expected)
        print("实际结果:", response)
        try:
            self.assertEqual(response["code"], expected["code"])
            self.assertEqual(response["msg"], expected["msg"])
        except AssertionError as e:
            log.error("用例-{}-未通过".format(case["title"]))
            log.error("预期结果-{}".format(case["expected"]))
            log.error("实际结果-{}".format(response))
            self.excel_login.write_data(row=row, column=8, value="未通过")
            raise e
        else:
            self.excel_login.write_data(row=row, column=8, value="通过")
            log.info("用例-{}-通过".format(case["title"]))

    @data(*cases_register)
    def test_register(self, case):
        headers = eval(conf.get("env", "headers"))
        url = case["url"]
        data = eval(case["data"])
        expected = eval(case["expected"])
        row = case["case_id"] + 1

        response = requests.post(url=url, json=data, headers=headers)
        response = response.json()
        print("预期结果:", expected)
        print("实际结果:", response)
        try:
            self.assertEqual(response["code"], expected["code"])
            self.assertEqual(response["msg"], expected["msg"])
        except AssertionError as e:
            log.error("用例-{}-未通过".format(case["title"]))
            log.error("预期结果-{}".format(case["expected"]))
            log.error("实际结果-{}".format(response))
            self.excel_register.write_data(row=row, column=8, value="未通过")
            raise e
        else:
            self.excel_register.write_data(row=row, column=8, value="通过")
            log.info("用例-{}-通过".format(case["title"]))
