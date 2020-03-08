"""
============================
Author:柠檬班-木森
Time:2020/3/7   10:28
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
from BeautifulReport import BeautifulReport

# 创建用例，加载套件
suite = unittest.defaultTestLoader.discover(r"C:\project\py27_class\py27_15day\demo2")

# 执行用例，生成报告
br = BeautifulReport(suite)
br.report("demo2报告","report.html")