"""
============================
Author:柠檬班-木森
Time:2020/3/5   21:38
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import unittest
from BeautifulReport import BeautifulReport



# 第一步：创建测试套件
# suite = unittest.TestSuite()


# 第二步：加载测试用例到测试套件
# 第一种：通过测试用例类去加载
# from py27_14day.testcases import LoginTestCase
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(LoginTestCase))

# 第二种：通过测试用例模块去加载
# 用例加载器对象
# from py27_14day import testcases
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(testcases))

# 第三种：通过路径去加载测试用例  :默认去找指定路径中test开头的模块中的测试用例
# loader = unittest.TestLoader()
# suite.addTest(loader.discover(r"C:\project\py27_class\py27_14day"))


# 第四种：一条一条去加载
# from py27_14day.testcases import LoginTestCase
# case1 = LoginTestCase("test_login_pass")
# suite.addTest(case1)


# 创建套件，加载用例（一行代码的简单写法）

suite = unittest.defaultTestLoader.discover(r"C:\project\py27_class\py27_14day")




# 使用BeautifulReport来执行测试套件中的用例，并生成报告
br = BeautifulReport(suite)
br.report("27期第一份测试报告","brreport.html")

