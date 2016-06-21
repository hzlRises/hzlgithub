#coding:utf-8
import urllib2
import sys
import re
import pycurl
import StringIO
from bs4 import BeautifulSoup
import os
import subprocess
reload(sys)
sys.setdefaultencoding('utf-8')
#url = 'http://home.fang.com/zhishi/'
for url in open('url.txt'):
	url = url.strip()
	html = urllib2.urlopen(urllib2.Request(url)).read()
	soup = BeautifulSoup(html,"lxml")
	all_a = soup.find_all('a')	
	for ab in all_a:		
		with open('all_a_list.txt',r'a+') as my:
			my.write(ab.get('href')+'\n')	
	os.system('cat all_a_list.txt|grep "http"|grep -v "fang.com"|grep -v "#"|grep -v "soufun.com"|grep -v "youtx.com"|grep -v "txdai.com"|grep -v "hkproperty.com"|grep -v "jiatx.com" > youlianurl.txt')	
	#subprocess.call(["cat domain.txt|sort|uniq -c|sort -r|head -100 > sortedTop100Domain.txt"],shell='true')
	
	with open('youlianurl.txt',r'r') as myurl:
		with open('result.txt',r'a+') as my:
			my.write(url+'>>>>>>>>>>>>>>>>>>>>>>>>>'+'\n')			
		for u in myurl.readlines():
			u = u.strip()
			c = pycurl.Curl()
			c.setopt(c.URL,u)
			c.setopt(c.FOLLOWLOCATION, True)
			c.setopt(c.MAXREDIRS,2)
			b = StringIO.StringIO()
			c.setopt(c.WRITEFUNCTION, b.write)
			c.perform()
			code = b.getvalue()
			match = re.search(r'home\.fang\.com',code)
			with open('result.txt',r'a+') as my:				
				if match:
					print u+' has '+url
				else:
					print u+' has no '+url
					my.write(u+'\n')
		os.remove('all_a_list.txt')
os.remove('youlianurl.txt')
