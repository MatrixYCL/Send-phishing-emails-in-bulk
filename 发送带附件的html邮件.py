# Filename  ：test.py
# Author by ：袁成龙
# Data      ：2023 02 18 14:03
######################### 发送URL内容及图片，SUCCESS #########################
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

# 设置邮箱服务器地址以及端口
smtp_server = "smtp.qq.com"
smtp_obj = smtplib.SMTP(smtp_server, 25)
smtp_obj.login("xxxx@qq.com","xxxxx")
smtp_obj.set_debuglevel(1)      				# 显示调试信息

# 设置邮件内容
mail_body ='''
    <h5> hello,小哥哥</h5>
    <p>
        小哥哥，您好2023...... <a href="http://www.baidu.com">这是我的照片</a></p>
    </p>
'''

msg = MIMEMultipart('related')     			# 允许添加附件、照片
# msg = MIMEText(mail_body,"html","utf-8")
msg["From"] = Header("来自娜美的问候2023","utf-8")     	# 发送人
msg["To"]=Header("有缘人","utf-8")             		# 接收者
msg["Subject"]=Header("娜美的信2023","utf-8")   		# 邮件主题

# 允许添加照片
msgAlternative = MIMEMultipart('alternative')
msgAlternative.attach(MIMEText(mail_body,'html','utf-8'))
msg.attach(msgAlternative)     # 把邮件正文内容添加到 msg_root 里

# 加载图片
fp = open('test1.jpg','rb')
msgImage=MIMEImage(fp.read())
fp.close()

# 定义图片ID，在HTML文本中引用
msgImage.add_header('Content-Disposition','attachment',filename='test1.jpg')
msgImage.add_header('Content-ID','<image1>')
msg.attach(msgImage)       			# 添加图片到 msg_root对象里

# 发送
smtp_obj.sendmail("xx3876@qq.com",["102xx@qq.com","76xxx047@qq.com"],msg.as_string())	# 单独群发，收件人只能看到收件人是自己，即发了多封邮件
