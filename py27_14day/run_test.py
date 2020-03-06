"""
============================
Author:柠檬班-木森
Time:2020/3/5   21:11
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
from py27_14day.tstcases import LoginTestCase



# 第一步：创建测试套件
suite = unittest.TestSuite()


# 第二步：加载测试用例到测试套件
# 第一种：通过测试用例类去加载
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(LoginTestCase))


# 第三步：执行测试套件中的用例

# 创建测试运行程序
# runner = unittest.TextTestRunner()
# runner.run(suite)


# 使用BeautifulReport来执行测试套件中的用例，并生成报告
# from BeautifulReport import BeautifulReport
# br = BeautifulReport(suite)
# br.report("27期第一份测试报告","brreport.html",report_dir=r"C:\project\py27_class\py27_01day")


# 使用 HTMLTestRunner来生成测试报告
# from HTMLTestRunnerNew import HTMLTestRunner
#
# runner = HTMLTestRunner(stream=open("new_report.html","wb"),
#                         title="27期第一份测试报告",
#                         tester="木森",
#                         description="第一个版本的测试"
#                         )
# runner.run(suite)