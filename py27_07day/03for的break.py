"""
============================
Author:柠檬班-木森
Time:2020/2/18   20:54
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

# 需求一：打印1000遍hello python

# for i in range(1,101):
#     print("这是第{}遍:hello python".format(i))


# 需求二：打印到第50遍跳出循环
# for i in range(1, 101):
#     print("这是第{}遍:hello python".format(i))
#     if i == 50:
#         break

# 第30遍到第50遍不打印：
# for i in range(1, 101):
#     if 30 <= i <= 50:
#         continue
#     print("这是第{}遍:hello python".format(i))


# for循环更加高级的语法：for--else:()
# for对应的else只有当循环是break结束的时候，不会执行，其他情况都会执行

# for i in range(10):
#     print("本轮遍历的数据为{}".format(i))
# else:
#     print("for对应的else语句")

# 需求 判断用户输入的账号是否存在？
# users = [{"user": "121"}, {"user": "122"}, {"user": "123"}, {"user": "124"}]
#
# user = input("请输入您的账号：")
#
# for item in users:
#     if user == item["user"]:
#         print("该用户已存在")
#         break
# else:
#     print("用户不存在")


