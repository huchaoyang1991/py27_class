"""
============================
Author:柠檬班-木森
Time:2020/2/18   20:11
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
for i in XXX:
	# 循环体
	
	
range(n):默认生成一个 0到n-1的整数序列，对于这个整数序列，
我们可以通过list()函数转化为列表类型的数据。

range（n,m)：默认生成一个n到m-1的整数序列，对于这个整数序列，
我们可以通过list()函数转化为列表类型的数据。

range(n,m,k)：相当于其他函数里面的for循环。n 初始值  m 结束值 ， k 步长，
会生成初始值为n,结束值为m-1,递减或者是递增的整数序列。

"""

# stu = ["木子", "凡人", "范先生", "知足", "余生"]
#
# for i in stu:
#     # 循环体代码
#     print("循环执行的代码一")
#     print("循环执行的代码一")
#     print("本次循环遍历出来的是:{}".format(i))


# 入门小练习：当前有10位同学的成绩，放在一个列表中，请区分成绩的等级
# 要求
# 小于60： 不及格
# 60-79：  及格
# 80-100）：优秀
#
# li = [78, 32, 55, 77, 88, 90, 54, 24, 67, 39]
# for item in li:
#     print("本轮遍历出来的成绩为：{}".format(item))
#     if item < 60:
#         print("成绩{}，不及格".format(item))
#     elif 60 <= item < 80:
#         print("成绩{}，及格".format(item))
#     else:
#         print("成绩{}，优秀".format(item))

# while循环实现 1+2+。。。100
# n = 1
# # 用例保存相加的结果
# s = 0
# while n <= 100:
#     s += n
#     n += 1
# print(s)

# for循环来实现：range
# s = 0
# for i in range(1, 101):
#     s += i
#
# print(s)


# 内置函数range()

# res = list(range(1, 101))
# print(res)
# 1 2 3 4 5 6 7 8 9
# for i in range(1,10,2):
#     print(i)

# 需求 ：生成 一组如下数据5,10 15,20。。。。100
# for i in range(0, 100, 2):
#     print(i)

# print(list(range(0,101,2)))
