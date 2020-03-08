import unittest

from py27_14day.HTMLTestRunnerNew import HTMLTestRunner
from py27_15day.task_14day import testcases

# 创建测试套件
suite = unittest.TestSuite()

# 添加一个模块中所有的测试用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(testcases))


# 生成html文件的的测试报告
runner = HTMLTestRunner(stream=open('report.html', 'wb'),
                        title='柠檬班测试报告',
                        description='这是我们27期的第一次生成报告的作业',
                        tester='MuSen')

runner.run(suite)
