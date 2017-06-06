#coding:utf-8
import requests,time
import xml.dom.minidom
from xml.etree import ElementTree as ET
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

mail_port = 25
mail_host = 'smtp.163.com'
mail_user = ''
mail_pass = ''	
	
def _format_addr(s):
  name, addr = parseaddr(s)
  return formataddr(( \
    Header(name, 'utf-8').encode(), \
    addr.encode('utf-8') if isinstance(addr, unicode) else addr))
def sendMail(yx):
	msg = MIMEText(u'\
	你好，换友链吗<br />\
	我的关键词：京东优评,链接：https://yp.jd.com/<br />\
	我在https://club.jd.com/links.aspx<br />\
	给你加上链接,相当于各自给对方一个单向链接，OK吗？<br />\
	可以的话加我微信详谈:***<br />\
	-----------------------------------------------<br />\
	此邮件通过Python自动发送\
	','html','utf-8')
	msg['Subject'] = Header(u'京东商城-交换友链','utf-8')
	msg['From'] = _format_addr(u'京东SEO<***>')
	mail_to = yx
	msg['To'] = '%s'%yx	
	s = smtplib.SMTP()
	s.connect(mail_host,mail_port)
	s.login(mail_user, mail_pass)
	s.sendmail(mail_user,mail_to, msg.as_string())
	s.close()

if __name__ == "__main__":
	num = 0
	for yx in open('yx.txt'):
		sendMail(yx.strip())
		time.sleep(5)
		num += 1
		print num
		
		
		
		
