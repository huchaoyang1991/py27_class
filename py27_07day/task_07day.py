# 1、一、输出99乘法表，结果如下：（提示嵌套for循环，参照上课打印三角形的案例）
import random

for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}*{}={}".format(i, j, j * i), end=" ")
    print()

# 2、实现剪刀石头布游戏（），提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4） 电脑随机出拳比较胜负，显示 用户胜、负还是平局。
info = {1: '石头', 2: '剪刀', 3: '布', 4: '退出'}

while 1:
    user_fist = int(input("请出拳：1（石头）2（剪刀）3（布）4（退出）"))
    computer_fist = random.randint(1, 3)

    while user_fist > 4 or user_fist < 1:
        user_fist = int(input("您输入的数字超出范围，请重新出拳：1（石头）2（剪刀）3（布）4（退出）"))

    if user_fist == 4:
        print("游戏结束")
        break
    elif user_fist == computer_fist:
        print("平局")
    elif user_fist == computer_fist - 1 or user_fist == computer_fist + 2:
        print("你赢了")
    else:
        print("你输了")
    print("您出拳：{},电脑出拳：{}".format(info[user_fist], info[computer_fist]))


# 运行如下图所示（提示：while循环加条件判断，做判断时建议先分析胜负的情况）：

# 3、通过定义一个计算器函数，调用函数分别提示用户输入数字1，数字2，然后再提示用户选择 ：   加【1】    减【2】    乘【3】      除【4】，
def calc(num1, num2, algorithm):
    if algorithm == 1:
        result = num1 + num2
    elif algorithm == 2:
        result = num1 - num2
    elif algorithm == 3:
        result = num1 * num2
    elif algorithm == 4:
        result = num1 / num2
    else:
        print("运算符输入有误")
        return
    return result


num1 = int(input("请输入第一个数字:"))
num2 = int(input("请输入第二个数字:"))
algorithm = int(input("请输入运算符:加【1】    减【2】    乘【3】   除【4】"))
result = calc(num1, num2, algorithm)
print("结果为", result)

# 5、扩展练习题：不用提交，不计入评分（有时间的同学可以做）：

#      学习控制流程时，我们讲了一个登录的案例，现在要求大家通过代码实现一个注册的流程，基本要求：
#
# 1、运行程序，提示用户，输入用户名，输入密码，再次确认密码。
# ​
# 2、判读用户名有没有被注册过，如果用户名被注册过了，那么打印结果该用户名已经被注册。
# ​
# 3、用户名没有被注册过，则判断两次输入的密码是否一致，一致的话则注册成功，否则给出对应的提示。
# ​
# 4、下面是已注册的两个账户，注册成功的账号密码按下面的形式保存到列表users中
# users = [{"uaer":"py27","pwd":"lemonban"},{"uaer":"py28","pwd":"lemonban2"}]
# ​
# 提示：要是有for-else语句才能实现
users = [{"uaer": "py27", "pwd": "lemonban"}, {"uaer": "py28", "pwd": "lemonban2"}]
username = input("请输入用户名")
password = input("请输入密码")
confirm = input("请再次确认密码")
for user in users:
    if username == user["uaer"]:
        print("该用户名已经被注册")
        break
else:
    if password == confirm:
        print("注册成功")
        users.append({"uaer": username, "pwd": password})
    else:
        print("俩次密码输入不一致，注册失败")
print(users)
