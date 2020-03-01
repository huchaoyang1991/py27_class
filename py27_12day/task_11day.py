"""
============================
Author:柠檬班-木森
Time:2020/2/28   17:05
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import random


def work1():
    print('---石头剪刀布游戏开始----')
    print('请按下面提示出拳：')
    # 创建一个列表来存储 石头 剪刀 布
    li = ['石头', '剪刀', '布']

    while True:
        print('石头【1】 剪刀【2】 布【3】 结束游戏【4】')
        # 用户输入数字
        try:
            user_num = int(input('请输入你的选项：'))
        except ValueError:
            print('您出拳有误，请按规矩出拳')
        else:
            # 电脑随机生成数字
            r_num = random.randint(1, 3)
            if 1 <= user_num <= 3:
                # 判断用户和电脑是否相等
                if r_num == user_num:
                    print('您的出拳为:{}，电脑出拳:{}，平局'.format(li[user_num - 1], li[r_num - 1]))
                # 判断用户胜利的情况
                elif (user_num - r_num) == -1 or (user_num - r_num) == 2:
                    print('您的出拳为:{}，电脑出拳:{}，您胜利了'.format(li[user_num - 1], li[r_num - 1]))
                else:
                    print('您的出拳为:{}，电脑出拳:{}，您输了'.format(li[user_num - 1], li[r_num - 1]))
            # 用户输入4，游戏结束
            elif user_num == 4:
                print('游戏结束')
                break
            else:
                print('您出拳有误，请按规矩出拳')


# work1()

"""
1、try的作用
    try可以用来监测代码是否出现异常（把有可能出现异常的代码放在try里面）
2、except下面的代码什么时候执行：
    try中的代码出现异常，被except成功的捕获之后执行，会执行except中的代码。
3、else下面的代码什么时候执行:
    try中的代码没有出现异常，执行else中的代码
4、finally下面的代码什么时候执行:
    不管try中的代码是否发生异常，finally下面的代码都会执行
"""

"""

3、用户输入一个数值，打印1到这个数值之间所有的偶数、及其偶数个数、及其它们的平均值
（如果输入非数值，请让用户重新输入）
"""


def work3():
    numbers = []
    count = 0
    while True:
        try:
            num = int(input("请输入一个数字："))
        except ValueError as e:
            print("您的输入有误")
        else:
            for i in range(1, num):
                if i % 2 == 0:
                    numbers.append(i)
                    count += 1
            break
    print("所有的偶数数为：", numbers)
    print("偶数的个数为：", count)
    print("平均值为：", sum(numbers) / count)


work3()

# 扩展题：
"""
规律分析：
第一个月：1
第二个月：1
第三个月：2    # 第二个月数量+生的一对小兔子
第四个月：3	  # 第三个月数量+生的一对小兔子
第五个月：5  = 3 + 2    # 第四个月数量+生的2对小兔子（最开始的兔子生一对，第三个月的也生了一对）
第六个月：8  = 5 + 3  # 第五个月数量+生的3对小兔子（最开始的，第三个月，第四个月的各生了一对）
第七个月：13 = 8 + 5 # 第六个月数量 +生的5对小兔子（最开始的，第三个月，第四个月，第五个月的两对 各生一对）
# ......以此类推，发现规律：除了第一个月和第二个月，后面每个月的兔子都等于前两个月之和。

# 解决思路：第二个月之后，计算兔子数量，需要知道前两个月的兔子数量，
那么通过for循环去遍历月份，将每个月的兔子数量都保存到一个列表中，
可以通过下标去列表中获取前两个月兔子的数量，然后计算本月的兔子




"""
li = []
for i in range(1, 11):
    if i == 1 or i == 2:
        print("第{}的兔子数量为{}".format(i, 1))
        li.append(1)
    else:
        num = li[i - 2] + li[i - 3]
        li.append(num)
        print("第{}的兔子数量为{}".format(i, num))

# li = []
# for i in range(1, 11):
#     if i == 1 or i == 2:
#         # 第一个月和第二个月的兔子为1对
#         num = 1
#     else:
#         # 当月的兔子数，等于前两个月的和
#         num = li[i - 2] + li[i - 3]
#     li.append(num)
# print('第10个月的兔子为：', li[-1])
