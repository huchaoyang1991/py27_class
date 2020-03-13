"""
============================
Author:柠檬班-木森
Time:2020/3/10   20:10
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
需求：将excel中的用例数据读取出来，保存为以下格式：

[
{"title": "登录成功", "excepted": {"code": 0, "msg": "登录成功"}, "data": ['python27', 'lemonban']},
{"title": "密码错误", "excepted": {"code": 1, "msg": "账号或密码不正确"}, "data": ['python27', 'asdasa67']},
]

"""

import openpyxl

wb = openpyxl.load_workbook("cases.xlsx")
# 选择表单
sh = wb["register"]
# 按行获取所有数据
datas = list(sh.rows)

case_datas =[]


# 获取第一行数据（表头）
# print(datas[0])
title = []
for item in datas[0]:
    title.append(item.value)
print(title)

# 读取第二行
values = []
for item in datas[1]:
    values.append(item.value)
print(values)

case = dict(zip(title, values))
case_datas.append(case)