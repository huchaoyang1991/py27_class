from jsonpath import jsonpath


class MyJson:
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


jsonpath_util = MyJson()
