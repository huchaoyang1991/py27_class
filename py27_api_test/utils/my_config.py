import os
from configparser import RawConfigParser

from py27_api_test.utils.my_path import CONF_DIR


class MyCofnig(RawConfigParser):
    def __init__(self, filename):
        super().__init__()
        self.read(filename)


conf = MyCofnig(os.path.join(CONF_DIR, "config.ini"))
