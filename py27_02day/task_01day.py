#   1、写一段代码，运行的时候在控制台依次提示提示输入姓名，年龄、性别，
import random

name = input("姓名：")
sex = input("性别：")
age = input("年龄：")

print("******************")
print("姓名：", name)
print("性别：", sex)
print("年龄：", age)
print("******************")

# 2、使用随机数模块生成一个5到10之间的浮点数，输出到控制台

f = random.random()
num = random.randint(5, 9)
data = f + num
print(data)

print(random.uniform(5, 9))
# 3、有5个数 a1=100，a2 =300,a3=400，b=180 、c=1000,
a1 = 100
a2 = 300
a3 = 400
b = 180
c = 1000
# 要求一、请使用逻辑运算符和比较运算符去  比较c大于 a1、a2、a3是否全部成立。
result = c > a1 and c > a2 and c > a3
print(result)
# 要求二、请使用逻辑运算符和比较运算符去 比较b大于 a1、a2、a3至少1个成立。
result = b > a1 or b > a2 or b > a3
print(result)

# 4、运算符的应用：

#   1、计算 5的三次方，除以15的余数
a = 5 ** 3
num = a % 15
print(num)
#   2、比较989除以57取余的结果，是否大于17
a = 989 % 57
b = 17
result = a > b
print(result)
