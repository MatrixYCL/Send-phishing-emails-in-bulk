# Filename  ：test.py
# Author by ：袁成龙
# Data      ：2022 10 18 14:00
###########################  SUCCESS  ###########################
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

# 设置邮箱服务器地址以及端口
smtp_server = "smtp.qq.com"
smtp_obj = smtplib.SMTP(smtp_server, 25)
smtp_obj.login("xxxx@qq.com","xxxxc")

# 设置邮件内容
mail_body ='''
    <h5> hello,小哥哥</h5>
    <p>
        小哥哥，您好2023...... <a href="http://www.baidu.com">这是我的照片</a></p>
    </p>
'''
msg = MIMEText(mail_body,"html","utf-8")
msg["From"] = Header("来自娜美的问候2023","utf-8")     	# 发送人
msg["To"]=Header("有缘人","utf-8")             		# 接收者
msg["Subject"]=Header("娜美的信2020","utf-8")   		# 邮件主题

smtp_obj.sendmail("xxxx@qq.com",["1xxxx2064@qq.com","639047@qq.com"],msg.as_string())	# 单独群发，收件人只能看到收件人是自己，即发了多封邮件
