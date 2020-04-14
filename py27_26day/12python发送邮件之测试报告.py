"""
============================
Author:柠檬班-木森
Time:2020/4/9   20:20
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import smtplib
from email.mime.text import MIMEText

"""
我qq邮箱的账号以及smtp服务的授权码
账号：musen_nmb@qq.com
授权码：algmmzptupjccbab

qq邮箱的smtp服务器地址：smtp.qq.com,端口：465
163邮箱的smtp服务器地址：smtp.163.com，端口：465 （25）

"""

# 第一步：连接smtp服务器，并登录
# 连接到smtp服务器
smtp = smtplib.SMTP_SSL(host="smtp.qq.com", port=465)
# 登录smtp服务器（邮箱账号和授权码进行登录，注意点：不是邮箱的密码）
smtp.login(user="musen_nmb@qq.com", password="algmmzptupjccbab")


# 读取邮件的内容，作为正文发送过去（缺陷：邮件中显示不友好，特别丑）
with open(r"C:\project\py27_class\py27_api_test\reports\report.html","r",encoding="utf8") as f:
    content = f.read()


# 第二步：构造一封邮件
msg = MIMEText(content,_subtype="html",_charset="utf-8")
msg["Subject"] = "上课邮件001"
msg["To"] = "lemonban@qq.com"
msg["From"] = "musen_nmb@qq.com"


# 第三步：发送邮件
smtp.send_message(msg,from_addr="musen_nmb@qq.com",to_addrs=["3247119728@qq.com","1393175994@qq.com"])

