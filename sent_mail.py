from email.mime.multipart import MIMEMultipart #可以带附件
from email.mime.multipart import MIMEBase #附件编码
from email.mime.text import MIMEText
from email.header import Header
from email import encoders
import smtplib
import csv

'''用python群发邮件，但是这种方式，各收件人知道是群发。'''
# #写入CSV数据
# data = [['zz','284066224@qq.com'],['bb','568407171@qq.com']]
# with open('sent_mail_to_addrs.csv', 'w', newline='') as f:
#     w = csv.writer(f)
#     for row in data:
#         w.writerow(row) #CSV的写入方式有别于txt的writeline()

# 邮件头信息
mail_subject = input('请输入邮件主题：') # '终于可以用python发带附件的邮件啦'
from_addr = input('发件箱：') # from_addr = '284066224@qq.com'
password = input('授权码：') # password = 'tofxuycrozzjbiii' #授权码，而非密码
smtp_serve = 'smtp.qq.com'  #qq邮箱服务器
to_addr = '' #通过下文读取CSV文件，这里纯粹是为了保持队形

# 1创建邮件对象
msg = MIMEMultipart()
# 2创建正文部分
text = 'python群发'
# 3添加邮件正文到邮件对象
msg.attach(MIMEText(text, 'plain', 'utf-8'))
# 4导入附件部分
with open('loveyou.gif','rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'gif', filename='test.gif')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.gif')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 5添加附件到邮件对象
    msg.attach(mime)
# 6自定义邮件头
msg['From'] = Header(from_addr) #内容可以自定义
msg['Subject'] = Header(mail_subject)
# 读取CSV中的邮箱地址，并依次发达邮件
with open('sent_mail_to_addrs.csv', 'r') as f:
    r = csv.reader(f) #CSV的读取方式
    for row in r:
        to_addr = row[1]
        msg['To'] = Header(to_addr)
        # 7发送邮件 
        serve = smtplib.SMTP_SSL(smtp_serve)
        '''ValueError: server_hostname cannot be an empty string or start with a leading dot.
        因为Python 3.7修改了ssl.py，导致smtplib.SMTP_SSL也连带产生了问题
        改动这句代码，在括号内加入host参数'''
        # 连接服务器
        serve.connect(smtp_serve,465)
        # 日志信息
        # serve.set_debuglevel(1)
        # 登录服务器
        serve.login(from_addr,password)
        # 发送
        try:
            serve.sendmail(from_addr,to_addr,msg.as_string())
            print('恭喜，%s发送成功'% to_addr)
        except:
            print('发送失败，请重试')


serve.quit()