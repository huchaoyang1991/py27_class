# 1、优化之前作业的石头剪刀布游戏，用户输入时，如果输入非数字会引发异常，请捕获这个异常，提示用户重新输入。
import random

info = {1: '石头', 2: '剪刀', 3: '布', 4: '退出'}
result = ''
while 1:
    try:
        user_fist = int(input("请出拳：1（石头）2（剪刀）3（布）4（退出）"))
        while user_fist > 4 or user_fist < 1:
            user_fist = int(input("您输入的数字超出范围，请重新出拳：1（石头）2（剪刀）3（布）4（退出）"))
    except ValueError as e:
        print("请输入有效的数字")
        print(e)

    else:
        computer_fist = random.randint(1, 3)
        if user_fist == 4:
            print("游戏结束")
            break
        elif user_fist == computer_fist:
            result_info = '平局'
        elif user_fist == computer_fist - 1 or user_fist == computer_fist + 2:
            result_info = "您赢了"
        else:
            result_info = "您输了"
        result = "您出拳：{},电脑出拳：{},{}".format(info[user_fist], info[computer_fist], result_info)

# 2、写出异常处理语句中try作用是什么，except,else,finally下面的代码分别在什么时候会执行？（简答题）
# try：try中的语句出现异常，程序会捕获异常，且让程序继续往下执行
# except:如果程序捕获了异常，会执行该内容
# else：如果程序没有捕获到异常，则会执行该内容
# finally：不管程序有没有捕获到异常，该内容都会执行

# 3、用户输入一个数值，打印1到这个数值之间所有的偶数、及其偶数个数、及其它们的平均值（如果输入非数值，请让用户重新输入）
import numpy

while 1:
    try:
        nums = int(input("请输入一个正整数,退出请输入 1"))
    except Exception as e:
        print("输入值有误，请重新输入")
        print(e)
    else:
        list = []
        if nums == 1:
            break
        elif nums < 1:
            print("您输入的数字不存在偶数")
        else:
            for i in range(2, nums + 1, 2):
                list.append(i)
            print(list)
            print(len(list))
            print(numpy.mean(list))
