"""
============================
Author:柠檬班-木森
Time:2020/3/21   11:16
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import jsonpath

res = {'code': 0,
       'msg': 'OK',
       'data': {'id': 7800007,
                'leave_amount': 0.0,
                'mobile_phone': '18189098765',
                'reg_name': '小柠檬',
                'reg_time': '2020-03-21 09:49:27.0',
                'type': 1,
                'token_info': {'token_type': 'Bearer',
                               'expires_in': '2020-03-21 11:16:59',
                               'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjc4MDAwMDcsImV4cCI6MTU4NDc2MDYxOX0.-zjbWEbXF9qdfvW1Wn0640HZnv3Xkdrx0nDedRTcsgk_URgU185yA-e2SjQUvVfsjA-FpJSKSOF4jjB-Jyv47A'}},
       'data1': {'id': 7800007,
                 'leave_amount': 0.0,
                 'mobile_phone': '18189098765',
                 'reg_name': '小柠檬',
                 'reg_time': '2020-03-21 09:49:27.0',
                 'type': 1,
                 'token_info': {'token_type': 'Bearer',
                                'expires_in': '2020-03-21 11:16:59',
                                'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjc4MDAwMDcsImV4cCI6MTU4NDc2MDYxOX0.-zjbWEbXF9qdfvW1Wn0640HZnv3Xkdrx0nDedRTcsgk_URgU185yA-e2SjQUvVfsjA-FpJSKSOF4jjB-Jyv47A'}},
       'copyright': 'Copyright 柠檬班 © 2017-2019 湖南省零檬信息技术有限公司 All Rights Reserved'}

#  使用字典的键值对 提取方式去提取
# # 提取用户的id
# member_id = res["data"]["id"]
# print(member_id)
#
# # 提取token值
# token = res["data"]["token_info"]["token"]
# print(token)


# 使用jsonpath来提取
member_id = jsonpath.jsonpath(res, "$.data..id")[0]
print(member_id,type(member_id))

token = jsonpath.jsonpath(res, "$.data1..token")[0]
print(token)

"""
. 代表直接子节点
.. 代表子孙节点（不管层级）

"""