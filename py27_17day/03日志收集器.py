"""
============================
Author:柠檬班-木森
Time:2020/3/12   20:26
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
loging模块默认的日志收集器(root)：收集的等级是warning以上的等级




"""



import logging


# 创建一个日志收集器（如果不传参数name,会返回默认的日志收集器root）
mylog = logging.getLogger()

# 设置日志收集器收集的等级
mylog.setLevel("ERROR")



logging.debug("这是一条debug级别的日志")
logging.info("这是一条info级别的日志")
logging.warning("这是一条warning级别的日志")
logging.error("这是一条error级别的日志")
logging.critical("这是一条critical级别的日志")


