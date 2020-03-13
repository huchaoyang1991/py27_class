"""
============================
Author:柠檬班-木森
Time:2020/3/12   21:52
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

from py27_17day.handle_logging import log, create_logger

m_log = create_logger()
m_log2 = create_logger()
m_log3 = create_logger()
print(id(m_log), id(m_log2), id(m_log3))

m_log.error("代码错误了")

# log.error("7890")
