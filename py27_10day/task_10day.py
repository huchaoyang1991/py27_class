# 1、实现一个文件复制器函数，通过给函数传入一个路径，复制该路径下面所有的文件(目录不用复制)到当前目录，

#  提示：os模块结合文件读写操作 、即可实现
# 步骤提示：获取指定路径下的所有文件信息，判断是否是文件，是文件则进行复制（读取内容，写入到新文件）
import os


def copy_file(path):
    files = os.listdir(path)  # 获取当前文件目录下的所有文件
    print(files)
    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            # 读取文件内容
            with open(file=os.path.join(path, file), mode='r', encoding='utf-8') as f:
                f1 = f.read()
            # 追加读取到文件内容到一个新文件
            with open(file=os.path.join(path, 'add_files'), mode='a', encoding='utf-8') as f2:
                f2.write(f1)


path = os.path.dirname(__file__)  # 获取当前文件目录的绝对路径
copy_file(path)
# 第二题：当前有一个case.txt文件，里面中存储了很多用例数据: 如下，每一行数据就是一条用例数据，

# # 文件中数据（可以先直接复制到文件中）
# url:www.baidu.com,mobilephone:13760246701,pwd:123456
# url:www.baidu.com,mobilephone:15678934551,pwd:234555
# url:www.baidu.com,mobilephone:15678934551,pwd:234555
# url:www.baidu.com,mobilephone:15678934551,pwd:234555
# url:www.baidu.com,mobilephone:15678934551,pwd:234555
# # 要求： 请把这些数据读取出来，转换为列表的格式：如下
# [{'url': 'www.baidu.com', 'mobilephone': '13760246701', 'pwd': '123456'}, {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
# {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'}]
# ​
# # 提示：可以分析读取出来的每一行字符串中的内容，然后使用的字符串分割方法进行分割，想办法组装成字典。
# ​
# # 注意点：数据中如果有换行符'\n'，要想办法去掉
path = os.path.dirname(__file__)  # 获取当前文件的目录
test_case = []  # 定义一个测试用例列表

with open(file=os.path.join(path, 'case.txt')) as f:
    list_line = f.readlines()  # 以列表的格式接收文件的内容
list_key = []  # 接收字典key
list_value = []  # 接收字典value
for list in list_line:
    cases_list = list.strip("\n").split(',')  # 将接收的文件内容去空格，并分割
    # print(cases_list)
    for case_list in cases_list:
        case_list = case_list.split(':')  # 将key和value分割
        list_key.append(case_list[0])  # 接收key
        list_value.append(case_list[1])  # 接收value
    test_case.append(dict(zip(list_key, list_value)))  # 通过zip打包为字典并添加到列表
print(test_case)

# 3、第三题：练习模块导入的方式（不用提交）
#
#

# 5、编程逻辑扩展练习题(不用提交)
#
# 1、有一个猴子，第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半  在加一个。到第10天早上想再吃时，见只剩下一个桃子了。
# 请通过一段通过代码来计算   第一天摘了多少个桃子？

# 搞不定了，头疼。。。理解不了。。。。


# 2、 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？
total = 0  # 落地的总距离
high = 100  # 弹起的高度
for i in range(10):
    total += high  # 计算每次从开始到落地的距离
    high = high / 2
    if i != 9:  # 计算每次从地上弹起的距离，因为最后一次落地无需计算弹起的距离，故去掉最后一次的数据
        total += high
    else:
        print(high)  # 最后一次弹起的距离

print(total, high)
