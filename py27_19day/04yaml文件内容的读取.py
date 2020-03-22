"""
============================
Author:柠檬班-木森
Time:2020/3/17   21:30
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""

yaml格式文件的操作模块： pyyaml
安装命令： pip install pyyaml


"""

import yaml

with open("lemon.yaml", "r", encoding="utf-8") as f:
    file = yaml.load(f, Loader=yaml.FullLoader)
    print(file)
