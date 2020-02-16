"""
============================
Author:柠檬班-木森
Time:2020/2/15   12:15
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""

break:强制跳出循环

continue:中止当前本轮循环，直接进行下一轮循环的条件判断



pass：没有具体的语义，用来占行，执行到改行代码直接通过，执行下一行
"""
#
# n = 0
# while n < 100:
#     n += 1
#     print("这是第{}打印:hello python".format(n))


# 需求：打印完第10遍退出循环
# n = 0
# while n < 100:
#     n += 1
#     print("这是第{}打印:hello python".format(n))
#     # 当n等于10的时候，退出循环
#     if n == 10:
#         break


# 需求：第10遍到第15遍不打印
n = 0
while n < 100:
    n += 1
    # 当n在10到15之间时，执行continue中止本轮循环，直接进行下一轮循环的条件判断
    if 10 <= n <= 15:
        # continue
        pass
    print("这是第{}打印:hello python".format(n))


# 关于pass

# data = {"user": "python27", "pwd": "lemonban"}
# # 第二步：提示用户输入账号，密码
# user = input("请输入账号：")
# pwd = input("请输入密码：")
# # 第三步：判断账号密码是否输入正确
# if user == data["user"]:
#     pass
# else:
#     print("输入的账号不对")

score = float(input("请输入您的成绩:"))
if 0 <= score < 40:
    pass
elif 40 <= score < 60:
    pass
elif 60 <= score < 75:
    pass
elif 75 <= score < 85:
    pass
elif 85 <= score <= 100:
    print("您的成绩等级为：A")
else:
    print("您输入的成绩有误！")

