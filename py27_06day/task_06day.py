# 一、请获取下面数据中的token，和reg_name
import random

data = {
    "code": 0,
    "msg": "OK",
    "data": {
        "id": 74711,
        "leave_amount": 29600.0,
        "mobile_phone": "13367899876",
        "reg_name": "小柠檬666",
        "reg_time": "2019-12-13 11:12:53.0",
        "type": 0,
        "token_info": {
            "token_type": "Bearer",
            "expires_in": "2019-12-30 22:28:57",
            "token": "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjc0NzExLCJleHAiOjE1Nzc3MTYxMzd9.eNMtnEWr57iJoZRf2IRsGDWm2GKj9LZc1J2SGRprAwOk7EPoJeXSjJwdh0pcVVJygHmsbh1TashWqFv1bvCVZQ"
        }
    },
    "copyright": "Copyright 柠檬班 © 2017-2019 湖南省零檬信息技术有限公司 All Rights Reserved"
}
token = data["data"]["token_info"]["token"]
rege_name = data["data"]["reg_name"]

print(token)
print(rege_name)

# 二、有下面几个数据 ，t1 = ("aa",11)      t2= (''bb'',22)    li1 = [("cc",22)]
# 请通过学过的知识点，进行相关操作变为如下字典: {"aa":11,"cc":22,"bb":22}
t1 = ("aa", 11)
t2 = ('bb', 22)
li1 = [("cc", 22)]
li1.insert(0, t1)
li1.append(t2)
print(dict(li1))
# 三、当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，
#  要求一：去除列表中的重复元素，
#  要求二：去重后删除 77，88，99这三个元素
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
li = list(set(li))
li.remove(77)
li.remove(88)
li.remove(99)
li.sort()
print(li)
# 四、利用random函数生成随机整数（范围1-9），然后用户输入一个数字，来进行比较：
# 如果大于随机数，则打印印大于随机数。
# 如果小于随机数，则打印小于随机数。
# 如果相等随机数，则打印等于随机数。
num = random.randint(1, 9)
num_input = int(input("请输入一个数字:"))
if num_input > num:
    print("您输入的数字大于随机数，随机数为{}".format(num))
elif num_input < num:
    print("您输入的数字小于随机数，随机数为{}".format(num))
else:
    print("您输入的数字等于随机数，随机数为{}".format(num))

# 五、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给打九折，
# 如果购买金额大于100元会给打八折。编写一程序，询问购买价格，再打印出折扣和最终价格。
price = float(input("请输入购买商品的价格:"))
if price < 50:
    print("很遗憾，您购买的商品价格未达到我们的促销金额，最终价格为{:.2f}".format(price))
elif 50 >= price <= 100:
    print("恭喜您符合我们的商场促销，给您打九折优惠,最终价格为{:.2f}".format(price * 0.9))
else:
    print("恭喜您符合我们的商场促销，给您打八折优惠,最终价格为{:.2f}".format(price * 0.8))

# 六、提示用户输入一个数（只考虑整数），判断这个数能同时被3和5整除，
# 能整除打印 :这个数据我喜欢
# 不能整除打印：这个数据不太喜欢
num_input = int(input("请输入一个整数："))
if not num_input % 3 and not num_input % 5:
    print("这个数据我喜欢")
else:
    print("这个数据不太喜欢")
