#coding:utf-8
import urllib2
import sys
import pycurl
import re
import StringIO
from bs4 import BeautifulSoup
from time import sleep
#import subprocess
#import os
reload(sys)
sys.setdefaultencoding('utf-8')
#url = 'http://home.fang.com/zhishi/'
def reg():	
	return '(fang.com|soufun.com|youtx.com|txdai.com|hkproperty.com|jiatx.com)'#需要剔除的自家顶级域名

with open('result.txt',r'a+') as my:
	for url in open('url.txt'):
		url = url.strip()
		my.write('>>>>>>>>>>>>>>>>>>>>>>>>>>'+url+'<<<<<<<<<<<<<<<<<<<<<<<<<<'+'\n')		
		html = urllib2.urlopen(urllib2.Request(url)).read()
		soup = BeautifulSoup(html,"lxml")
		all_a = soup.find_all('a')
		for ab in all_a:
			youLian = re.findall(r'(http.*)',ab.get('href'))#去掉js、不是绝对路径等链接		
			if(youLian):
				str = "".join(youLian)#list转换成字符串
				if(str):#以http开的链接					
					yL = re.findall(reg(),str)#匹配到自家顶级域名
					str1 = "".join(yL)				
					if(str1 == ''):#如果没有匹配到自家顶级域名，就可以判断为友链					
	#					youlianurl_list.append(str)					
						try:
							c = pycurl.Curl()
							c.setopt(c.URL,str)
							c.setopt(c.FOLLOWLOCATION, True)
							c.setopt(c.ENCODING, 'gzip,deflate')
							c.setopt(c.CONNECTTIMEOUT, 60)
							c.setopt(c.TIMEOUT,120)
							c.setopt(c.MAXREDIRS,2)
							b = StringIO.StringIO()
							c.setopt(c.WRITEFUNCTION, b.write)
							c.perform()
							code = b.getvalue()
							match = re.search(r'home\.fang\.com',code)
							if match:
								print 'YES> '+str
							else:
								print 'NO> '+str
								my.write(str+'\n')																
						except:
							print 'Could not resolve host:%s' %str
							my.write('Could not resolve host:'+str+'\n')												
					else:
						pass
				else:
					pass
			else:
				pass		
'''
os.system('cat all_a_list.txt|grep "http"|grep -v "fang.com\|#\|soufun.com\|youtx.com\|txdai.com\|hkproperty.com\|jiatx.com" > youlianurl.txt')
os.system('cat all_a_list.txt|grep "http"|grep -v "fang.com"|grep -v "#"|grep -v "soufun.com"|grep -v "youtx.com"|grep -v "txdai.com"|grep -v "hkproperty.com"|grep -v "jiatx.com" > youlianurl.txt')	
subprocess.call(["cat domain.txt|sort|uniq -c|sort -r|head -100 > sortedTop100Domain.txt"],shell='true')
'''
