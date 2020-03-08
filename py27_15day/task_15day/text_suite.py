import unittest
from BeautifulReport import BeautifulReport

suite=unittest.defaultTestLoader.discover(r"D:\Pywork\py27_class\py27_15day\task_15day")

br = BeautifulReport(suite)
br.report("登录成功")
