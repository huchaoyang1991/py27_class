import logging


def ccc_logger():
    # 第一步：创建日志接收器
    logs = logging.getLogger("chris")
    # 第二步：设置收集器收集的等级
    logs.setLevel("DEBUG")
    # 第三步：设置输出渠道以及输出渠道的等级
    fh = logging.FileHandler("mylog.log", encoding="utf-8")
    fh.setLevel("DEBUG")
    logs.addHandler(fh)

    sh = logging.StreamHandler()
    sh.setLevel("WARNING")

    logs.addHandler(sh)

    # 第四步：设置输出格式
    formats = '%(asctime)s -- [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
    form = logging.Formatter(formats)
    fh.setFormatter(form)
    sh.setFormatter(form)

    return logs


logs = ccc_logger()