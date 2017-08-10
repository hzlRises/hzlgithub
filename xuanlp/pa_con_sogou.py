#coding:utf8
import requests,re,sys
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')
url = 'http://wenwen.sogou.com/z/q285435043.htm?sw=%E9%80%81%E5%A5%B3%E6%9C%8B%E5%8F%8B%E7%94%9F%E6%97%A5%E7%A4%BC%E7%89%A9&ch=new.w.search.1&'

r = requests.get(url)
print r.status_code


s = BeautifulSoup(r.content,"lxml")

con = s.find_all('pre',attrs={'class':'replay-info-txt answer_con'})
con_str = ''
for c in con:
	try:
		print c.get_text().encode('utf8')#
#		with open('re_sogou.txt',r'a+') as my:
#			my.write('<p>'+c.get_text().encode('utf8')+'</p>')
		con_str += '<p>'+c.get_text().encode('utf8')+'</p>'
	except Exception,e:
		print e
	
	
	
with open('asd.txt',r'a+') as you:
	you.write(con_str)
