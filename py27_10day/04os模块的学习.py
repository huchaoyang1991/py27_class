"""
============================
Author:柠檬班-木森
Time:2020/2/25   21:27
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import os

"""
# 相对路径表示法
. 代表的是当前目录
.. 代表的是父级所在目录

"""

# 获取当前文件所在目录的绝对路径
# res = os.path.abspath(".")
# print(res)

# 获取当前目录父级目录的绝对路径
# print(os.path.abspath(".."))

# 魔法变量：__file__:代表的是当前文件的文件名

# print(__file__)

# 获取当前文件的绝对路径
# res = os.path.abspath(__file__)


# dirname:获取父级目录的路径
# res1 = os.path.dirname(res)
# print(res1)


# 需求：在当前文件夹下面，根据项目的层级关系来获取项目目录路径？
# res2 = os.path.dirname(res1)
# print(res2)


Basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(Basedir)

# 路径拼接的方法 os.path.join()

# res22 = os.path.join(Basedir,"py27_02day")
# print(res22)

# res33 = '\\'.join([Basedir,"py27_02day"])
# print(res33)


r"""
# win：  C:\Users\MuSen\AppData\LocalLow\Mozilla

# linux: /home/lomen_data/data

"""