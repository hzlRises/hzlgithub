#coding:utf-8
import	HeaderData,re,sys
import requests,time
from bs4 import BeautifulSoup
reload(sys) 
sys.setdefaultencoding('utf8')

def get_arturl(m,maxpage):
	f = open('%s.txt'%m.replace('/',''),r'a+')
	for i in range(1,int(maxpage)):
		time.sleep(1)
		try:
			url = 'http://www.7y7.com'+m+'index_%s.html'%i
			r = requests.get(url,headers=HeaderData.get_header(),timeout=60)
			if r.status_code == 200 and 'i.7y7.com' in r.content:
				s = BeautifulSoup(r.content,"lxml")
				top = s.find_all('div',attrs={"class":"top"})
				for t in top:
					art_link = t.find('a').get('href')
					f.write(art_link+'\n')				
			print i,maxpage
		except Exception,e:
			print e
			if '10054' in e:
				time.sleep(10)
				print 'sleep 10s...'
	f.close()

def main():
	mulu = [line.strip() for line in open('mulu.txt')]
	for m in mulu:
		#http://www.7y7.com/shoushen/index_960.html
		url = 'http://www.7y7.com'+m+'index_10000.html'
		r = requests.get(url,headers=HeaderData.get_header(),timeout=60)
		s = BeautifulSoup(r.content,"lxml")
		maxpage = s.find('span',attrs={"class":"current"}).get_text()		
		get_arturl(m,maxpage)

if __name__ == '__main__':
	main()
