import os
import unittest

import requests

from py27_api_test.lib.myddt import ddt, data
from py27_api_test.service.common_service import CommonService
from py27_api_test.utils.my_config import conf
from py27_api_test.utils.my_excel import MyExcel
from py27_api_test.utils.my_log import log
from py27_api_test.utils.my_mysql import MyMysql
from py27_api_test.utils.my_path import DATA_DIR
from py27_api_test.utils.my_replace_data import replace_data

filename = os.path.join(DATA_DIR, "apicases.xlsx")


@ddt
class UpdateTestCase(unittest.TestCase):
    excel = MyExcel(filename, "update")
    cases = excel.read_data()
    db = MyMysql()
    # 声明公共服务类-包含登录
    common = CommonService()

    @classmethod
    def setUpClass(cls):
        cls.member_id, cls.token = cls.common.login()

    @data(*cases)
    def test_update(self, case):
        url = conf.get("env", "url") + case["url"]
        print(url)
        # data = eval(replace_data(case["data"]))
        data = eval(case["data"].replace("#member_id#", self.member_id))
        headers = eval(conf.get("env", "headers"))
        headers["Authorization"] = self.token
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        if case["check_sql"]:
            sql = case["check_sql"].replace("#member_id#", self.member_id)
            # reg_name = self.db.find_one(sql)
            # log.debug("修改之前的name：{}".format(reg_name))
        # 发送接口请求
        response = requests.patch(url=url, json=data, headers=headers)
        res = response.json()
        print("预期结果：", expected)
        print("实际结果：", res)
        # 获取充值后的金额
        # 第三步：断言预期结果和实际结果
        try:
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected["msg"], res["msg"])
            # 判断是否需要进行sql校验
            if case["check_sql"]:
                sql = case["check_sql"].replace("#member_id#", self.member_id)
                reg_name = self.db.find_one(sql)
                self.assertEqual(data["reg_name"], reg_name["reg_name"])
        except AssertionError as e:
            # 结果回写excel中
            log.error("用例--{}--执行未通过".format(case["title"]))
            log.debug("预期结果：{}".format(expected))
            log.debug("实际结果：{}".format(res))
            log.exception(e)
            self.excel.write_data(row=row, column=8, value="未通过")
            raise e
        else:
            # 结果回写excel中
            log.info("用例--{}--执行通过".format(case["title"]))
            self.excel.write_data(row=row, column=8, value="通过")
