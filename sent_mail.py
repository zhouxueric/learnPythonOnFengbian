import smtplib
from email.mime.text import MIMEText
from email.header import Header
import csv

'''用python群发邮件，但是这种方式，各收件人知道是群发。'''
# #写入CSV数据
# data = [['老公','284066224@qq.com'],['宝贝','568407171@qq.com']]
# with open('sent_mail_to_addrs.csv', 'w', newline='') as f:
#     w = csv.writer(f)
#     for row in data:
#         w.writerow(row)

# from_addr = '284066224@qq.com'
# password = 'tofxuycrozzjbiii' #授权码，而非密码
from_addr = input('发件箱：')
password = input('授权码：')
smtp_serve = 'smtp.qq.com'
mail_subject = '用python发邮件'
text = 'python群发'
msg = MIMEText(text, 'plain', 'utf-8')
msg['From'] = Header(from_addr) #可以自定义
msg['Subject'] = Header(mail_subject)
with open('sent_mail_to_addrs.csv', 'r') as f:
    r = csv.reader(f)
    for row in r:
        to_addr = row[1]
        msg['To'] = Header(to_addr)
        serve = smtplib.SMTP_SSL(smtp_serve)
        '''ValueError: server_hostname cannot be an empty string or start with a leading dot.
        因为Python 3.7修改了ssl.py，导致smtplib.SMTP_SSL也连带产生了问题
        改动这句代码，在括号内加入host参数'''
        serve.connect(smtp_serve,465)
        # serve.set_debuglevel(1)
        serve.login(from_addr,password)
        try:
            serve.sendmail(from_addr,to_addr,msg.as_string())
            print('恭喜，%s发送成功'% to_addr)
        except:
            print('发送失败，请重试')


serve.quit()