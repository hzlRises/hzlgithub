#coding:utf-8
import	HeaderData,re,sys
import requests,time
from bs4 import BeautifulSoup

reload(sys) 
sys.setdefaultencoding('utf8')

def get_long_url(url):
	num_1 = 0
	num_2 = 0
	try:
		r = requests.get('https:'+url,headers=HeaderData.get_header(),timeout=60)				
		s = BeautifulSoup(r.content,"lxml")
		ptag = s.find_all("p",attrs={"class":"view mb20"})			
		atag = s.find_all("a",attrs={"class":"careful"})
		
		for a in atag:
			uri = a.get('href')
			if 'qzbd' in uri:
				num_1 += 1
				if num_1 > 3:
					break
				else:
					get_long_url(uri)		
			else:
				f.write(uri+'\n')
				print uri
				
		for p in ptag:
			uri =  p.find('a').get('href')
			if 'qzbd' in uri:
				num_2 += 1
				if num_2 > 3:
					break
				else:
					get_long_url(uri)
			else:
				f.write(uri+'\n')	
				print uri
				
	except Exception,e:
		print e
		
def main():	
	url_list = [url.strip() for url in open('z_url.txt')]	
	for k,i in enumerate(url_list):
		url = i.split(',')[1]
		print k,url	
		try:
			r = requests.get(url,headers=HeaderData.get_header(),timeout=60)				
			s = BeautifulSoup(r.content,"lxml")
			ultag = s.find_all("div",attrs={"class":"mod-title"})
			
			for atag in ultag:
				if atag.find('a'):
					if 'art' in atag.find('a').get('href'):
						a = atag.find('a').get('href')			
						f.write(i+','+a+'\n')		
				#else		
			
			'''
			for ul in ultag:
				atag = ul.find_all('a')
				for a in atag:
					if '#' in a.get('href'):
						pass
					else:
						print a.get('href')
						f.write(url+','+a.get('href')+'\n')
			'''
		except Exception,e:
			print e			
		time.sleep(0.1)

if __name__ == '__main__':
	f = open('z_art_url.txt',r'a+')
	main()
	f.close()
	
