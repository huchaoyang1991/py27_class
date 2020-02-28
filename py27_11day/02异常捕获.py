"""
============================
Author:柠檬班-木森
Time:2020/2/27   20:56
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
对于有可能会出错的代码，我们可以对这行代码进行异常捕获


try-except:

try-except--else:

try-except--else--finally:


"""

import random

try:
    # 对于有可能会出错的代码，我们可以对这行代码进行异常捕获
    price = float(input("请输入橘子价格："))
except:
    # try里面的代码，出现了异常执行except中的代码
    print("输入价格的代码出错了")
else:
    # try里面的代码没有出现异常的时候执行else的代码
    n = random.randint(1, 100)
    sum_price = price * n
    print("您购买的橘子为{:.2f}斤，每斤{:.2f}元，应支付金额为{:.2f}".format(n, price, sum_price))
finally:
    # 不管try的代码是否出现异常，都会执行
    print("这个是finally中的代码")