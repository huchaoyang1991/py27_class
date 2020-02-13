# 1、 将字符串中的单词位置反转，“hello xiao mi” 转换为 “mi xiao hello”
# （提示：通过字符串分割，拼接，列表反序等知识点来实现）
import random

str = 'hello xiao mi'
li = str.split(' ')
print(li)
li.reverse()
print(li)
s_blank = ' '
str2 = s_blank.join(li)
print(str2)

# # 2、字典的增删查改操作： 某比赛需要获取你的个人信息，编写一段代码要求如下：
# #         1、运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据通过字典存储起来，
# dic = {}
# dic['name'] = input("请输入姓名：")
# dic['sex'] = input("请输入性别：")
# dic['age'] = input("请输入年龄：")
# print(dic)
# #         2、数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
# # info = "我的名字{name},今年{age}岁,性别{sex},喜欢敲代码".format(**dic)
# info = "我的名字{name},今年{age}岁,性别{sex},喜欢敲代码".format_map(dic)
# print(info)
# #         3、有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
# dic['height'] = input("请输入您的身高：")
# dic['phone'] = input("请输入您的联系方式：")
# print(dic)
# #         4、平台为了保护你的隐私，需要你删除你的联系方式；
# dic.pop('phone')
# print(dic)
# #         5、你为了取得更好的成绩， 你添加了一项自己的擅长技能。
# dic['skill'] = input("请输入你的擅长技能：")
# print(dic)
# 3、利用下划线将列表li=[“python”,“java”,“php”]的元素拼接成一个字符串，然后将所有字母转换为大写，
li = ["python", "java", "php"]
s_blank = '_'
str = s_blank.join(li)
print(str.upper())

# 4、利用切片把 'http://www.python.org'中的python字符串取出来
str = 'http://www.python.org'
print(str[11:17])

# 5、编写一个买橘子的计算器：
#     运行代码提示输入橘子的价格（要考虑小数的情况），
#     然后随机生成斤数（1-100之间整数），最后计算应付金额，控制台输出如下信息(所有数据输出时都要保留两位小数)
#        输出内容格式：“您购买的橘子为xx.xx斤，每斤xx.xx元，应支付金额为xx.xx”
price = float(input("请输入橘子的价格："))
num = random.randint(1, 100)
pay = price * num
print("您购买的橘子为{:.2f}斤,每斤{:.2f}元，应支付金额为{:.2f}元".format(num, price, pay))
