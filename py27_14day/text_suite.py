import unittest

from BeautifulReport import BeautifulReport

suite = unittest.defaultTestLoader.discover(r"D:\Pywork\py27_class\py27_14day")

# runner=HTMLTestRunner(stream=open("new_report.html","wb"),title="第一份测试报告")
# runner.run(suite)
br = BeautifulReport(suite)
br.report("27期第一份测试报告", "report.html")
