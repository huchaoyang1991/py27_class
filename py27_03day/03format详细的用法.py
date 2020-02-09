name = "Ann"
info = "学费"
money = 500

# 保留指定小数位数
print("今天收到{}，交来{}{:.2f}，开此收据为凭证".format(name, info, money))
# 指定占位符的字符串长度
# 默认左对齐
print("python:{:10}AAAAAAAAAAAAAAAAAAAAAAA".format("123"))
# 左对齐
print("python:{:<10}AAAAAAAAAAAAAAAAAAAAAAA".format("123"))
# 右对齐
print("python:{:>10}AAAAAAAAAAAAAAAAAAAAAAA".format("123"))
# 居中对齐
print("python:{:^10}AAAAAAAAAAAAAAAAAAAAAAA".format("123"))

# 指定内容填充
print("python:{:q^10}AAAAAAAAAAAAAAAAAAAAAAA".format("123"))

# 百分比显示效果
print("百分比为：{:.3%}".format(0.2))
