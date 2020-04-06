import os
import unittest
import random
import requests


from py27_api_test.lib.myddt import ddt, data
from py27_api_test.utils.common_util import common_util
from py27_api_test.utils.my_config import conf
from py27_api_test.utils.my_excel import MyExcel
from py27_api_test.utils.my_log import log
from py27_api_test.utils.my_mysql import db
from py27_api_test.utils.my_path import DATA_DIR

filename = os.path.join(DATA_DIR, "apicases.xlsx")


@ddt
class LemonTestCase(unittest.TestCase):
    excel_login = MyExcel(filename, "login")
    cases_login = excel_login.read_data()
    excel_register = MyExcel(filename, "register")
    cases_register = excel_register.read_data()

    @classmethod
    def random_phone(cls):
        while True:
            phone = common_util.random_phone()
            sql = "SELECT * FROM futureloan.member WHERE mobile_phone={}".format(phone)
            res = db.find_count(sql)
            if res == 0:
                return phone

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
        if "#phone#" in case["data"]:
            phone = self.random_phone()
            case["data"] = case["data"].replace("#phone#", phone)
        data = eval(case["data"])
        log.debug("注册用例更新手机号码的数据={}".format(data))
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        res_count = 0  # sql影响行数，打印日志使用

        response = requests.post(url=url, json=data, headers=headers)
        response = response.json()
        print("预期结果:", expected)
        print("实际结果:", response)
        try:
            self.assertEqual(response["code"], expected["code"])
            self.assertEqual(response["msg"], expected["msg"])
            if case["check_sql"]:
                sql = case["check_sql"].replace("#phone#", data["mobile_phone"])
                res_count = db.find_count(sql)
                self.assertEqual(1, res_count)
        except AssertionError as e:
            log.error("用例-{}-未通过".format(case["title"]))
            log.error("预期结果-{}".format(case["expected"]))
            log.error("实际结果-{}".format(response))
            log.error("sql影响行数={}".format(res_count))
            self.excel_register.write_data(row=row, column=8, value="未通过")
            raise e
        else:
            self.excel_register.write_data(row=row, column=8, value="通过")
            log.info("用例-{}-通过".format(case["title"]))
