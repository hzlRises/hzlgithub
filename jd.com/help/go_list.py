#coding:utf-8
import	HeaderData
import requests,time
from bs4 import BeautifulSoup
file_name = 'help.jd.com_index'

def main():	
	f = open('%s_detail_url.txt'%file_name,r'a+')
	for i in range(1,1001):
		#爬取
		for page in range(1,21):
			url = 'http://help.jd.com/user/issue/list-%s.html?page=%s'%(i,page)
			try:	
				r = requests.get(url,headers=HeaderData.get_header(),timeout=60)
				s = BeautifulSoup(r.content,"lxml")
				content_url_list = s.find('ul',attrs={"class":"help_list"}).find_all('a')
				for atag in content_url_list:
					print atag.get('href')
					f.write(atag.get('href')+'\n')
			except Exception,e:
				print e
			print i,url
		'''	
		#保存		
		try:
			
		except Exception,e:
			print e
		'''
		
		
		
		
	f.close()



if __name__ == '__main__':
	main()
