import re
from common.handle_config import conf

data = '{"user":#user#,"pwd":#pwd#,"name":"#name#","age":"#python#"}'


def replace_data(data):
    while re.search("#(.*?)#", data):
        res = re.search("#(.*?)#", data)
        # 返回的式一个匹配对象
        print(res)
        # 获取匹配到的数据
        key = res.group()
        print(key)
        # 获取匹配规则中括号里面的内容
        item = res.group(1)
        print(item)
        value = conf.get("musen", item)

        data = data.replace(key, value)
    return data


res = replace_data(data)
print(res)