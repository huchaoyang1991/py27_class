"""
============================
Author:柠檬班-木森
Time:2020/2/15   9:52
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
集合:set类型
通过{}来表示
内部的数据{value,value2,value3}

集合的特性
1、集合的数据不能存在重复的元素
2、集合中的数据只能是不可变类型

3、集合和字典都是无序的，没有下标索引
4、集合是可变类型的数据
5、增删查改
    add:添加数据
    pop:删除数据
    交集
    并集
    差集
    
集合的应用：
1、对数据去重

2、用来区分数据是否可变



"""
# set1 = {11, 22, 33, 44, 55}
# # print(type(set1))
# print(set1)
#
# # 集合的数据不能存在重复的元素
#
# set2 = {1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 3, 2, 4, 5, 6}
# print(set2)
#
# # 集合中的数据只能是不可变类型
# set3 = {1, 1.11, 'pthon'}

# 字符串去重
# s = "dfghjkldfghjkdfghjk"
# s1 = set(s)
# s2 = "".join(s1)
# print(s2)

# 列表去重
# li = [1, 1, 1, 2, 3, 4, 5]
# res = list(set(li))
# print(res)


# s6 = {111,99.99,True,"python",(1,2)}
# s7 = {{1,2,3}}
