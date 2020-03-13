"""
============================
Author:柠檬班-木森
Time:2020/3/12   20:26
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
日志输出渠道：

1、输出到控制台


2、输出到文件




"""



import logging


# 创建一个日志收集器（如果不传参数name,会返回默认的日志收集器root）
mylog = logging.getLogger()

# 设置日志收集器收集的等级
mylog.setLevel("DEBUG")


# 设置日志输出的等级
# 创建一个输出到控制台的输出渠道
sh = logging.StreamHandler()
# 设置输出渠道的输出等级
sh.setLevel("ERROR")
# 将输出渠道和日志收集器绑定
mylog.addHandler(sh)


# 创建一个输出到文件的输出渠道
fh = logging.FileHandler("all.log",encoding="utf8")
fh.setLevel("DEBUG")
mylog.addHandler(fh)



logging.debug("这是一条debug级别的日志")
logging.info("这是一条info级别的日志")
logging.warning("这是一条warning级别的日志")
logging.error("这是一条error级别的日志")
logging.critical("这是一条critical级别的日志")


