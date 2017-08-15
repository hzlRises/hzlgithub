#coding:utf-8
#处理关键词特殊字符
import requests,sys,time,re
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')
author = 'heziliang'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "__jda=122270672.1496654831191591020064.1496654831.1499329155.1499908086.30; __jdu=1496654831191591020064; ipLoc-djd=1-72-4137-0; areaId=1; __jdv=122270672|baidu|-|organic|not set|1498616240066; xtest=2217.8731.604.cf6b6759; mx=0_X; ipLocation=%u5317%u4EAC; __jdb=122270672.2.1496654831191591020064|30.1499908086; __jdc=122270672; rkv=V0000",
    "Host": "search.jd.com",
	"Referer":"https://www.jd.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
}
successNUm = 0
failNum = 0
def getCountnum(kw):
	global successNUm
	global failNum
	keyw = kw.split(',')[0]#只取组合后关键词
	try:
		url = 'https://search.jd.com/Search?keyword=%s&enc=utf-8'%keyw
		r = requests.get(url,headers=headers)
		s = BeautifulSoup(r.content,'lxml')
		resCount = s.find('span',attrs={'id':'J_resCount'}).get_text()
		if '+' in str(resCount):
			resCount = resCount.replace('+','')
		with open('result_2.txt',r'a+') as my:#结果存放文件
			my.write(kw+','+resCount+'\n')
		successNUm += 1
	except Exception,e:
		with open('fail_2.txt',r'a+') as my:#异常关键词文件
			my.write(kw+'\n')
		failNum += 1
		print e 
	print 'successNUm,failNum:'+successNUm+','+failNum
	
def main():
	for line in open('2.txt'):#
		kw = line.strip()
		reg = re.compile(r'(\(.*?\))')
		reg2 = re.compile(r'（.*?）')
		reg3 = re.compile(r'(\(.*?）)')
		reg4 = re.compile(r'(（.*?\))')
		reg5 = re.compile(r'\&')
		kw = re.sub(reg,'',kw)#两边都是英文括号
		kw = re.sub(reg2,'',kw)#两边都是中文括号
		kw = re.sub(reg3,'',kw)#左边英文，右边中文
		kw = re.sub(reg4,'',kw)#左边中文，右边英文
		kw = re.sub(reg5,'',kw)#&符号
		kw = kw.upper()#小写变大写
		getCountnum(kw)
		time.sleep(0.1)

if __name__ == '__main__':
	main()
	
	
	
	
	
	
'''
#品牌+三级分类关键词
#coding:utf-8
#处理关键词特殊字符
import requests,sys,time,re
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import Encoders
reload(sys)
sys.setdefaultencoding('utf8')
author = 'heziliang'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "unpl=V2_YDNtbUIFSkIlDEdVKxgJB2IBGwkSXkZCcglGXCgbVQJvV0EOclRCFXMUR1NnGlQUZwQZX0RcQhVFCHZXfBpaAmEBFl5yBBNNIEwEACtaDlwJARZcSlNHFHwAT1FLKV8FVwMTbUJSSxN3CE9UeRleAmIGFV5HVkUdfQB2ZHwpbDVjBxpeRFNzFEUJdhYvRVQFYAsQXw9XRh1zCkZdextcB2AGF1pBUkITfQBOZHopXw%3d%3d; areaId=1; dmpjs=dmp-d397334d8775b9e47c1b57a4965d93c531df885; sso.jd.com=14c8d0262ccd4c26b0eaf72cc4bb09c4; TrackID=1rF6W-FCjri_MEgfRa2KTWaRF3R1sze8LDTprx0d72_o9QIuK_FOtusYR0kbbtroHC5fwKQnBk2lb5GSGNnpS1le4dL2wzfZaJhqZseHiWzI; pinId=qs7eO3zat2CJ-45-Bvmd6bV9-x-f3wj7; unick=jd_619237350; _tp=v3jaNqGkC7JI3eyGwLdKcShMkQUtIh4HZu%2FnFibvd98%3D; _pst=jd_53c836d89d9e0; ceshi3.com=103; user-key=1afba303-1aed-4b52-b12c-d066bd5b8827; ipLocation=%u5317%u4eac; __jdv=182888763|baidu|-|organic|%25E7%2599%25BE%25E5%25BA%25A6%25E7%2590%2586%25E8%25B4%25A2%25E6%2596%25B0%25E6%2589%258B%25E4%25B8%2593%25E4%25BA%25AB|1499922736586; ipLoc-djd=1-2809-51217-0.138636316; mt_xid=V2_52007VwMXWltaUlMfSxleAmIGFVFYWVRSF0EpX1ZjVxsFWFFOWhkbTEAAMwBFTg4LUV8DSxsJUmJUQVUJWwBdL0oYXAN7AhROXVpDWhpCGlsOZQUiUG1YYlofSxpcDGMEEGJdXVRd; cn=0; rkv=V0600; xtest=4624.8257.7027.cf6b6759; mx=0_X; __jda=122270672.1497318131364462407999.1497318131.1499922737.1499926485.12; __jdb=122270672.67.1497318131364462407999|12.1499926485; __jdc=122270672; __jdu=1497318131364462407999",
    "Host": "search.jd.com",
	"Referer":"https://www.jd.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
}
successNUm = 0#成功数
failNum = 0#失败数
def getCountnum(i,kw):#文件后缀、关键词
	global successNUm
	global failNum
	keyw = kw.split(',')[0]#只取组合后关键词
	#请求搜索
	try:
		url = 'https://search.jd.com/Search?keyword=%s&enc=utf-8'%keyw
		r = requests.get(url,headers=headers)
		s = BeautifulSoup(r.content,'lxml')
		resCount = s.find('span',attrs={'id':'J_resCount'}).get_text()
		if '+' in str(resCount):
			resCount = resCount.replace('+','')
		with open('result_%s.txt'%i,r'a+') as my:#结果存放文件
			my.write(kw+','+resCount+'\n')
		successNUm += 1
	except Exception,e:
		with open('fail_%s.txt'%i,r'a+') as my:#异常关键词文件
			my.write(kw+'\n')
		failNum += 1
		print e 
	print 'successNUm,failNum:'+str(successNUm)+','+str(failNum)
	
mail_host = 'smtp.163.com'
mail_user = '@163.com'
mail_pass = ''
mail_to = ''

#发送附件邮件
def sendMail(rank):
	try:
		msg = MIMEMultipart()
		msg['Subject'] = Header(u'品牌+三级分词- %s of 36'%rank,'utf-8')  #主题	
		msg['From'] = mail_user#
		msg['To'] = mail_to#
	#	msg.attch(MIMEText(u'品牌+三级分词- %s of 36'%rank,'plain','utf-8'))
	#	with open('result_%s.txt'%rank,'rb') as f:
	#		mime = MIMEBase('file','txt',filename='result_%s.txt'%rank)
	#		mime.add_header('Content-Disposition', 'attachment', filename='result_%s.txt'%rank)
	#		mime.set_payload(f.read())
	#		Encoders.encode_base64(mime)
	#		msg.attach(mime)
		partSuccess = MIMEApplication(open('result_%s.txt'%rank,'rb').read())
		partSuccess.add_header('Content-Disposition','attachment',filename='result_%s.txt'%rank)
		msg.attach(partSuccess)
		
		partFail = MIMEApplication(open('fail_%s.txt'%rank,'rb').read())
		partFail.add_header('Content-Disposition','attachment',filename='fail_%s.txt'%rank)
		msg.attach(partFail)
	except Exception,e:
		print e
		#发送邮件
	try:
		s = smtplib.SMTP()
		s.connect(mail_host)
		s.login(mail_user, mail_pass)
		s.sendmail(mail_user,mail_to, msg.as_string())
		s.close()
	except Exception,e:
		print 'sendMail failed...'
		print e

def main():
	for i in range(0,2):
		for line in open('%s.txt'%i):#
			kw = line.strip()
			#处理字符
			reg = re.compile(r'(\(.*?\))')
			reg2 = re.compile(r'（.*?）')
			reg3 = re.compile(r'(\(.*?）)')
			reg4 = re.compile(r'(（.*?\))')
			reg5 = re.compile(r'\&')
			kw = re.sub(reg,'',kw)#两边都是英文括号
			kw = re.sub(reg2,'',kw)#两边都是中文括号
			kw = re.sub(reg3,'',kw)#左边英文，右边中文
			kw = re.sub(reg4,'',kw)#左边中文，右边英文
			kw = re.sub(reg5,'',kw)#&符号
			kw = kw.upper()#小写变大写
			getCountnum(i,kw)
			time.sleep(0.3)
		time.sleep(60)#处理完一个文件暂停30秒
		sendMail(i)#传参文件后缀

if __name__ == '__main__':
	main()


'''

'''
品牌+二级分类
#coding:utf-8
#处理关键词特殊字符
import requests,sys,time,re,urllib2,pycurl,StringIO
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import Encoders
#reload(sys)
#sys.setdefaultencoding('utf8')
author = 'heziliang'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "__jda=122270672.1496654831191591020064.1496654831.1500457135.1500463730.40; __jdu=1496654831191591020064; xtest=2217.8731.604.cf6b6759; mx=0_X; ipLocation=%u5317%u4EAC; __jdv=122270672|baidu|-|organic|not set|1500351606990; dmpjs=dmp-d100486c43717be8c7f2c62e02abd33a0585609; user-key=40f66c71-d1f5-40fe-b421-26b0ae7cbeba; cn=0; __jdc=122270672; sso.jd.com=bae981b6ad46402abcfa85726f5e96ba; __jdb=122270672.1.1496654831191591020064|40.1500463730",
    "Host": "search.jd.com",
    "Referer":"https://www.jd.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
}
num = 0

def jiexi(html):
	try:
		f_leimu = re.search(r'mbNav-1">(.*?)</a></div>',html)
		f_leimu = re.sub('mbNav-1">','',f_leimu.group(0))
		f_leimu = re.sub('</a></div>','',f_leimu)
	
		s_leimu = re.search(r'mbNav-2">(.*?)</a></div>',html)
		s_leimu = re.sub('mbNav-2">','',s_leimu.group(0))
		s_leimu = re.sub('</a></div>','',s_leimu)
		
		
		t_leimu = re.search(r'mbNav-3">(.*?)</a></div>',html)
		t_leimu = re.sub('mbNav-3">','',t_leimu.group(0))
		t_leimu = re.sub('</a></div>','',t_leimu)
		return f_leimu+','+s_leimu+','+t_leimu+','
	except Exception,e:
		print e



def getCountnum(kw):
	global num
	#请求搜索
	try:
		url = 'https://search.jd.com/Search?keyword=%s&enc=utf-8'%kw
		r = requests.get(url,headers=headers,timeout=60)
		s = BeautifulSoup(r.content,'lxml')
		resCount = s.find('span',attrs={'id':'J_resCount'}).get_text()
		#返回商品数
		if '+' in str(resCount):
			resCount = resCount.replace('+','')
		#返回商品第一个sku
		firstSku = s.find('li',attrs={'class':'gl-item'}).get('data-sku')
	except Exception,e:
		print e
	try:
		url_2 = 'https://item.jd.com/%s.html'%firstSku
		c = pycurl.Curl()
		c.setopt(pycurl.URL,url_2)
		c.fp = StringIO.StringIO()
		c.setopt(c.WRITEFUNCTION, c.fp.write)
		c.perform()
		html = c.fp.getvalue()
	except Exception,e:
		print e
	try:
		with open('result.txt',r'a+') as my:
			my.write(kw.decode('utf-8').encode('gbk')+','+jiexi(html)+str(resCount)+'\n')
		num += 1
		print num
	except Exception,e:
		print e
def main():
	for line in open('sid_kw.txt'):#
		kw = line.strip()
		#处理字符
		reg = re.compile(r'(\(.*?\))')
		reg2 = re.compile(r'（.*?）')
		reg3 = re.compile(r'(\(.*?）)')
		reg4 = re.compile(r'(（.*?\))')
		reg5 = re.compile(r'\&')
		kw = re.sub(reg,'',kw)#两边都是英文括号
		kw = re.sub(reg2,'',kw)#两边都是中文括号
		kw = re.sub(reg3,'',kw)#左边英文，右边中文
		kw = re.sub(reg4,'',kw)#左边中文，右边英文
		kw = re.sub(reg5,'',kw)#&符号
		kw = kw.upper()#小写变大写
		getCountnum(kw)
		time.sleep(0.1)
if __name__ == '__main__':
	main()




'''




'''

#coding:utf-8
#优评内已启用关键词
import requests,sys,time,re
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import Encoders
reload(sys)
sys.setdefaultencoding('utf8')
author = 'heziliang'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "mx=0_X; ipLocation=%u5317%u4eac; ipLoc-djd=1-2810-51081-0.138453223; cn=0; mt_xid=V2_52007VwMXWltaUlMfSxleAmIGFVFYWVRSF0EpWVJnAxBRWg1OXR5JHEAAZgMXTg5QUVwDSEpYBTUCQFJfCFMPL0oYXAN7AhtOXFBDWhlCGFsOZQYiUG1YYlofQB5ZAmIHG2JdXVRd; xtest=8133.cf6b6759; TrackID=1T5EuXf-GW_nDMjms6zHLILae2dn9RBjOPC_agJqDSzgjFtyHXYKeXnmOV4FNJXverDsCGtCxweO7L08iiSfIkvAweT9ycz2QmzCM8XZmrro; pinId=sEXqQzc6jbTC4-ywFcvXDrV9-x-f3wj7; unick=jd_188001lin; _tp=tAk%2BinB8QxVDni0qm6hl9DXhbd5sz3LXsCXtaG4AeX4%3D; _pst=jd_51a61be6b7e94; dmpjs=dmp-d217391dbf70cd8b8362421055cf0d288074c0c; __jdv=122270672|jd.com|dmp_1528|cpc|dmp_1528_80702_d217391dbf70cd8b8362421055cf0d288074c0c_1502421221|1502421222581; __jda=122270672.1497318131364462407999.1497318131.1499689625.1499853526.6; __jdb=122270672.12.1497318131364462407999|6.1499853526; __jdc=122270672; __jdu=1497318131364462407999; 3AB9D23F7A4B3C9B=SRFBEFEUQOW6A6HQK43UV4IIDN2F3ZNPV2LWJPBJJWDCACNBBMNYPY7ZYPLYE43ZEQGT7BO74O3V3VOUNSDW3C5KPI",
    "Host": "search.jd.com",
	"Referer":"https://www.jd.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
}
successNUm = 0#成功数
failNum = 0#失败数
re_num = 36#起始result后缀
def getCountnum(i,kw):#文件后缀、关键词
	global successNUm
	global failNum
	global re_num
	keyw = kw.split(',')[0].replace('"','')#只取组合后关键词

	if (successNUm + failNum)%50000 == 49999:
		time.sleep(60)#处理完一个文件暂停30秒
		sendMail(re_num)
		re_num += 1
		
	#请求搜索
	try:
		url = 'https://search.jd.com/Search?keyword=%s&enc=utf-8'%keyw
		r = requests.get(url,headers=headers,timeout=60)
		s = BeautifulSoup(r.content,'lxml')
		resCount = s.find('span',attrs={'id':'J_resCount'}).get_text()
		if '+' in str(resCount):
			resCount = resCount.replace('+','')
		with open('result_%s.txt'%re_num,r'a+') as my:#结果存放文件
			my.write(keyw+','+resCount+'\n')
		successNUm += 1
	except Exception,e:
		with open('fail_%s.txt'%re_num,r'a+') as my:#异常关键词文件
			my.write(keyw+'\n')
		failNum += 1
		print e 
	print 'successNUm,failNum:'+str(successNUm)+','+str(failNum)
	
mail_host = 'smtp.163.com'
mail_user = 'hzl_789789@163.com'
mail_pass = '201508241653hzl'
mail_to = 'heziliang@jd.com'

#发送附件邮件
def sendMail(rank):
	try:
		msg = MIMEMultipart()
		msg['Subject'] = Header(u'优评-运营添加-启用词- %s'%rank,'utf-8')  #主题
		msg['From'] = mail_user#
		msg['To'] = mail_to#
	#	msg.attch(MIMEText(u'品牌+三级分词- %s of 36'%rank,'plain','utf-8'))
	#	with open('result_%s.txt'%rank,'rb') as f:
	#		mime = MIMEBase('file','txt',filename='result_%s.txt'%rank)
	#		mime.add_header('Content-Disposition', 'attachment', filename='result_%s.txt'%rank)
	#		mime.set_payload(f.read())
	#		Encoders.encode_base64(mime)
	#		msg.attach(mime)
		partSuccess = MIMEApplication(open('result_%s.txt'%rank,'rb').read())
		partSuccess.add_header('Content-Disposition','attachment',filename='result_%s.txt'%rank)
		msg.attach(partSuccess)
		
#		partFail = MIMEApplication(open('fail_%s.txt'%rank,'rb').read())
#		partFail.add_header('Content-Disposition','attachment',filename='fail_%s.txt'%rank)
#		msg.attach(partFail)
	except Exception,e:
		print e
		#发送邮件
	try:
		s = smtplib.SMTP()
		s.connect(mail_host)
		s.login(mail_user, mail_pass)
		s.sendmail(mail_user,mail_to, msg.as_string())
		s.close()
	except Exception,e:
		print 'sendMail failed...'
		print e

def main():
	for i in range(5,10):
		for line in open('%s.csv'%i):#
			kw = line.strip()
			#处理字符
			reg = re.compile(r'(\(.*?\))')
			reg2 = re.compile(r'（.*?）')
			reg3 = re.compile(r'(\(.*?）)')
			reg4 = re.compile(r'(（.*?\))')
			reg5 = re.compile(r'\&')
			kw = re.sub(reg,'',kw)#两边都是英文括号
			kw = re.sub(reg2,'',kw)#两边都是中文括号
			kw = re.sub(reg3,'',kw)#左边英文，右边中文
			kw = re.sub(reg4,'',kw)#左边中文，右边英文
			kw = re.sub(reg5,'',kw)#&符号
			kw = kw.upper()#小写变大写
			kw = kw.replace(' ','')#空格
			getCountnum(i,kw)
			time.sleep(0.1)
if __name__ == '__main__':
	main()


'''



