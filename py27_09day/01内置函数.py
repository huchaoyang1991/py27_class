"""
============================
Author:柠檬班-木森
Time:2020/2/22   9:46
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
获取最小值：min


获取最大值:max


求和：sum

enumerate:获取数据的索引和值


filter(参数1，参数2):
参数1：函数（过滤的规则）
参数2：需要过滤的数据
filter会根据参数一函数的返回值是True还是False来决定改数据要不要过滤？


匿名函数： 
语法：lambda 函数的参数:返回值
应用场景，一般用于非常简单的函数（函数内部只有一行代码），比如：结合过滤器使用（当成别的函数的参数）


eval:能够识别字符串中的有效python表达式


zip:聚合打包


"""
# tu = (11, 222, 33, 44)
# li = [1, 2, 3, 4, 5]
# dic = {"a": 11, "b": 44, "c": 99}
# min
# print(min(tu))
# print(min(li))
# print(min(dic.values()))

# max
# print(max(tu))
# print(max((li)))
# print(max(dic.values()))


# sum
# print(sum(tu))
# print(sum(li))
# print(sum(dic.values()))


# enumerate:获取数据的索引和值
# res = enumerate(tu)
# print(list(res))
#
# res2 = enumerate(li)
# print(list(res2))
#
# res3 = enumerate(dic)
# print(list(res3))

# for i in dic:
#     print(i)

#  过滤器函数

li = [11, 2, 22, 444, 56, 121, 324, 45, 11, 777, 3334, 664]

# 需求：过滤出来大于50的数据？
# for循环实现
# li2 = []
# for i in li:
#     if i > 50:
#         li2.append(i)
#
# print(li2)
# 过滤器实现
# def func(x):
#     return x > 50
#
# res = filter(func, li)
# print(res)
# print(list(res))

#  filter运行的原理
# res3 = []
# for i in li:
#     if func(i):
#         res3.append(i)

# 匿名函数：
# res = lambda x:x>50
# print(res(60))

# 匿名函数 结合过滤器一起使用
# res = filter(lambda x: x > 300, li)
# print(list(res))


#
# li1 = [1, 2, 3, 4]
# li2 = [1, 2, 32, 4, 5, 2, 5, 1, 3, 444, 2, 44, 2, 4, 5, 2, 4, 2]
# res = filter(lambda x: x in li1, li2)
# print(list(res))

# 过滤0-100能够被5正常的数据
# res = filter(lambda x: x % 5 == 0, range(101))
# print(list(res))

# eval:
#  需求：s = "{"a":11,"c":111}",将s对应的数据，转换为字典类型

# s = '{"a":11,"c":111}'
#
# # 错误示范
# # print(s,type(s))
#
# res = eval(s)
# print(res, type(res))

# 需求 s2 = '[11,22,33,44]'，将s2对应的数据，转换为列表
# s2 = '[11,22,33,44]'
# # 错误示范
# # print(list(s2))
# res2 = eval(s2)
# print(res2, type(res2))

# 错误示范： s3 = "musen"
# s3 = "musen"  # s3 = musen
# print(eval(s3))

# 注意点：只去掉一层引号
# s4 = "'abc'"
# res4 = eval(s4)
# print(type(res4))

#  zip函数：
# 将以下两个列表，组合为一个字典，title中的元素作为键，data中的元素作为值
# title = ["name", "age", "gender","info"]
# data = ["木森", 18, "男"]
# for循环实现
# dic = {}
# for i in range(2):
#     key = title[i]
#     value = data[i]
#     dic[key] = value
#
# print(dic)
# zip实现
# res = zip(title, data)
# print(dict(res))


#  zip扩展使用

li1 = [11, 22, 33, 44]
li2 = [1, 2, 3, 4, 5]
li3 = [111, 222, 333, 44, 555]
li4 = [11, 12, 13, 14, 15]

# res = zip(li1, li2)
# print(res)
# print(list(res))
# print(tuple(res))
# print(dict(res))

# 注意点 zip对象只能进行一次强制转换，

# res = zip(li1,li2,li3,li4)

# list1 = list(res)
# print(tuple(list1))
