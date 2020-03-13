"""
============================
Author:柠檬班-木森
Time:2020/3/12   21:28
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
日志轮转：

第一种：通过时间来轮转




"""

from logging.handlers import TimedRotatingFileHandler,RotatingFileHandler


import logging

# 第一步：创建一个日志收集器
log = logging.getLogger("musen")

# 第二步：设置收集器收集的等级
log.setLevel("DEBUG")


# 第三步：创建输出渠道
# 创建一个按时间进行轮转的文件输出渠道
# fh = TimedRotatingFileHandler("user.log",encoding="utf8",when="S",interval=1,backupCount=7)
# fh.setLevel("DEBUG")
# log.addHandler(fh)

# 按文件大小进行轮转
fh = RotatingFileHandler("musen.log",encoding="utf8",maxBytes=1024*1024*20,backupCount=7)
fh.setLevel("DEBUG")
log.addHandler(fh)


# 第四步：设置输出格式
formats='%(asctime)s -- [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
# 创建一个输出格式对象
form = logging.Formatter(formats)
# 将输出格式添加到输出渠道
fh.setFormatter(form)




log.info("-------------info等级的日志-------------")
log.error("-------------error等级的日志-------------")