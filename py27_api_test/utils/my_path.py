import os

# 获取项目所在路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试用例所在路径
CASE_DIR = os.path.join(BASE_DIR, "testcases")
# 用例数据所在目录-excel
DATA_DIR = os.path.join(BASE_DIR, "data")
# 配置文件所在目录
CONF_DIR = os.path.join(BASE_DIR, "config")
# 测试报告所在目录
REPORT_DIR = os.path.join(BASE_DIR, "reports")
# 日志文件所在目录
LOG_DIR = os.path.join(BASE_DIR, "logs")
