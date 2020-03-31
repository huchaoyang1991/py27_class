import os
import unittest

import requests

from py27_api_test.lib.myddt import ddt, data
from py27_api_test.service.common_service import CommonService
from py27_api_test.utils.common_util import common_util
from py27_api_test.utils.my_config import conf

from py27_api_test.utils.my_excel import MyExcel
from py27_api_test.utils.my_log import log
from py27_api_test.utils.my_mysql import MyMysql
from py27_api_test.utils.my_path import DATA_DIR

filename = os.path.join(DATA_DIR, "apicases.xlsx")


@ddt
class AuditTestCase(unittest.TestCase):
    excel = MyExcel(filename, "audit")
    cases = excel.read_data()
    db = MyMysql()

    common = CommonService()  # 声明公共服务类-包含登录
    user_member_id = None  # 普通用户ID
    user_token = None  # 普通用户token
    admin_member_id = None  # 管理员ID
    admin_token = None  # 管理员token
    load_id = None  # 待审核项目ID

    @classmethod
    def setUpClass(cls) -> None:
        # user_id
        cls.user_member_id, cls.user_token = cls.common.login()
        # admin_id
        cls.admin_member_id, cls.admin_token = cls.common.login(conf.get("test_data", "admin_phone"),
                                                                conf.get("test_data", "admin_pwd"))
        print("usesr_token", cls.user_token)
        print("admin_token", cls.admin_token)

    def setUp(self) -> None:
        url = conf.get("env", "url") + "/loan/add"
        headers = eval(conf.get("env", "headers"))
        headers["Authorization"] = self.user_token
        data = {"member_id": self.user_member_id,
                "title": "我还是个宝宝",
                "amount": 2000,
                "loan_rate": 12.0,
                "loan_term": 3,
                "loan_date_type": 1,
                "bidding_days": 5}
        response = requests.post(url=url, json=data, headers=headers)
        res = response.json()
        self.load_id = common_util.get_json_one(res, "$..id")

    @data(*cases)
    def test_audit(self, case):

        url = conf.get("env", "url") + case["url"]
        data = eval(case["data"].replace("#loan_id#", str(self.load_id)))
        headers = eval(conf.get("env", "headers"))
        headers["Authorization"] = self.admin_token
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        response = requests.patch(url=url, json=data, headers=headers)
        res = response.json()
        print("预期结果：", expected)
        print("实际结果：", res)
        # 断言
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
