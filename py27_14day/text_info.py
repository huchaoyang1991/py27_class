"""
============================
Author:柠檬班-木森
Time:2020/3/5   20:13
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


def login_check(username=None, password=None):
    """
    登录校验的函数
    :param username: 账号
    :param password:  密码
    :return: dict type
    """
    if username != None and password != None:
        if username == 'python27' and password == 'lemonban':
            return {"code": 0, "msg": "登录成功"}
        else:
            return {"code": 1, "msg": "账号或密码不正确"}
    else:
        return {"code": 1, "msg": "所有的参数不能为空"}


"""
1、账号密码正确 
入参：账号python27  密码lemonban     
预期结果：{"code": 0, "msg": "登录成功"}
实际结果：

2、账号正确，密码错误   
入参：账号python27  密码lemonban11     
预期结果：{"code": 1, "msg": "账号或密码不正确"}
实际结果：

3、账号错误，密码正确，
入参：账号python25  密码lemonban     
预期结果：{"code": 1, "msg": "账号或密码不正确"}
实际结果：

4、账号为空
入参：账号为空  密码lemonban11     
预期结果：{"code": 1, "msg": "所有的参数不能为空"}
实际结果：

5、密码为空、
入参：账号Python6  密码为空    
预期结果：{"code": 1, "msg": "所有的参数不能为空"}
实际结果

"""

# 第一条用例
# 预期结果
expected = {"code": 0, "msg": "登录成功"}
# 调用功能函数，传入参数，获取实际结果
resullt = login_check("python27", "lemonban")

if expected == resullt:
    print("用例通过")
else:
    print("用例执行未通过")
