#coding:utf-8
_author_ = 'heziliang'
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = 'smtp.163.com'
mail_user = '****'
mail_pass = '****'
mail_to = '****'

def sendMail(sub,content):
	msg = MIMEText(content,'plain','utf-8')
	msg['Subject'] = Header(sub,'utf-8')  #主题	
	msg['From'] = mail_user#
	msg['To'] = mail_to#
	s = smtplib.SMTP()
	s.connect(mail_host)
	s.login(mail_user, mail_pass)
	s.sendmail(mail_user,mail_to, msg.as_string())
	s.close()	
def main():	
	sendMail('666','666')#主题和内容
	print 'success'	
main()
	
