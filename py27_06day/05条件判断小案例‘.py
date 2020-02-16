"""
============================
Author:柠檬班-木森
Time:2020/2/15   11:11
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

# 登录小案例：事先存储一组账号密码，提示用户输入账号，密码，然后判断账号密码是否输入正确

# 第一步：事先存储账号密码
data = {"user": "python27", "pwd": "lemonban"}

# 第二步：提示用户输入账号，密码
user = input("请输入账号：")
pwd = input("请输入密码：")

# 第三步：判断账号密码是否输入正确
if user == data["user"]:
    if pwd == data["pwd"]:
        print("账号密码都正确")
    else:
        print("输入的密码不对")
else:
    print("输入的账号不对")


# 使用逻辑运算符去判断多个条件
# if user == data["user"] and pwd == data["pwd"]:
#     print("账号和密码输入正确，登录成功")
# else:
#     print("账号或密码有误！")



# if：判断条件成立的标准（扩展）
# if成立的标准是根据 if后面的python表达式或者数据的布尔值是否为True来确定条件是否成立

# python中数据布尔值：
# 非0为True: None、数字0或者数据的长度为0(len)的布尔值为False，其他的数据布尔值都是True

# 数据长度为0：例如：空字符串，空列表、空元祖、空字典、


# s = "python"
# s2 = ""
# li = []
#
# if s2:
#     print("成立")
# else:
#     print("不成立")
#



