import re

from py27_api_test.utils.my_config import conf

data = '{"user":#user#,"pwd":#pwd#,"name":"#name#","age":"#python#"}'


def replace_data(data):
    while re.search("#(.*?)#", data):
        res = re.search("#(.*?)#", data)
        key = res.group()
        item = res.group(1)
        value = conf.get("chris", item)
        data = data.replace(key, value)
    return data
