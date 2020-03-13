"""
============================
Author:柠檬班-木森
Time:2020/3/12   20:55
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import logging

# 第一步：创建一个日志收集器
log = logging.getLogger("musen")

# 第二步：设置收集器收集的等级
log.setLevel("DEBUG")

# 第三步：设置输出渠道以及输出渠道的等级
fh = logging.FileHandler("mylog.log", encoding="utf8")
fh.setLevel("DEBUG")
log.addHandler(fh)


sh = logging.StreamHandler()
sh.setLevel("WARNING")
log.addHandler(sh)


# 第四步：设置输出格式
formats='%(asctime)s -- [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
# 创建一个输出格式对象
form = logging.Formatter(formats)
# 将输出格式添加到输出渠道
fh.setFormatter(form)
sh.setFormatter(form)



# 输出日志
# 注意点：自己创建的的日志收集器收集，要使用收集器取记录，不能直接使用logging去记录
# logging.error("----------------error----------")


log.info("-------------info等级的日志-------------")
log.error("-------------error等级的日志-------------")