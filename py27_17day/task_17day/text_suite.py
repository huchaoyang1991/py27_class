import unittest
from BeautifulReport import BeautifulReport

suite=unittest.defaultTestLoader.discover(r"D:\Pywork\py27_class\py27_17day\task_17day")

br = BeautifulReport(suite)
br.report("登录成功")
