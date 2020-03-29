import random

from jsonpath import jsonpath


class CommonUtil:
    def random_phone(self, phone="155") -> str:
        """
        生成随机手机号码
        :param phone: 手机号码头三位
        :return:
        """
        for i in range(8):
            num = str(random.randint(0, 9))
            phone += num
        return phone

    def get_json_all(self, res, expr) -> list:
        """
        jspnpath解析返回所有数据
        :param res:源数据
        :param expr:jsonpath表达式
        :return:
        """
        return jsonpath(res, expr)

    def get_json_one(self, res, expr) -> str:
        """
        jsonpath解析返回第一个数据
        :param res:源数据
        :param expr:jsonpath表达式
        :return:
        """
        return jsonpath(res, expr)[0]


common_util = CommonUtil()
