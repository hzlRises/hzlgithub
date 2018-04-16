#coding:utf-8
import	HeaderData,re,sys
import requests,time
from bs4 import BeautifulSoup
from selenium import webdriver


reload(sys) 
sys.setdefaultencoding('utf8')

file_name = 'group_chaoshi'

circle_id = 20000541

page_num = 1




def jadge_page(url):
	'''
	browser = webdriver.PhantomJS(executable_path=r'D:\programfiles\anaconda\Lib\site-packages\selenium\webdriver\phantomjs\bin\phantomjs.exe')
	browser.get(url)
	page = browser.find_element_by_xpath('//*[@id="pageSpn"]/a[7]').text
	'''
	r = requests.get(url,headers=HeaderData.get_header(),timeout=60)
	page = re.search(r'setPage[\s\S].*?(\d+)',r.content)
	return int(page.group(1))
	
def generage_page_url(url,page):
	url_list = url.split('.')	
	for i in range(1,page+1):
		last_url = ''
		last_url = url_list[0]+'.'+url_list[1]+'.'+url_list[2]+'/p%s/t-1'%i+'.'+url_list[3]
		f.write(last_url+'\n')
		print last_url
	
	
def main():		
	#circle_list = ['http://group.jd.com/circle/all-circle/20000001.htm']	
	
	for t in range(1,page_num+1):#遍历每个一级导航下的所有圈子页数
		url = 'http://group.jd.com/circle/all-circle/s%s/p%s.htm'%(circle_id,t)
		try:
			r = requests.get(url,headers=HeaderData.get_header(),timeout=60)				
			s = BeautifulSoup(r.content,"lxml")
			imatag = s.find_all('div',attrs={"class":"item-img"})			
			for a in imatag:
				url =  'http:'+a.find('a').get('href')
				page = jadge_page(url)#判断该列表下总有多少页
				generage_page_url(url,page)
		except Exception,e:
			print e	
		
	


if __name__ == '__main__':
	f = open('%s_detail_url.txt'%file_name,r'a+')
	main()
	f.close()
	
	
	
	
'''

JD游戏 （电脑） > 全部圈子	http://group.jd.com/circle/all-circle/20000001.htm

手机站  > 全部圈子    		http://group.jd.com/circle/all-circle/20000151.htm

智能站  > 全部圈子			http://group.jd.com/circle/all-circle/20000121.htm

摄影站  > 全部圈子			http://group.jd.com/circle/all-circle/20000391.htm

娱乐站  > 全部圈子			http://group.jd.com/circle/all-circle/20000241.htm

妆比社(超市)  > 全部圈子	http://group.jd.com/circle/all-circle/20000541.htm


'''
