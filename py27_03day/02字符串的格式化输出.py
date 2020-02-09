s1 = "今天收到张三，交来学费500，开此收据为凭证"
#   如何在字符串中预留位置，插入数据
#  input 不管输入什么值，都会转化为字符串类型
# 第一种：format
name = "Ann"
info = "学费"
money = 500
s2 = "今天收到{}，交来{}{}，开此收据为凭证"
ss = s2.format(name, info, money)
print(ss)
#  第二种 传统的%占位符
s3 = "今天收到%s，交来%s%d，开此收据为凭证"
s4 = s3 % ("Ann", "学费", 500)
print(s4)
# F表达式

s5 = F"今天收到{name}，交来{info}{money}，开此收据为凭证"
