#coding:utf-8
import requests,sys,time
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup
def getWord(url):
	r = requests.get(url)	
	s = BeautifulSoup(r.content,"lxml")	
	for ul in s.find_all('ul',attrs={'class':'baike-list'}):
		print ul.get_text().strip()
		with open('result.txt',r'a+') as myfile:
			myfile.write(ul.get_text().strip())
def main():
	start = time.clock()
	url = ['http://baike.bzw315.com/zx/','http://baike.bzw315.com/sj/','http://baike.bzw315.com/cp/','http://baike.bzw315.com/pp/','http://baike.bzw315.com/sh/']
	for url in url:		
		getWord(url)
	end = time.clock()
	print 'RunTime: '+'%1.f s' %(end - start)
main()
