import random

# 1、现在有变量 a = ‘hello’ ,    b = ‘python18’     c = ‘!’  ,通过相关操作转换成字符串：'hello python18 !'（注意点:转换之后单词之间有空格）


s_blank = " "
a = 'hello'
b = 'python18'
c = '!'
print(s_blank.join((a, b, c)))

# 2、使用random模块和字符串拼接的方法，随机生成一个130开头的手机号码（只能使用上课学过的知识去做）。
phone = '130'
for i in range(8):
    num = str(random.randint(0, 9))
    phone += num
# num = random.randint(10000000, 99999999)
# print('130' + str(num))
print(phone)

# 3、有一个如下列表，请编写代码，提示用户输入1-7中的数字，分别代表周一到周日，根据用户输入，打印输出“今天是周X”（要求：使用上课学过的知识点来做）

li = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
index = int(input("请输入1-7："))

if index > 7 or index < 1:
    index = int(input("您输入的数字不在有效范围，请重新输入1-7:"))
week = '今天是{}'.format(li[index - 1])
print(week)

# 4、现有字符串    str1 = "PHP is the best programming language in the world!"
#       要求一：将给定字符串的PHP替换为Python
str1 = "PHP is the best programming language in the world!"
str2 = str1.replace('PHP', 'Python')
print(str2)

#       要求二：替换以后，将字符串以空格为分割点进行分割得到一个列表
print(str2.split(" "))
# 5、切片操作

#     1、通过切片获取s = 'python java php' 中的java
s = 'python java php'
s1 = s.split(' ')
print(s1[1])
#     2、通过切片获取 li = [2,3,1,4,6,2,5,6,7]中的  [2,5,6,7]
li = [2, 3, 1, 4, 6, 2, 5, 6, 7]
print(li[5:9])
