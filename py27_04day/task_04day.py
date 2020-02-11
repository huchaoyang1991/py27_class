# 一、现在有一个列表 li2=[1，2，3，4，5]，
#      第一步：请通过三行代码将上面的列表，改成这个样子 li2 = [0，1，2，3，66，5，11，22，33]，
li = [1, 2, 3, 4, 5]
li.insert(0, 0)
li[4] = 66
li.extend([11, 22, 33])
print(li)

#      第二步：对列表进行升序排序 （从小到大）
li.sort()
print(li)

#      第三步：将列表复制一份进行降序排序（从大到小）
li2 = li.copy()
li2.sort(reverse=True)
print(li2)
# 二、定义一个空列表user=[],   分别提示用户输入，姓名，年龄，身高，用户输入完之后，将输入的信息作为添加的列表中保存，然后按照一下格式输出：
#     用户的姓名为：xxx,年龄为：xxx,  身高为：xxx  ,请仔细核对
user = []
user.append(input("请输入姓名："))
user.append(input("请输入年龄："))
user.append(input("请输入身高："))
# user_info = "用户的姓名为:{0},年龄为:{1}，身高为:{2},请仔细核对".format(*user)
user_info = "用户的姓名为:{0[0]},年龄为:{0[1]}，身高为:{0[2]},请仔细核对".format(user)
print(user_info)
# 三、切片练习
#
# 1、现在有一个字符串 s = 'abcdefghijk',
s = 'abcdefghijk'
#     要求一：通过切片获取: defg
print(s[3:7])
#      要求二：通过切片获取：cgk
print(s[2::4])
#     要求三：通过切片获取：jhf
print(s[-2:-7:-2])
# 2、现在有一个列表li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li[2::3])
