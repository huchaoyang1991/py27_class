"""
============================
Author:柠檬班-木森
Time:2020/2/25   20:15
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
模块就是python文件

# 1、导入模块
import 模块名
from 包名(文件夹) import 模块名
from 包名(文件夹).包名(文件夹) import 模块名

# 2、导入模块中的 某个变量（函数，类）
from 模块名 import 变量名
from 包名（文件夹）.模块名 import 变量 

# 3、导入的时候起别名
from 模块 import 变量 as 别名
from 包名(文件夹) import 模块名 as 别名

python中的包：
from 包名 import init文件中的变量



keyword、random、os等模块是python官方库，


标识符：python中自己起的名字都叫标识符（变量名，函数名，模块名，包名，类名）
标识符命名规范：只能由数字字母下划线组成，不能使用数字开头



"""

# import work1


# from py27_10day import work1
# print(work1.n)
#
# work1.func1()

# 打印python中的关键字
# import keyword
# print(keyword.kwlist)

# import random
# res= random.random()

#  多层级目录下的模块导入
# from py27_10day.pack01 import work2


# 包中init文件的导入
# from py27_10day.pack02 import aaa
# print(aaa)


# 导入模块中的变量或者函数

# from py27_10day.work1 import n
# print("work中导入的n:",n)

# from py27_10day.pack01.work2 import number
# print("work2下面的number:",number)
#
# from py27_10day.pack02.work3 import n3
# print("work3下面的n3",n3)
#
#
# from keyword import kwlist
# print("keyword中的kwlist",kwlist)
#
# from random import randint,random,uniform
# print(randint(1,100))


# 导入的时候给模块或者变量起别名
from random import randint as rt, random as rm
print(rt(1, 100))

from py27_10day import work1 as wk1
print(wk1.n)


