#coding:utf-8
import	HeaderData,re,sys
import requests,time
from bs4 import BeautifulSoup

reload(sys) 
sys.setdefaultencoding('utf8')

def get_long_url(url):
	try:
		r = requests.get('https:'+url,headers=HeaderData.get_header(),timeout=60)				
		s = BeautifulSoup(r.content,"lxml")
		ptag = s.find_all("p",attrs={"class":"view mb20"})			
		atag = s.find_all("a",attrs={"class":"careful"})
		
		for a in atag:
			uri = a.get('href')
			if 'qzbd' in uri:
				get_long_url(uri)				
			else:
				f.write(uri+'\n')
				print uri
				
		for p in ptag:
			uri =  p.find('a').get('href')
			if 'qzbd' in uri:
				get_long_url(uri)
			else:
				f.write(uri+'\n')	
				print uri
				
	except Exception,e:
		print e	
		
def main():	

	url_list = ['http://baike.pcbaby.com.cn/fenmian.html','http://baike.pcbaby.com.cn/yuezi.html','http://baike.pcbaby.com.cn/xinshenger.html','http://baike.pcbaby.com.cn/yinger.html','http://baike.pcbaby.com.cn/youer.html','http://baike.pcbaby.com.cn/xuelingqian.html','http://baike.pcbaby.com.cn/yongpin.html','http://baike.pcbaby.com.cn/shenghuo.html']
	for i in url_list:	
		url = i
		print url
		try:
			r = requests.get(url,headers=HeaderData.get_header(),timeout=60)				
			s = BeautifulSoup(r.content,"lxml")
			atag = s.find("div",attrs={"id":"Jbaike"}).find_all('a')			
			for a in atag:
				url =  a.get('href')
				if 'qzbd' in url:					
					f_qzbd.write(url+'\n')
					get_long_url(url)				
			
		except Exception,e:
			print e			
		time.sleep(0.1)	
	
		
if __name__ == '__main__':
	f_qzbd = open('qzbd_url.txt',r'a+')
	f = open('long_url.txt',r'a+')
	main()
	f.close()
	f_qzbd.close()
	
	
