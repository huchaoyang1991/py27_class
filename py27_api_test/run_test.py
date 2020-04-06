import unittest

from BeautifulReport import BeautifulReport

from py27_api_test.testcases.test_loans import LoansTestCase
from py27_api_test.testcases.test_undate import UpdateTestCase
from py27_api_test.testcases.test_user import UserTestCase
from py27_api_test.utils.my_path import REPORT_DIR, CASE_DIR

suite = unittest.defaultTestLoader.discover(CASE_DIR)
# suite = unittest.defaultTestLoader.loadTestsFromTestCase(UserTestCase)
br = BeautifulReport(suite)
br.report(description="柠檬班接口测试报告", filename="report.html", report_dir=REPORT_DIR)
