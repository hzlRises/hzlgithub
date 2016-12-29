#coding:utf-8
import requests,re,time,string,random
from bs4 import BeautifulSoup
author = 'heziliang'
def getUA():
	uaList = [
		'Mozilla/4.0+(compatible;+MSIE+6.0;+Windows+NT+5.1;+SV1;+.NET+CLR+1.1.4322;+TencentTraveler)',
		'Mozilla/4.0+(compatible;+MSIE+6.0;+Windows+NT+5.1;+SV1;+.NET+CLR+2.0.50727;+.NET+CLR+3.0.4506.2152;+.NET+CLR+3.5.30729)',
		'Mozilla/5.0+(Windows+NT+5.1)+AppleWebKit/537.1+(KHTML,+like+Gecko)+Chrome/21.0.1180.89+Safari/537.1',
		'Mozilla/4.0+(compatible;+MSIE+6.0;+Windows+NT+5.1;+SV1)',
		'Mozilla/5.0+(Windows+NT+6.1;+rv:11.0)+Gecko/20100101+Firefox/11.0',
		'Mozilla/4.0+(compatible;+MSIE+8.0;+Windows+NT+5.1;+Trident/4.0;+SV1)',
		'Mozilla/4.0+(compatible;+MSIE+8.0;+Windows+NT+5.1;+Trident/4.0;+GTB7.1;+.NET+CLR+2.0.50727)',
		'Mozilla/4.0+(compatible;+MSIE+8.0;+Windows+NT+5.1;+Trident/4.0;+KB974489)',
		'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
		'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
		"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
		"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
	]
	newUa = random.choice(uaList) 
	return newUa

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8",
	"Cache-Control":"max-age=0",
    "Connection": "keep-alive",
#    "Cookie": "",
    "Host": "book.douban.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": getUA(), 
}
#27046
for i in range(14,1000):
	print i
	url = 'https://book.douban.com/series/%s'%i	
	try:
		r = requests.get(url,headers=headers)
	except Exception,e:
		print e
		pass
	if "paginator" not in r.content:		
		s = BeautifulSoup(r.content,"lxml")		
		for wz in s.find_all('h2'):
			try:
				print wz.get_text().replace('\n','').replace(' ','')			
				with open('re.txt',r'a+') as my:
					my.write(wz.get_text().replace('\n','').replace(' ','').encode('utf-8')+'\n')
			except Exception,e:
				print e
				pass
	if "paginator" in r.content:
		print 'has paginator'
		s = BeautifulSoup(r.content,"lxml")
		for wz in s.find_all('h2'):
			try:
				print wz.get_text().replace('\n','').replace(' ','')
				with open('re.txt',r'a+') as my:
					my.write(wz.get_text().replace('\n','').replace(' ','').encode('utf-8')+'\n')
			except Exception,e:
				print e
				pass
		for fenpage in s.find('div',attrs={'class':'paginator'}).find_all('a'):
			if fenpage.get_text().isdigit():
				print fenpage.get('href')
				r_paginator = requests.get(fenpage.get('href'),headers=headers)
				s_paginator = BeautifulSoup(r_paginator.content,"lxml")
				for title in s_paginator.find_all('h2'):
					try:
						print title.get_text().replace('\n','').replace(' ','')
						with open('re.txt',r'a+') as my:
							my.write(title.get_text().replace('\n','').replace(' ','').encode('utf-8')+'\n')
					except Exception,e:
						print e
						pass
'''
#coding:utf-8
import requests,re,time,string,random,sys,threading
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool
reload(sys)
sys.setdefaultencoding('utf-8')
author = 'heziliang'
totalThread = 1
def getUA():
	uaList = [
		"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
		"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
	]
	newUa = random.choice(uaList) 
	return newUa

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8",
	"Cache-Control":"max-age=0",
    "Connection": "keep-alive",
	"Host": "book.douban.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": getUA(), 
}
#27046
def gofuckyouself(id):
	try:
		r = requests.get(id,headers=headers)
	except Exception,e:
		print e
	if "paginator" not in r.content:		
		s = BeautifulSoup(r.content,"lxml")		
		for wz in s.find_all('h2'):
			try:
				print wz.get_text().replace('\n','').replace(' ','')
				mutex.acquire()	
				with open('result.txt',r'a+') as my:
					my.write(wz.get_text().replace('\n','').replace(' ','').encode('utf-8')+'\n')
				with open('hasdone.txt',r'a+') as you:
					you.write(id+'\n')
				mutex.release()

			except Exception,e:
				print e
				pass
	if "paginator" in r.content:
		print 'has paginator'
		s = BeautifulSoup(r.content,"lxml")
		for wz in s.find_all('h2'):
			try:
				print wz.get_text().replace('\n','').replace(' ','')
				mutex.acquire()
				with open('result.txt',r'a+') as my:
					my.write(wz.get_text().replace('\n','').replace(' ','').encode('utf-8')+'\n')
				with open('hasdone.txt',r'a+') as you:
					you.write(id+'\n')
				mutex.release()
			except Exception,e:
				print e
				pass
		for fenpage in s.find('div',attrs={'class':'paginator'}).find_all('a'):
			if fenpage.get_text().isdigit():
				print fenpage.get('href')
				r_paginator = requests.get(fenpage.get('href'),headers=headers)
				s_paginator = BeautifulSoup(r_paginator.content,"lxml")
				for title in s_paginator.find_all('h2'):
					try:
						print title.get_text().replace('\n','').replace(' ','')
						mutex.acquire()
						with open('result.txt',r'a+') as my:
							my.write(title.get_text().replace('\n','').replace(' ','').encode('utf-8')+'\n')
						mutex.release()
					except Exception,e:
						print e
						pass			
def main():
	urlNum = 0
	url_list = []	
	urlNum_list = []
	for i in range(4142,27047):
		url = 'https://book.douban.com/series/%s'%i		
		url_list.append(url)
		urlNum_list.append(urlNum)
		urlNum += 1		
	pool = ThreadPool(totalThread)
	pool.map(gofuckyouself, url_list)
	pool.close() 
	pool.join()
mutex = threading.Lock()
main()
	

'''
