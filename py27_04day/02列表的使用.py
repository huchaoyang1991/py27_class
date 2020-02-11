"""
============================
Author:柠檬班-木森
Time:2020/2/11   20:36
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
列表：list类型
列表通过[]来表示
列表中的元素可以是任何的数据类型，元素和元素之间使用逗号隔开。
空列表：li = []
空列表的布尔值为False,其他的布尔值都是True
内置函数len:可以用来查看（字符串，列表，元组，字典，集合）元素的总数

列表的常用方法：
增：
    append：
    insert:
    extend:
删：
    remove:
    pop:
    clear:
查：
   下标取值
   index:
   count: 
改：
   通过下标进行赋值


列表的其他方法：
sort:排序

reverse: 反向

copy:复制




"""

# li = [11, 2, 33]
# li1 = []  # 空列表
# print(bool(li1))

# len函数:获取列表的长度（元素的总数）
# print(len(li1))
# print(len("rt5678odfghjkl"))

# li = [11, 22, 33, 44]
# 添加元素

# append:往列表尾部追加元素
# li.append(111)

# insert:指定位置添加元素
# li.insert(1, "python666")

# extend：一次性添加多个元素(添加在列表尾部)
# li.extend([1, 2, 3])

# li.extend((111, 2222, "a"))

# li.append(["python","java","php"])
# print(li)


# 删除元素
# li = [1, 2, 3, 4, 5, 6, 11, 22, 33, 11, 22, 33]
# # remove:删除指定的元素(找到第一个，进行删除)
# li.remove(11)

# # pop：可以通过下标删除指定的元素（默认删除最后一个）
# # li.pop(6)
#
# # clear:清空列表（删除列表中的所有元素）
# li.clear()
# print(li)

# 查找元素
# li = [1, 2, 3, 4, 5, 6, 11, 22, 33, 11, 22, 33]

# 通过下标取值
# res = li[6]
# print(res)

# index:查找指定元素的下标（找到第一个，就返回下标）
# 参数1：要找的元素值，参数2：查找范围的起始位置，参数3：查找范围的终止位置（左闭又开）
# res = li.index(11, -3, -2)
# print(res)

# count:查找列表中某个元素的个数
# res3 = li.count(1)
# print(res3)

# 修改元素：
# li = [11, 22, 33, 44]
# # 通过下标进行赋值
# li[1] = 999
# print(li)


# 列表的其他方法：
# sort:对列表进行排序（列表中全是数值）
# li = [11, 224, 12, 432, 4, 35, 3, 6, 32, 34, 552, 233]
# 默认从小到大进行排序(升序)
# li.sort()

# 从大到小进行排序（降序）
# li.sort(reverse=True)

# reverse:反向(倒序)
# li.reverse()
# print(li)

# copy:复制
# li = [11, 22, 33]
# 变量赋值 引用的是li中的数据
# li2 = li
#
# print(id(li))
# print(id(li2))
#
# li2.append(111)
#
# print(li)
# print(li2)


# 复制
# li = [11, 22, 33]
# li3 = li.copy()
#
# print(li is li3)
#
# li3.append(111)
#
# print(li)
# print(li3)




