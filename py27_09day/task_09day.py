# 内置函数&文件操作
# 截至：02月25日  23:59 展示词云
# # 第一题：现有数据如下
import random

users_title = ["name", "age", "gender"]
users_info = [['小明', 18, '男'], ["小李", 19, '男'], ["小美", 17, '女']]

# # 要求：请封装一个函数，上述两个列表作为参数传入，返回值为如下数据（提示:需要用到zip和for循环）
# users = [{'name': '小明', 'age': 18, 'gender': '男'},
#          {'name': '小李', 'age': 19, 'gender': '男'},
#          {'name': '小美', 'age': 17, 'gender': '女'}]
users = []
for user_in in users_info:
    users.append(dict(zip(users_title, user_in)))
print(users)

# 第二题：请封装一个函数，按要求实现数据的格式转换
# 传入参数： data = ["{'a':11,'b':2}", "[11,22,33,44]"]
# 返回结果：res = [{'a': 11, 'b': 2}, [11, 22, 33, 44]]
# 通过代码将传入参数转换为返回结果所需数据，然后返回
data = ["{'a':11,'b':2}", "[11,22,33,44]"]
res = []
for i in data:
    res.append(eval(i))

print(res)
# 第三题：当前有一个data.txt文件，内容如下：
# 数据aaa
# 数据bbb
# 数据ccc
# 数据ddd
# # 要求：请将数据读取出来，保存为以下格式
# {'data0': '数据aaa', 'data1': '数据bbb', 'data2': '数据ccc', 'data3': '数据ddd'}
#
# # 提示思路：
# #1、按行读取数据，2、构造字典的键，  3、打包为字典
# ​
# # 注意点：读取出来的数据有换行符'\n'，要想办法去掉
nums = ['data0', 'data1', 'data2', 'data3']
li = []
with open(file="data.txt", encoding='utf-8') as f:
    for i in f.readlines():
        li.append(i.replace('\n', ''))
    print(dict(zip(nums, li)))

# 4、继续扩展石头剪刀布的游戏，想办法把每次游戏结果都写入到txt文件中保存，文件中写入内容格式如下：

info = {1: '石头', 2: '剪刀', 3: '布', 4: '退出'}
result = ''
while 1:
    user_fist = int(input("请出拳：1（石头）2（剪刀）3（布）4（退出）"))
    computer_fist = random.randint(1, 3)

    while user_fist > 4 or user_fist < 1:
        user_fist = int(input("您输入的数字超出范围，请重新出拳：1（石头）2（剪刀）3（布）4（退出）"))

    if user_fist == 4:
        print("游戏结束")
        break
    elif user_fist == computer_fist:
        result_info='平局'
    elif user_fist == computer_fist - 1 or user_fist == computer_fist + 2:
        result_info="您赢了"
    else:
        result_info="您输了"
    result = "您出拳：{},电脑出拳：{},{}".format(info[user_fist], info[computer_fist],result_info)
    print(result)
    with open(file='game.txt', mode='a', encoding='utf-8') as f:
        f.write(result + '\n')
