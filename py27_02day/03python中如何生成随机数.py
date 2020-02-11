"""
============================
Author:柠檬班-木森
Time:2020/2/6   21:14
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
python中内置的随机数模块:random

random.random():随机生成一个浮点数（0-1之间）

random.randint():生成指定范围的整数


"""
import random
# 随机生成一个浮点数（0-1之间）
num = random.random()
# print(num)

# 随机生成指定范围的整数
# n = random.randint(0,100)
# print(n)


# 需求：生成指定范围的浮点数？ 1-100之间
# 解决方法：随机生成的整数+小数

# 注意事项：
# random.random生成的小数范围：左闭右开，包含0不，包含1
# random.randint()随机生成指定范围的整数：包含起始位置和终止位置的值
# print(random.randint(1,3))









