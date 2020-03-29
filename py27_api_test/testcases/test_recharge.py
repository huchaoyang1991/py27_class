import decimal
import os
from unittest import TestCase

import requests

from py27_api_test.lib.myddt import ddt, data
from py27_api_test.service.common_service import CommonService
from py27_api_test.utils.my_config import conf
from py27_api_test.utils.my_excel import MyExcel
from py27_api_test.utils.my_log import log
from py27_api_test.utils.my_mysql import MyMysql
from py27_api_test.utils.my_path import DATA_DIR

filename = os.path.join(DATA_DIR, "apicases.xlsx")


@ddt
class RechargeTestCase(TestCase):
    excel = MyExcel(filename, "recharge")
    cases = excel.read_data()
    db = MyMysql()
    # 声明公共服务类-包含登录
    common = CommonService()

    @classmethod
    def setUpClass(cls) -> None:
        cls.member_id, cls.token = cls.common.login()

    @data(*cases)
    def test_recharge(self, case):
        url = conf.get("env", "url") + case["url"]
        case["data"] = case["data"].replace("#member_id#", self.member_id)
        data = eval(case["data"])
        headers = eval(conf.get("env", "headers"))
        headers["Authorization"] = self.token
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        if case["check_sql"]:
            sql = case["check_sql"].format(self.member_id)
            start_money = self.db.find_one(sql)["leave_amount"]
            log.debug("充值之前的金额：{}".format(start_money))
        # 发送接口请求
        response = requests.post(url=url, json=data, headers=headers)
        res = response.json()
        print("预期结果：", expected)
        print("实际结果：", res)
        # 获取充值后的金额
        if case["check_sql"]:
            sql = case["check_sql"].format(self.member_id)
            end_money = self.db.find_one(sql)["leave_amount"]
            log.debug("充值之后的金额：{}".format(end_money))
            # 第三步：断言预期结果和实际结果
            try:
                self.assertEqual(expected["code"], res["code"])
                self.assertEqual(expected["msg"], res["msg"])
                # 判断是否需要进行sql校验
                if case["check_sql"]:
                    # 将充值金额转换为decimal类型（因为数据库中的金额是decimal类型的）
                    recharge_money = decimal.Decimal(str(data["amount"]))
                    self.assertEqual(recharge_money, end_money - start_money)
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
