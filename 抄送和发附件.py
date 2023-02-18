import smtplib
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.application import MIMEApplication

# 发件人邮箱
asender = "xxxx@qq.com"
# 收件人邮箱
areceiver = "xxxx@qq.com"
# 抄送人邮箱
acc = 'xxxx@qq.com'
# 邮件主题
asubject = '这是一份测试邮件'

# 发件人地址
from_addr = "xxxx@qq.com"
# 邮箱密码（授权码）
password = "xxxxxfc"

# 邮件设置
msg = MIMEMultipart()
msg['Subject'] = asubject
msg['to'] = areceiver
msg['Cc'] = acc
msg['from'] = "xxxxx"

# 邮件正文
body = "你好，这是一份测试邮件"
# 添加邮件正文:
msg.attach(MIMEText(body, 'plain', 'utf-8'))

# 添加附件
# 注意这里的文件路径是斜杠
xlsxpart = MIMEApplication(open('测试文件.xlsx', 'rb').read())
xlsxpart.add_header('Content-Disposition', 'attachment', filename='这是附件.xlsx')      # 附件重命名
msg.attach(xlsxpart)

# 设置邮箱服务器地址以及端口
smtp_server = "smtp.qq.com"
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
# 登陆邮箱
server.login(from_addr, password)

# 发送邮件
server.sendmail(from_addr, areceiver.split(',') + acc.split(','), msg.as_string())
# 断开服务器链接
server.quit()