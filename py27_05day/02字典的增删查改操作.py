"""
============================
Author:柠檬班-木森
Time:2020/2/13   20:28
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
字典的操作


"""

dic = {"a": 11, "b": 22, "c": 33}

# 添加元素
# dic["d"] = 99
# print(dic)

# update:往字典中添加多个键值对
# dic.update({"aa": 111, "bb": 222, "cc": 33})

# 修改元素
# dic["c"] = 99

# 删除元素
# pop:通过键去删除指定的键值对,返回键对应的值
# res = dic.pop("a")
# print(res)
# popitem:删除最后添加进去的键值对,以元组的形式返回一个键值对
# res = dic.popitem()
# print(res)

# 查找元素
# 通过键进行索引取值
# res = dic["c"]
# print(res)

# get:通过键获取对应的值,键不存在返回None
# res2 = dic.get("python")
# print(res2)


# 其他的方法（）

# 获取字典中所有的键
res3 = dic.keys()
print(list(res3))

# 获取字典中所有的值
res4 = dic.values()
print(list(res4))

# 获取字典中所有的键值对
res5 = dic.items()





# print(dic)