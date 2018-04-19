#coding:utf-8
import	HeaderData,re,sys
import requests,time
from bs4 import BeautifulSoup

reload(sys) 
sys.setdefaultencoding('utf8')

file_name = 'yuqian'

def main():	
	i = 0
	for line in open('%s_detail_url.txt'%file_name):
		url = 'https:'+line.strip()
		try:
			r = requests.get(url,headers=HeaderData.get_header(),timeout=60)				
			s = BeautifulSoup(r.content,"lxml")
			ptag = s.find_all("p",attrs={"class":"view mb20"})
			
			atag = s.find_all("a",attrs={"class":"careful"})
			for a in atag:
				url = a.get('href')
				if 'qzbd' in url:
					with open('yuqian_detail_url_qzbd.txt',r'a+') as my:
						my.write(url+'\n')
				else:
					f.write(url+'\n')
					
			for p in ptag:
				url =  p.find('a').get('href')
				if 'qzbd' in url:
					with open('yuqian_detail_url_qzbd.txt',r'a+') as my:
						my.write(url+'\n')
				else:
					f.write(url+'\n')				
		except Exception,e:
			print e	
		i += 1
		print i,line.strip()
	
	'''
	for i in range(1,2):
		url = 'https://baike.pcbaby.com.cn/yunqian.html'
		try:
			r = requests.get(url,headers=HeaderData.get_header(),timeout=60)				
			s = BeautifulSoup(r.content,"lxml")
			atag = s.find("div",attrs={"id":"Jbaike"}).find_all('a')			
			for a in atag:
				url =  a.get('href')
				if 'qzbd' in url:
					f.write(url+'\n')
				print i
		except Exception,e:
			print e			
		time.sleep(0.1)	
	'''
		
if __name__ == '__main__':
	f = open('%s_long_url.txt'%file_name,r'a+')
	main()
	f.close()
	
