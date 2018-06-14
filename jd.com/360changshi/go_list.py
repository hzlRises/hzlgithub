#coding:utf-8
import	HeaderData,re,sys
import requests,time
from bs4 import BeautifulSoup
reload(sys) 
sys.setdefaultencoding('utf8')

def get_arturl(m,maxpage):
	f = open('art_url.txt',r'a+')
	for i in range(1,int(maxpage)+1):
		time.sleep(0.1)
		try:
			url = m+'list_%s.html'%i
			if i == 1:
				url = m
			
			r = requests.get(url,headers=HeaderData.get_header(),timeout=60)
			if r.status_code == 200:
				s = BeautifulSoup(r.content,"lxml")
				#wzl = [soup.extract() for soup in s('div')]
				wzl = s.find_all('h3')				
				for t in wzl:					
					art_link = t.find('a').get('href')					
					f.write(art_link+'\n')	
			print i,maxpage		
		except Exception,e:
			print e
		
	f.close()
	time.sleep(2)
	
	
def main():
	mulu = [line.strip() for line in open('url.txt')]
	for m in mulu:
		try:
			url = m.strip().split(',')[0]
			r = requests.get(url,headers=HeaderData.get_header(),timeout=60)	
			s = BeautifulSoup(r.content,"lxml")		
			maxpage_a = s.find('div',attrs={"class":"paging"}).find_all('a')		
			#maxpage = int(maxpage.split('_')[-1].replace('.html',''))
			page_list = []
			
			for atag in maxpage_a:
				page = atag.get('href').split('/')[-1].replace('list_','').replace('.html','')
				page_list.append(page)						
			maxpage = int(page_list[-2])			
			get_arturl(url,maxpage)
		except Exception,e:
			print e

if __name__ == '__main__':
	main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
