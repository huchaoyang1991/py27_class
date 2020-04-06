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
class UserTestCase(unittest.TestCase):
    excel = MyExcel(filename, "user")
    cases = excel.read_data()
    db = MyMysql()
    # 声明公共服务类-包含登录
    common = CommonService()

    @classmethod
    def setUpClass(cls) -> None:
        # user_id
        cls.user_member_id, cls.user_token = cls.common.login()
        # admin_id
        cls.admin_member_id, cls.admin_token = cls.common.login(conf.get("test_data", "admin_phone"),
                                                                conf.get("test_data", "admin_pwd"))

    @data(*cases)
    def test_get_user(self, case):
        url = conf.get("env", "url") + case["url"]
        if case["case_id"] == 1:
            url = url.replace("#member_id#", self.user_member_id)
        elif case["case_id"] == 2:
            url = url.replace("#member_id#", self.admin_member_id)
        else:
            url = url.replace("#member_id#", self.admin_member_id)

        headers = eval(conf.get("env", "headers"))
        if case["case_id"] == 1:
            headers["Authorization"] = self.user_token
        elif case["case_id"] == 2:
            headers["Authorization"] = self.admin_token
        else:
            headers["Authorization"] = self.user_token

        expected = eval(case["expected"])
        row = case["case_id"] + 1

        # 发送接口请求
        response = requests.get(url=url, headers=headers)
        res = response.json()
        print("预期结果：", expected)
        print("实际结果：", res)
        # 获取充值后的金额
        # 第三步：断言预期结果和实际结果
        try:
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected["msg"], res["msg"])

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
