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


[
{'case_id': 1, 'title': '注册成功', 'data': "['python1', '123456', '123456']", 'expected': '{"code": 1, "msg": "注册成功"}'},
{'case_id': 2, 'title': '两次密码不一致', 'data': "['python12', '1234567', '123456']", 'expected': '{"code": 0, "msg": "两次密码不一致"}'}, 
{'case_id': 3, 'title': '两次密码不一致', 'data': "['python12', '1234567', '123457']", 'expected': '{"code": 1, "msg": "两次密码不一致"}'}
]


注意点：从excel中读取的数据，除了数值，其他的不管你保存的是什么格式，读取出来都是字符串。

"""

import openpyxl

wb = openpyxl.load_workbook("cases.xlsx")
# 选择表单
sh = wb["register"]
# 按行获取所有数据
datas = list(sh.rows)

# 创建一个空列表，用来存放所有的用例数据
case_datas =[]


# 获取第一行数据（表头），保存到title这个列表中
title = []
for item in datas[0]:
    title.append(item.value)

# 遍历除表头之外的其他行数据
for item in datas[1:]:
    # 没遍历出来一行数据，就创建一个空列表，来存放该行数据
    values = []
    # 遍历改行的格子对象，获取该行的数据值，放入values中
    for i in item:
        values.append(i.value)

    # print(values)
    # 没遍历往一行数据，就拿该行的数据和表头打包转换为字典
    case = dict(zip(title,values))
    # print(case)
    # 将该行用例数据添加到列表case_datas中
    case_datas.append(case)

print(case_datas)



# 读取第二行
# values = []
# for item in datas[1]:
#     values.append(item.value)
# print(values)
#
# case = dict(zip(title, values))
# case_datas.append(case)