import logging
import os

from py27_api_test.utils.my_config import conf
from py27_api_test.utils.my_path import LOG_DIR

log_path = os.path.join(LOG_DIR, conf.get("log", "filename"))


class MyLogging:
    @staticmethod
    def create_logger():
        # 创建日志收集器
        log = logging.getLogger()
        log.setLevel(conf.get("log", "level"))
        # 设置控制台日志
        sh = logging.StreamHandler()
        sh.setLevel(conf.get("log", "sh_level"))
        log.addHandler(sh)
        # 设置文件日志
        fh = logging.FileHandler(log_path, encoding="utf-8")
        fh.setLevel(conf.get("log", "fh_level"))
        log.addHandler(fh)
        # 设置日志格式
        form = logging.Formatter(conf.get("log", "formats"))
        sh.setFormatter(form)
        fh.setFormatter(form)
        return log


log = MyLogging.create_logger()
