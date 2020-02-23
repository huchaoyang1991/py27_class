"""
============================
Author:柠檬班-木森
Time:2020/2/21   9:39
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
print("------------------第1题------------------------")

count = 0
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            if a != b and c != b and a != c:
                # print(a, b, c)
                number = int('{}{}{}'.format(a, b, c))
                print(number)
                count += 1
print('一共有{}个'.format(count))



print("------------------第2题------------------------")

count = 0
for a in range(100 // 5 + 1):
    for b in range(100 // 3 + 1):
        c = 100 - a - b
        if a * 5 + b * 3 + c * 0.5 == 100:
            print("a:{},b:{},c:{}".format(a,b,c))
            count += 1
print("一共有{}种买法".format(count))

print("------------------第3题------------------------")


def add_number(*args, **kwargs):
    # 定义一个初始变量为零
    s = 0
    # 遍历参数进行累加
    for n in args:
        s += n
    for n in kwargs.values():
        s += n
    return s


res = add_number(1, 2, 3, a=4, b=5,c=99,d=100)
print("结果为：", res)

# 4、简答题
# 1、直接定义在py文件（模块）中的变量叫做全局变量，全局变量在该模块中任意地方都可以访问
# 2、定义在函数中的变量，叫做局部变量，局部变量只有在该函数内部才能访问
# 3、在函数中定义（或修改）全局变量，需要使用global进行声明
# 4、必备参数、默认参数、不定长参数
