from configparser import ConfigParser


def conf():
    conf = ConfigParser()

    conf.read("aaa.conf", encoding='utf-8')
    # r = conf.sections()
    # a = conf.get("mysql", "a")
    # print(a, type(a))
    # d = conf.options("mysql")
    # print(d)

# common
# conf
# library
# log
# reports
# testcases
# run_test.py
# 框架模型搭建.txt
# HandleLogger
