# count方法，查找字符串中某个字符串的个数
s1 = "12jlksdfsj1lkjjsdDSAakj21lkjsa1lks12"
print(s1.count("1"))
# find：查找字符串中某个字符串出现的第一次的下标
print(s1.find("s"))
print(s1.replace("12", "666"))
print(s1.replace("12", "666", 1))
print(s1.upper())
print(s1.lower())
s2 = "python111java111php"
print(s2.split("111"))
print(type(s2.split("111")))
s3="111".join(['python','java','php'])
s4="111".join(('python','java','php'))
s5=('python','java','php')
print(s3)
print(s4)
print(type(s5))
