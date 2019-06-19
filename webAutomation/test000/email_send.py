# import smtplib
# from email.mime.text import MIMEText
# from email.utils import formataddr
#
# my_sender='125081306@qq.com'    # 发件人邮箱账号
# my_pass = 'wgwgwg0051'              # 发件人邮箱密码(当时申请smtp给的口令)
# my_user='857779009@qq.com'      # 收件人邮箱账号，我这边发送给自己
# def mail():
#     ret=True
#     try:
#         msg=MIMEText('填写邮件内容','plain','utf-8')
#         msg['From']=formataddr(["发件人昵称",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
#         msg['To']=formataddr(["收件人昵称",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
#         msg['Subject']="邮件主题-测试"                # 邮件的主题，也可以说是标题
#
#         server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
#         server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
#         server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
#         server.quit()# 关闭连接
#     except Exception:# 如果 try 中的语句没有执行，则会执行下面的 ret=False
#         ret=False
#     return ret
#
# ret=mail()
# if ret:
#     print("邮件发送成功")
# else:
#     print("邮件发送失败")


from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

# 发件人地址
from_addr = '125081306@qq.com'#发件人地址@qq.com
# 邮箱密码(此处为开启smpt后给出的授权码，而不是登录面膜)
#开启的方式在qq邮箱，设置-》账户的中间偏下位置（账户安全下一栏中），选择开启
password = 'hbjfwkfmawndbheg'#授权码
# 收件人地址
to_addr = '857770990@qq.com'#收件人地址可以任意
# qq邮箱服务器地址
smtp_server = 'smtp.qq.com'


# 调用parseaddr,将传入的参数
def _format_addr(s):
    name, addr = parseaddr(s)
    # print(name)
    # print(addr)
    # 打印出parseaddr方法返回的值，
    # 由此可以看到将在formataddr中传入的值的具体信息
    # xx爬虫出现异常
    # 发件人 @ qq.com
    # 管理员
    # 收件人 @ qq.com
    # return formataddr((Header(name, 'utf-8').encode(), addr))


# # 设置邮件信息
# # 设置发送的文本内容
# #这里第二个参数为plain，指的是发送的事纯文本
# #若想发送网页信息，那就在第一个参数中传入网页信息，把第二个参数设置成html就可以了
# msg = MIMEText('Python爬虫程序出现异常......', 'plain', 'utf-8')
# # 设置发送人
# msg['From'] = _format_addr('xx爬虫出现异常 <%s> ' % from_addr)
# # 设置接收人
# msg['To'] = _format_addr('管理员 <%s> ' % to_addr)
# # 设置邮件标题
# msg['Subject'] = Header('xx爬虫运行状态', 'UTF-8').encode()
#
# # 发送邮件
# # 25为端口号，这一步为连接qq的smtp服务器
# server = smtplib.SMTP(smtp_server, 25)
# # 调用账号和密码进行登录
# server.login(from_addr, password)
# # 开始发送email（发送人，接收人，发送的内容）
# server.sendmail(from_addr, [to_addr], msg.as_string())
# # 退出
# server.quit()
#————————————————————————————————————————————————————

import email.mime.multipart
import email.mime.text
import smtplib


# 接受：收件人，主题，内容
# 返回：邮件发送结果
def send_mail(self, to_mail, to_title, to_content):
    self.to_mail = to_mail  # 收件人邮箱，可以使列表
    self.title = to_title  # 邮件标题
    self.content = to_content  # 邮件内容


    ret = True
    FROM_MAIL = "125081306@qq.com"  # 发件人
    TO_MAIL = self.to_mail  # 收件人

    SMTP_SERVER = 'smtp.qq.com'  # qq邮箱服务器
    SSL_PORT = '465'  # 加密端口
    USER_NAME = FROM_MAIL  # qq邮箱用户名
    USER_PWD = "hbjfwkfmawndbheg"  # qq邮箱授权码
    msg = email.mime.multipart.MIMEMultipart()  # 实例化email对象
    msg['from'] = FROM_MAIL  # 对应发件人邮箱昵称、发件人邮箱账号
    msg['to'] = ';'.join(TO_MAIL)  # 对应收件人邮箱昵称、收件人邮箱账号
    msg['subject'] = self.title  # 邮件的主题
    txt = email.mime.text.MIMEText(self.content)
    msg.attach(txt)
    try:
        # 纯粹的ssl加密方式
        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SSL_PORT)  # 邮件服务器地址和端口
        smtp.ehlo()  # 用户认证
        smtp.login(USER_NAME, USER_PWD)  # 括号中对应的是发件人邮箱账号、邮箱密码
        smtp.sendmail(FROM_MAIL, TO_MAIL, str(msg))  # 收件人邮箱账号、发送邮件
        smtp.quit()  # 等同 smtp.close()  ,关闭连接
    except Exception as e:
        ret = False
        print(">>>>>>>:" + e)
    return ret
