"""
============================
Author:柠檬班-木森
Time:2020/3/3   20:24
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


# python3中下面两种类定义没有区别。


# 方式一：不写继承的父类，默认继承object
class MyTest:
    pass


# 方式二：在类名的括号后面指定继承object这个类。
class MyClass(object):
    pass

#  python2中，方式一：的定义形式叫经典类，方式二：的定义形式叫新式类。
