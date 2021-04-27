#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib

#HOST = "smtp.office365.com:587" #定义smtp主机
HOST="smtp3.hpe.com:25"
SUBJECT = "test" #定义邮件主题
TO = "ke.wang@hpe.com" #定义邮件收件人
FROM = "liang.yan@hpe.com" #定义邮件发件人
#plain text
BODY = "python test mail" #邮件的内容
#MIME text


server = smtplib.SMTP() #创建一个SMTP对象
server.connect(HOST) #通过connect方法连接smtp主机
#server.starttls() #启动安全传输模式
#server.login("liang.yan@hpe.com","!@#qweasdZXC") #邮件账户登录校验
server.login(null,null)
server.sendmail(FROM,TO,BODY) #邮件发送
server.quit() #断开smtp连接 
print("mail sent...")


def send_mail(self,message,title):
	print("sending email....")
	import smtplib
	from eamil.MIMEMultipart import MIMEMultipart
