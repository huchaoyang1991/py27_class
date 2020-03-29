import requests
from jsonpath import jsonpath

from py27_api_test.utils.my_config import conf
from py27_api_test.utils.my_json import jsonpath_util
from py27_api_test.utils.my_log import log


class CommonService:
    def login(self, username=conf.get("test_data", "phone"), password=conf.get("test_data", "pwd")) -> list:
        """
        登录
        :param username: 用户名
        :param password: 密码
        :return: 用户ID和token
        """
        url = conf.get("env", "url") + "/member/login"
        data = {
            "mobile_phone": username,
            "pwd": password
        }
        headers = eval(conf.get("env", "headers"))
        response = requests.post(url=url, json=data, headers=headers)
        res = response.json()
        log.debug("res={}".format(res))
        member_id = str(jsonpath_util.get_json_one(res, "$..id"))
        token = "Bearer" + " " + jsonpath_util.get_json_one(res, "$..token")
        return member_id, token
