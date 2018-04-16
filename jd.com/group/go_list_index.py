#coding:utf-8
import	HeaderData
import requests,time
from bs4 import BeautifulSoup
file_name = 'group_chaoshi'

def main():	
	f = open('article_url_%s.txt'%file_name,r'a+')
	
	index_list = [url.strip() for url in open('%s_detail_url.txt'%file_name)]
	
	for url in index_list:#爬取		
		try:
			r = requests.get(url,headers=HeaderData.get_header(),timeout=60)
			s = BeautifulSoup(r.content,"lxml")
			content_url_list = s.find_all('h1')
			
		except Exception,e:
			print e
		if content_url_list:
			for atag in content_url_list:
				print atag.find('a').get('href')
				f.write(atag.find('a').get('href')+'\n')
		print url
		time.sleep(0.1)
		
	f.close()

