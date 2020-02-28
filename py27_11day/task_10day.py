"""
============================
Author:柠檬班-木森
Time:2020/2/26   15:35
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import os


def copy_file(path):
    # 第一步：获取目标路径中所有的文件和目录
    file_list = os.listdir(path)
    # 第二步：遍历文件，
    for item in file_list:
        # 获取该文件的路径
        file_path = os.path.join(path, item)

        # 第三步：判断是文件还是目录，是文件的话就进行copy
        if os.path.isfile(file_path):
            # 打开文件，读取内容
            with open(file_path, 'r', encoding='utf8') as f:
                contnet = f.read()

            # 在当前目录创建副本文件，写入内容
            new_file = 'cp' + item
            with open(new_file, 'w', encoding='utf8') as f:
                f.write(contnet)


# copy_file(r"C:\project\py27_class\py27_02day")


# 第二题：

"""
思路分析 
url:www.baidu.com,mobilephone:13760246701,pwd:123456
{'url': 'www.baidu.com', 'mobilephone': '13760246701', 'pwd': '123456'}

"""


# s = "url:www.baidu.com,mobilephone:13760246701,pwd:123456"
#
# res1 = s.split(",")
# # print(res1)
# dic = {}
# for item in res1:
#     res2 = item.split(":")
#     dic[res2[0]] = res2[1]
# print(dic)


def work2():
    # 第一步：读取数据,每一行作为一个元素放到列表中
    with open('cases.txt', 'r') as f:
        datas = f.readlines()
        print(datas)
    # 第二步：将数据转换为列表
    # 创建一个空列表
    cases = []
    # # 遍历出来每一行数据
    for i in datas:
        i = i.replace('\n', '')
        #     # 将该行数据使用split按，进行分割,得到一个列表
        itme = i.split(',')
        # 创建一个空字典，用例存放该行数据
        dic = {}
        # 遍历分割后的列表，
        for j in itme:
            # 将遍历出来的数据，按:分割，得到key,value,然后加入到字典中
            key = j.split(':')[0]
            value = j.split(':')[1]
            dic[key] = value
        # 将该行数据加入到列表中
        cases.append(dic)
    # # 完成转换之后，将转换后的数据 进行返回
    return cases


# data2 = work2()
# print('第二题最终的数据为：', data2)

"""
1、有一个猴子，第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个
第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
以后每天早上都吃了前一天剩下的一半  在加一个。
到第10天早上想再吃时，见只剩下一个桃子了。
请通过一段通过代码来计算   第一天摘了多少个桃子？


10       1

9 (1+1)*2  4
8 (4+1)*2  10
7 (10+1)*2  22
 
   
"""
# 第10天的桃子数
n = 1
for i in range(10):

    if i == 0:
        print("今天是第{}天,桃子数量{}".format((10 - i), n))
    else:
        n = (n + 1) * 2
        print("今天是第{}天,桃子数量{}".format((10 - i), n))



#  逻辑第二题

s = 0
h = 100
for i in range(1,11):
    if i ==1:
        s += h
        print("第{}次落地的距离{}".format(i,s))
    else:
        # 计算上一次返回距离
        h = h / 2
        # 加上反弹的距离
        s += h*2
        print("第{}次落地的距离{}".format(i, s))


