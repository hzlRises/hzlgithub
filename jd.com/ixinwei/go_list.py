#coding:utf-8
import	HeaderData,re,sys
import requests,time
from bs4 import BeautifulSoup

reload(sys) 
sys.setdefaultencoding('utf8')


file_name = 'ixinwei'


def get_max_page(i):
	url = 'http://www.ixinwei.com/list/%s.html'%i
	page_last_num = ''	
	try:
		r = requests.get(url,headers=HeaderData.get_header(),timeout=60)
		page_list = re.findall('page=(\d+)',r.content)	
		page_last_num = page_list[-1]
	except Exception,e:
		print e
	if page_last_num:
		return int(page_last_num)
	else:
		return 0

def main():	
	for i in range(7,83):
		page = get_max_page(i)		
		for page in range(1,page+1):
			url = 'http://www.ixinwei.com/news.aspx?typeid2=%s&page=%s'%(i,page)
			try:
				r = requests.get(url,headers=HeaderData.get_header(),timeout=60)				
				s = BeautifulSoup(r.content,"lxml")
				atag = s.find_all('a',attrs={"class":"ntitlebold"})			
				for a in atag:
					url =  a.get('href')	
					f.write(url+'\n')
					print i,page
			except Exception,e:
				print e			
			time.sleep(0.1)
		
		
		
if __name__ == '__main__':
	f = open('%s_detail_url.txt'%file_name,r'a+')
	main()
	f.close()
	